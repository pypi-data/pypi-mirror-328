"""Package management for virtual environments"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Set
from ..ui.console import progress_status, print_error, console, print_warning
from rich.text import Text
from rich.tree import Tree
from rich.style import Style
from .package_analyzer import PackageAnalyzer
from .version_utils import parse_requirement_string
from .events import events, EventType
from packaging import version
import re
import requests


class PackageManager:
    """Package management for virtual environments"""

    def __init__(self, venv_path: Path):
        """Initialize package manager

        Args:
            venv_path: Path to the virtual environment
        """
        self.venv_path = venv_path
        self.requirements_path = Path("requirements.txt")
        self._pip_path = self._get_pip_path()

        # Initialize package analyzer with project root directory
        self.package_analyzer = PackageAnalyzer()

    def _check_pip_upgrade(self, stderr: str) -> None:
        """Check if pip needs upgrade and handle it

        Args:
            stderr: Error output from pip
        """
        if "new version of pip available" in stderr.lower():
            try:
                # Get current and latest version
                current_version = None
                latest_version = None
                for line in stderr.split("\n"):
                    if "new release" in line.lower():
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if part == "->":
                                current_version = parts[i - 1]
                                latest_version = parts[i + 1]
                                break

                if current_version and latest_version:
                    console.print(
                        f"[yellow]⚠ A new version of pip is available: {current_version} -> {latest_version}[/yellow]"
                    )
                    console.print(
                        "[dim]To update, run: pip install --upgrade pip[/dim]"
                    )
            except Exception:
                pass

    def _build_dependency_tree(
        self,
        name: str,
        version: str,
        deps: List[str],
        visited: Optional[Set[str]] = None,
    ) -> Tree:
        """Build a rich Tree structure for package dependencies"""
        if visited is None:
            visited = set()

        # Create tree node
        tree = Tree(
            Text.assemble(
                (name, "cyan"),
                ("==", "dim"),
                (version, "cyan"),
            )
        )

        # Add dependencies
        if deps:
            visited.add(name)
            for dep in sorted(deps):
                if dep not in visited:
                    dep_version = self._get_installed_version(dep)
                    dep_deps = self._check_dependencies(dep)
                    dep_tree = self._build_dependency_tree(
                        dep, dep_version, dep_deps, visited
                    )
                    tree.add(dep_tree)

        return tree

    def _update_dependency_files(
        self, *, added: List[str] = None, removed: List[str] = None
    ) -> None:
        """Update all dependency files (requirements.txt and pyproject.toml)

        Args:
            added: List of packages that were added
            removed: List of packages that were removed
        """
        # Update requirements.txt
        if added:
            self._update_requirements(added=added)
        if removed:
            self._update_requirements(removed=removed)

        # Update pyproject.toml if exists
        pyproject_path = Path("pyproject.toml")
        if pyproject_path.exists():
            from .pyproject_manager import PyProjectManager

            proj_manager = PyProjectManager(pyproject_path)

            if added:
                for pkg_spec in added:
                    try:
                        # Parse full package spec including extras
                        pkg_info = parse_requirement_string(pkg_spec)
                        pkg_name, pkg_extras, _, pkg_version = pkg_info

                        if not pkg_version:
                            # Get installed version if not specified
                            pkg_version = self._get_installed_version(pkg_name)

                        if pkg_version:
                            # Construct full package name with extras
                            if pkg_extras:
                                extras_str = f"[{','.join(sorted(pkg_extras))}]"
                                full_pkg_name = f"{pkg_name}{extras_str}"
                            else:
                                full_pkg_name = pkg_name

                            proj_manager.add_dependency(
                                full_pkg_name, pkg_version, ">="
                            )
                    except Exception as e:
                        print_warning(
                            f"Warning: Failed to add {pkg_name} to pyproject.toml: {str(e)}"
                        )

            if removed:
                for pkg_name in removed:
                    try:
                        proj_manager.remove_dependency(pkg_name)
                    except Exception as e:
                        print_warning(
                            f"Warning: Failed to remove {pkg_name} from pyproject.toml: {str(e)}"
                        )

    def add_packages(
        self,
        packages: List[str],
        *,
        dev: bool = False,
        editable: bool = False,
        no_deps: bool = False,
    ) -> Dict[str, Dict[str, Any]]:
        """Add packages to the virtual environment

        Args:
            packages: List of packages to add
            dev: Whether to install as development dependency
            editable: Whether to install in editable mode
            no_deps: Whether to skip installing package dependencies

        Returns:
            Dict with installation results for each package
        """
        results = {}
        successfully_added = []
        total_packages = len(packages)

        # Parse package specifications
        package_specs = [parse_requirement_string(pkg) for pkg in packages]

        for index, (
            pkg_name,
            pkg_extras,
            pkg_constraint,
            pkg_version,
        ) in enumerate(package_specs, 1):
            try:
                # Emit package installation start event
                events.emit(
                    EventType.Package.INSTALLING,
                    pkg_name,
                    extras=pkg_extras,
                    version=pkg_version,
                    constraint=pkg_constraint,
                    is_dependency=False,
                    total_packages=total_packages,
                    current_index=index,
                )
                # Install package
                cmd = [str(self._pip_path), "install"]
                if editable:
                    cmd.append("-e")
                if no_deps:
                    cmd.append("--no-deps")

                # Construct package spec with extras if present
                if pkg_extras:
                    extras_str = f"[{','.join(sorted(pkg_extras))}]"
                    pkg_spec = f"{pkg_name}{extras_str}"
                else:
                    pkg_spec = pkg_name

                if pkg_version:
                    pkg_spec = f"{pkg_spec}=={pkg_version}"

                cmd.append(pkg_spec)

                process = subprocess.run(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )

                if process.returncode == 0:
                    # Get installed version and dependencies
                    self.package_analyzer.clear_cache()
                    packages_after = (
                        self.package_analyzer.get_installed_packages()
                    )

                    # Try to find the package with case-insensitive matching
                    pkg_name_lower = pkg_name.lower()
                    matching_pkg = None
                    for installed_pkg, info in packages_after.items():
                        if installed_pkg.lower() == pkg_name_lower:
                            matching_pkg = installed_pkg
                            pkg_info = info
                            break

                    if matching_pkg:
                        version = pkg_info["installed_version"]
                        # Construct full package spec with extras
                        if pkg_extras:
                            extras_str = f"[{','.join(sorted(pkg_extras))}]"
                            full_pkg_spec = (
                                f"{matching_pkg}{extras_str}=={version}"
                            )
                        else:
                            full_pkg_spec = f"{matching_pkg}=={version}"

                        successfully_added.append(full_pkg_spec)
                        results[matching_pkg] = {
                            "status": "installed",
                            "version": version,
                            "extras": pkg_extras,  # Store extras information
                            "dependencies": sorted(pkg_info["dependencies"]),
                            "new_dependencies": sorted(
                                pkg_info["dependencies"]
                            ),
                        }
                        # Emit package installation success event
                        events.emit(
                            EventType.Package.INSTALLED,
                            matching_pkg,
                            extras=pkg_extras,
                            version=version,
                            total_packages=total_packages,
                            current_index=index,
                            dependencies=pkg_info["dependencies"],
                        )
                else:
                    # Extract version information from pip's error output
                    error_output = (
                        process.stderr if process.stderr else "Unknown error"
                    )
                    version_info = {}

                    # Try to get available versions from error message
                    if (
                        "Could not find a version that satisfies the requirement"
                        in error_output
                    ):
                        try:
                            # Extract versions from error message
                            versions = []
                            for line in error_output.split("\n"):
                                if "from versions:" in line:
                                    versions_str = line.split(
                                        "from versions:", 1
                                    )[1].strip()
                                    versions = [
                                        v.strip()
                                        for v in versions_str.strip("()").split(
                                            ","
                                        )
                                    ]
                                    break

                            if versions:
                                version_info["latest_versions"] = ", ".join(
                                    f"[cyan]{v}[/cyan]"
                                    for v in versions[-3:][::-1]
                                )
                                version_info["similar_versions"] = ", ".join(
                                    f"[cyan]{v}[/cyan]"
                                    for v in versions[-6:-3][::-1]
                                )
                        except Exception:
                            # If parsing fails, try to get from PyPI
                            try:
                                response = requests.get(
                                    f"https://pypi.org/pypi/{pkg_name}/json"
                                )
                                if response.status_code == 200:
                                    data = response.json()
                                    versions = sorted(
                                        data["releases"].keys(), reverse=True
                                    )
                                    version_info["latest_versions"] = ", ".join(
                                        f"[cyan]{v}[/cyan]"
                                        for v in versions[:3]
                                    )
                                    version_info["similar_versions"] = (
                                        ", ".join(
                                            f"[cyan]{v}[/cyan]"
                                            for v in versions[3:6]
                                        )
                                    )
                            except Exception:
                                pass

                    results[pkg_name] = {
                        "status": "error",
                        "message": error_output,
                        "version_info": version_info,
                    }
                    # Emit package installation failure event
                    events.emit(
                        EventType.Package.FAILED,
                        pkg_name,
                        extras=pkg_extras,
                        error=error_output,
                        version_info=version_info,
                        total_packages=total_packages,
                        current_index=index,
                    )

            except Exception as e:
                results[pkg_name] = {
                    "status": "error",
                    "message": str(e),
                }
                # Emit package installation error event
                events.emit(
                    EventType.Package.FAILED,
                    pkg_name,
                    extras=pkg_extras,
                    error=str(e),
                    total_packages=total_packages,
                    current_index=index,
                )

        # Update dependency files only after successful installations
        if successfully_added:
            self._update_dependency_files(added=successfully_added)

        return results

    def get_packages_to_remove(
        self,
        package_names: List[str],
        excluded_packages: Optional[List[str]] = None,
    ) -> Dict[str, List[Dict[str, str]]]:
        """
        Get a list of unique dependencies (including itself) for multiple top-level packages,
        excluding specified packages (excluded packages will be considered as shared dependencies and not included in the removal list)

        Args:
        package_names: List of packages to remove
        excluded_packages: List of packages to exclude

        Returns:
        Dict[str, List[Dict[str, str]]]: Format is
        {top-level package name: [{name: package name, installed_version: version}, ...]}
        """
        # Get full dependency tree
        dependency_tree = self.package_analyzer.get_dependency_tree()

        # Internal function: Recursively collect dependencies of a package and its sub-dependencies
        def gather_deps(
            pkg_obj: Dict, visited: Optional[Set[str]] = None
        ) -> Dict[str, Dict]:
            if visited is None:
                visited = set()
            pkg_name = pkg_obj.get("name")
            if not pkg_name or pkg_name in visited:
                return {}
            visited.add(pkg_name)
            result = {pkg_name: pkg_obj}
            for dep in pkg_obj.get("dependencies", {}).values():
                result.update(gather_deps(dep, visited))
            return result

        removal_set = set(package_names)
        non_removal_top_levels = set(dependency_tree.keys()) - removal_set

        # Collect removal candidates for each package to be removed
        removal_candidates = {}
        for pkg_name in package_names:
            if pkg_name not in dependency_tree:
                continue
            removal_candidates[pkg_name] = gather_deps(
                dependency_tree[pkg_name]
            )

        # Collect non-removal top-level packages and their dependencies (considered as shared dependencies)
        non_removal_deps = {}
        for pkg_name in non_removal_top_levels:
            non_removal_deps.update(gather_deps(dependency_tree[pkg_name]))

        # Convert excluded packages to set
        excluded_set = (
            set(excluded_packages) if excluded_packages is not None else set()
        )

        # Exclude shared dependencies and pre-excluded packages, get unique dependencies
        result = {}
        for top_pkg, candidate in removal_candidates.items():
            removable = {}
            for pkg_name, pkg_info in candidate.items():
                if (
                    pkg_name not in non_removal_deps
                    and pkg_name not in excluded_set
                ):
                    removable[pkg_name] = pkg_info
            result[top_pkg] = [
                {
                    "name": info["name"],
                    "installed_version": info["installed_version"],
                }
                for info in removable.values()
            ]

        return result

    def remove_packages(
        self,
        packages: List[str],
        excluded_packages: Optional[List[str]] = None,
    ) -> Dict[str, Dict[str, Any]]:
        """
        Remove packages and their unnecessary dependencies

        Args:
            packages: List of packages to remove

        Returns:
            Dict containing removal results
        """
        results = {}
        dependency_tree = self.package_analyzer.get_dependency_tree()

        # Get all packages that can be safely removed
        removable_packages = self.get_packages_to_remove(
            packages, excluded_packages
        )
        all_to_remove = set()  # Collect all packages to remove
        pkg_versions = {}  # Collect all package version information

        # Collect all packages and their version information to remove
        for pkg_deps in removable_packages.values():
            for dep in pkg_deps:
                pkg_name = dep["name"]
                all_to_remove.add(pkg_name)
                pkg_versions[pkg_name] = dep["installed_version"]

        # First check if the top-level packages to remove exist
        for pkg_name in packages:
            pkg_info = dependency_tree.get(pkg_name, {})
            if not pkg_info:
                results[pkg_name] = {
                    "status": "not_found",
                    "message": f"Package {pkg_name} is not installed",
                }
                all_to_remove.discard(
                    pkg_name
                )  # Remove from removal list if not found
                continue

            # Collect this package's unique dependencies
            removable_deps = {}
            pkg_deps = removable_packages.get(pkg_name, [])
            for dep in pkg_deps:
                dep_name = dep["name"]
                if dep_name != pkg_name:  # Exclude itself
                    removable_deps[dep_name] = dep["installed_version"]

            try:
                # Execute pip uninstall
                process = subprocess.run(
                    [str(self._pip_path), "uninstall", "-y", pkg_name],
                    capture_output=True,
                    text=True,
                )

                if process.returncode == 0:
                    results[pkg_name] = {
                        "status": "removed",
                        "version": pkg_versions.get(pkg_name),
                        "removable_deps": removable_deps,
                    }
                else:
                    results[pkg_name] = {
                        "status": "error",
                        "message": process.stderr,
                    }

            except Exception as e:
                results[pkg_name] = {
                    "status": "error",
                    "message": str(e),
                }

        # Remove remaining dependency packages
        remaining_deps = all_to_remove - set(packages)
        for dep_name in sorted(remaining_deps):
            if dep_name not in results:  # Avoid duplicate removal
                try:
                    process = subprocess.run(
                        [str(self._pip_path), "uninstall", "-y", dep_name],
                        capture_output=True,
                        text=True,
                    )

                    if process.returncode == 0:
                        results[dep_name] = {
                            "status": "removed",
                            "version": pkg_versions.get(dep_name),
                            "is_dependency": True,
                        }
                    else:
                        results[dep_name] = {
                            "status": "error",
                            "message": process.stderr,
                        }

                except Exception as e:
                    results[dep_name] = {
                        "status": "error",
                        "message": str(e),
                    }

        # Update dependency files
        self._update_dependency_files(removed=list(all_to_remove))

        return results

    def _get_installed_packages(self) -> Dict[str, Dict[str, Any]]:
        """Get installed packages and their information

        Returns:
            Dict mapping package names to their information
        """
        return self.package_analyzer.get_installed_packages()

    def _get_all_dependencies(self) -> Dict[str, Set[str]]:
        """Get all packages and their dependents

        Returns:
            Dict mapping package names to sets of packages that depend on them
        """
        packages = self._get_installed_packages()
        dependents = {}

        # Build dependency map
        for pkg_name, pkg_info in packages.items():
            for dep in pkg_info["dependencies"]:
                if dep not in dependents:
                    dependents[dep] = set()
                dependents[dep].add(pkg_name)

        return dependents

    def _get_installed_version(self, package: str) -> Optional[str]:
        """Get installed version of a package

        Args:
            package: Package name

        Returns:
            Version string if installed, None otherwise
        """
        packages = self.package_analyzer.get_installed_packages()
        if package in packages:
            return packages[package]["installed_version"]
        return None

    def _check_conflicts(
        self,
        package_specs: List[Tuple[str, Optional[str]]],
        existing: Dict[str, str],
    ) -> List[Dict[str, Any]]:
        """Check for version conflicts"""
        conflicts = []
        for name, version in package_specs:
            if name in existing and version and existing[name] != version:
                conflicts.append(
                    {
                        "package": name,
                        "requested": version,
                        "installed": existing[name],
                    }
                )
        return conflicts

    def _check_dependencies(self, package: str) -> List[str]:
        """Get dependencies of a package

        Args:
            package: Package name

        Returns:
            List of dependency names
        """
        packages = self.package_analyzer.get_installed_packages()
        if package in packages:
            return packages[package]["dependencies"]
        return []

    def _is_dependency(self, package: str) -> Tuple[bool, List[str]]:
        """Check if package is a dependency of other packages

        Args:
            package: Package name to check

        Returns:
            Tuple of (is_dependency, list_of_dependent_packages)
        """
        packages = self.package_analyzer.get_installed_packages()
        dependents = []

        for pkg_name, pkg_info in packages.items():
            if pkg_name != package and package in pkg_info["dependencies"]:
                dependents.append(pkg_name)

        return bool(dependents), dependents

    def _update_requirements(
        self,
        added: Optional[List[str]] = None,
        removed: Optional[List[str]] = None,
        dev: bool = False,
    ) -> None:
        """Update requirements.txt with added or removed packages

        Args:
            added: List of packages to add
            removed: List of packages to remove
            dev: Whether to update dev dependencies
        """
        if not self.requirements_path.exists():
            # Create empty requirements file if it doesn't exist
            self.requirements_path.touch()

        # Read existing requirements
        with open(self.requirements_path, "r") as f:
            requirements = f.readlines()

        # Remove packages if specified
        if removed:
            new_requirements = []
            for req in requirements:
                req = req.strip()
                if not req or req.startswith("#"):
                    new_requirements.append(req + "\n")
                    continue

                # Parse requirement to get package name
                pkg_info = parse_requirement_string(req)
                pkg_name = pkg_info[0]  # Get package name only

                if pkg_name not in removed:
                    new_requirements.append(req + "\n")
            requirements = new_requirements

        # Add new packages if specified
        if added:
            # Convert added packages to set for deduplication
            added_set = set()
            for pkg_spec in added:
                pkg_info = parse_requirement_string(pkg_spec)
                pkg_name, pkg_extras, _, pkg_version = pkg_info

                # Construct full package spec with extras
                if pkg_extras:
                    extras_str = f"[{','.join(sorted(pkg_extras))}]"
                    full_pkg_name = f"{pkg_name}{extras_str}"
                else:
                    full_pkg_name = pkg_name

                if pkg_version:
                    added_set.add(f"{full_pkg_name}=={pkg_version}")
                else:
                    # Get installed version if not specified
                    version = self._get_installed_version(pkg_name)
                    if version:
                        added_set.add(f"{full_pkg_name}=={version}")

            # Remove existing entries for added packages
            new_requirements = []
            for req in requirements:
                req = req.strip()
                if not req or req.startswith("#"):
                    new_requirements.append(req + "\n")
                    continue

                # Parse requirement to get package name
                pkg_info = parse_requirement_string(req)
                pkg_name = pkg_info[0]  # Get package name only

                if pkg_name not in [
                    p.split("==")[0].split("[")[0] for p in added_set
                ]:
                    new_requirements.append(req + "\n")

            # Add new packages
            new_requirements.extend(f"{pkg}\n" for pkg in sorted(added_set))
            requirements = new_requirements

        # Write updated requirements
        # Sort all non-comment lines while preserving comments
        sorted_requirements = []
        package_lines = []
        comment_lines = []

        for line in requirements:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                comment_lines.append(line + "\n")
            else:
                package_lines.append(line)

        # Sort package lines
        package_lines.sort(key=str.lower)

        # Combine comments and sorted packages
        sorted_requirements.extend(comment_lines)
        if (
            comment_lines and package_lines
        ):  # Add a blank line between comments and packages
            sorted_requirements.append("\n")
        sorted_requirements.extend(f"{pkg}\n" for pkg in package_lines)

        with open(self.requirements_path, "w") as f:
            f.writelines(sorted_requirements)

    def _get_pip_path(self) -> Path:
        """Get path to pip executable"""
        if sys.platform == "win32":
            pip_path = self.venv_path / "Scripts" / "pip.exe"
        else:
            pip_path = self.venv_path / "bin" / "pip"

        if not pip_path.exists():
            raise RuntimeError(f"pip not found at {pip_path}")

        return pip_path

    def _get_pip_versions(
        self, stderr: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """Extract current and latest pip versions from stderr"""
        current_version = None
        latest_version = None
        for line in stderr.split("\n"):
            if "new release" in line.lower():
                parts = line.split()
                for i, part in enumerate(parts):
                    if part == "->":
                        current_version = parts[i - 1]
                        latest_version = parts[i + 1]
                        break
        return current_version, latest_version

    def auto_fix_install(
        self,
        package_name: str,
        version: Optional[str] = None,
        *,
        dev: bool = False,
        editable: bool = False,
        no_deps: bool = False,
    ) -> Dict[str, Any]:
        """
        Install a package with automatic version fixing if needed.

        Args:
            package_name: Name of the package to install
            version: Optional version specification
            dev: Whether to install as development dependency
            editable: Whether to install in editable mode
            no_deps: Whether to skip installing package dependencies

        Returns:
            Dict containing installation results with status and additional info
        """
        # Clean and format version string
        if version:
            version = str(version).strip()
            # If version string does not contain version constraints, add ==
            if not any(
                version.startswith(op)
                for op in [">=", "<=", "!=", "~=", ">", "<", "=="]
            ):
                version = version.lstrip("=").strip()
                package_spec = f"{package_name}=={version}"
            else:
                package_spec = f"{package_name}{version}"
        else:
            package_spec = package_name

        # Try to install
        results = self.add_packages(
            [package_spec],
            dev=dev,
            editable=editable,
            no_deps=no_deps,
        )

        pkg_info = results.get(package_name, {})

        # If installation fails, check if automatic fixing is needed
        if pkg_info.get("status") != "installed":
            error_msg = pkg_info.get("message", "")
            version_info = pkg_info.get("version_info", {})

            # Check if it's a version-related error
            if (
                "Version not found" in error_msg
                or "No matching distribution" in error_msg
                or "Could not find a version that satisfies the requirement"
                in error_msg
            ) and version_info:
                # Get latest version
                latest_version = (
                    version_info["latest_versions"]
                    .split(",")[0]
                    .strip()
                    .replace("[cyan]", "")
                    .replace("[/cyan]", "")
                    .replace(" (latest)", "")
                )

                # Analyze update reason
                if (
                    "Python version" in error_msg
                    or "requires Python" in error_msg
                ):
                    update_reason = "Python compatibility issue"
                elif "dependency conflict" in error_msg:
                    update_reason = "Dependency conflict"
                elif (
                    "not found" in error_msg
                    or "No matching distribution" in error_msg
                ):
                    update_reason = "Version not found"
                else:
                    update_reason = "Installation failed"

                # Use latest version to retry
                retry_results = self.add_packages(
                    [f"{package_name}=={latest_version}"],
                    dev=dev,
                    editable=editable,
                    no_deps=no_deps,
                )

                retry_info = retry_results.get(package_name, {})
                if retry_info.get("status") == "installed":
                    retry_info["auto_fixed"] = True
                    retry_info["original_version"] = version
                    retry_info["update_reason"] = update_reason
                    retry_info["installed_version"] = latest_version
                    return retry_info

                # If retry also fails, return retry error information
                return retry_info

        return pkg_info


def _get_pre_release_type_value(pre_type: str) -> int:
    """Get numeric value for pre-release type for ordering"""
    pre_type_order = {"a": 0, "b": 1, "rc": 2}
    return pre_type_order.get(pre_type, 3)


def get_version_distance(ver_str: str, target_str: str) -> float:
    """Calculate distance between two version strings with improved handling of pre-releases"""
    # Parse versions using packaging.version
    ver = version.parse(ver_str)
    target = version.parse(target_str)

    # Get release components
    ver_release = ver.release
    target_release = target.release

    # Pad with zeros to make same length
    max_len = max(len(ver_release), len(target_release))
    ver_parts = list(ver_release) + [0] * (max_len - len(ver_release))
    target_parts = list(target_release) + [0] * (max_len - len(target_release))

    # Calculate weighted distance for release parts
    distance = 0
    for i, (a, b) in enumerate(zip(ver_parts, target_parts)):
        weight = 10 ** (max_len - i - 1)
        distance += abs(a - b) * weight

    # Add pre-release penalty
    pre_release_penalty = 0
    if ver.is_prerelease or target.is_prerelease:
        # Penalize pre-releases but still keep them close to their release version
        pre_release_penalty = 0.5

        # If both are pre-releases, reduce penalty and compare their order
        if ver.is_prerelease and target.is_prerelease:
            pre_release_penalty = 0.25
            # Compare pre-release parts
            if ver.pre and target.pre:
                pre_type_diff = abs(
                    _get_pre_release_type_value(ver.pre[0])
                    - _get_pre_release_type_value(target.pre[0])
                )
                pre_num_diff = abs(ver.pre[1] - target.pre[1])
                pre_release_penalty += (
                    pre_type_diff + pre_num_diff * 0.1
                ) * 0.25

    return distance + pre_release_penalty
