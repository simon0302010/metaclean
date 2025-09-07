# reused and modified from simon0302010/MetaView

import json
import os
import subprocess


def check_installed():
    try:
        result = subprocess.run(
            ["exiftool", "-ver"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.returncode == 0
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_metadata(file_path):
    result = subprocess.run(
        ["exiftool", "-j", "-b", file_path], capture_output=True, text=True
    )
    metadata = json.loads(result.stdout)
    return metadata[0] if metadata else {}

# TODO: deletion of permanent data
def delete_metadata(file_path, all=True, properties=[]):
    if os.path.exists(file_path):
        if all:
            command = ["exiftool", "-overwrite_original", "-All=", file_path]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.stderr.strip():
                return False
            return result.stdout.strip()
        elif properties:
            command = ["exiftool", "-overwrite_original"]
            for property in properties:
                command.append(f"-{property}=")
            command.append(file_path)
            result = subprocess.run(command, capture_output=True, text=True)
            if result.stderr.strip():
                return False
            return result.stdout.strip()
