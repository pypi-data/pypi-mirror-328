import os
import sys
from .templates import get_main_template, get_utils_template, get_readme_template

def create_structure() -> None: 
    root_dir = os.getcwd()
    structure = {
        "src": {
            "utils.py": get_utils_template(),
        },
        "example.py": get_main_template(),
        "README.md": get_readme_template(),
    }

    for folder, files in structure.items():
        path = os.path.join(root_dir, folder)
        if isinstance(files, dict):  # If folder contains files
            os.makedirs(path, exist_ok=True)
            for file, content in files.items():
                file_path = os.path.join(path, file)
                with open(file_path, "w") as f:
                    f.write(content)
        else:  # Single file at the root
            with open(os.path.join(root_dir, folder), "w") as f:
                f.write(files)

    print(f"Project structure for FederatedModel upload created successfully in {root_dir}.")

def main():
    if len(sys.argv) < 2:
        print("Usage: msi <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        create_structure()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

