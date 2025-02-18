import argparse
from depgeist.scanner import scan_project
from depgeist.checker import check_dependencies
from depgeist.updater import suggest_updates

def main():
    parser = argparse.ArgumentParser(prog="depgeist", description="A smart dependency checker.")
    
    subparsers = parser.add_subparsers(dest="command")

    # Scan command
    scan_parser = subparsers.add_parser("scan", help="Scan the project for missing dependencies.")
    scan_parser.add_argument("path", nargs="?", default=".", help="Project directory (default: current)")

    # Check command
    check_parser = subparsers.add_parser("check", help="Check for installed vs required dependencies.")

    # Update command
    update_parser = subparsers.add_parser("update", help="Suggest updates for outdated dependencies.")

    args = parser.parse_args()

    if args.command == "scan":
        scan_project(args.path)
    elif args.command == "check":
        check_dependencies()
    elif args.command == "update":
        suggest_updates()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()