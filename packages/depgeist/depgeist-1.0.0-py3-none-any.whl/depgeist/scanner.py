import os
import ast

def scan_project(path="."):
    """Scan a project directory for used dependencies."""
    dependencies = set()

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read(), filename=file_path)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    dependencies.add(alias.name)
                            elif isinstance(node, ast.ImportFrom) and node.module:
                                dependencies.add(node.module)
                    except SyntaxError:
                        print(f"Skipping file with syntax errors: {file_path}")

    print("\n📌 Found Imports:", dependencies)
    return dependencies