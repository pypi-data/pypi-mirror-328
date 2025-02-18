import pkg_resources
from depgeist.scanner import scan_project

def check_dependencies():
    """Check which dependencies are installed and which are missing."""
    found_imports = scan_project()
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}

    missing = found_imports - installed_packages
    extra = installed_packages - found_imports

    if missing:
        print("\n⚠️ Missing Dependencies:")
        for dep in missing:
            print(f"  - {dep} (Try: pip install {dep})")

    if extra:
        print("\n🧹 Unused Installed Dependencies:")
        for dep in extra:
            print(f"  - {dep} (Consider removing)")

    return missing, extra