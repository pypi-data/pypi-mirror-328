import subprocess
import pkg_resources

def suggest_updates():
    """Check for outdated dependencies and suggest updates."""
    outdated_packages = []
    
    try:
        result = subprocess.run(["pip", "list", "--outdated"], capture_output=True, text=True)
        lines = result.stdout.split("\n")[2:]

        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                package, current, latest = parts[:3]
                outdated_packages.append((package, current, latest))

    except Exception as e:
        print(f"Error fetching outdated packages: {e}")
        return

    if outdated_packages:
        print("\n📢 Outdated Packages:")
        for package, current, latest in outdated_packages:
            print(f"  - {package}: {current} → {latest} (Upgrade: pip install --upgrade {package})")
    else:
        print("\n✅ All packages are up to date!")

    return outdated_packages