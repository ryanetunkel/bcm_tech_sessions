from pathlib import Path


def check_if_manifest_exist(directory: Path):
    for file in directory.glob("*"):
        if file.name == "Manifest.txt":
            return True
    return False
