import json
import os
import subprocess
import sys

def _get_exiftool_path():
    if hasattr(sys, '_MEIPASS'):
        exe_name = "exiftool.exe" if sys.platform.startswith("win") else "exiftool"
        exe_path = os.path.join(sys._MEIPASS, 'metaclean', 'core', exe_name)
        return exe_path
    exe_name = "exiftool.exe" if sys.platform.startswith("win") else "exiftool"
    return exe_name

def check_installed():
    exiftool_path = _get_exiftool_path()
    try:
        result = subprocess.run(
            [exiftool_path, "-ver"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.returncode == 0
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_metadata(file_path):
    exiftool_path = _get_exiftool_path()
    result = subprocess.run(
        [exiftool_path, "-j", "-b", file_path], capture_output=True, text=True
    )
    metadata = json.loads(result.stdout)
    return metadata[0] if metadata else {}

def delete_metadata(file_path, all=True, properties=[]):
    exiftool_path = _get_exiftool_path()
    if os.path.exists(file_path):
        if all:
            command = [exiftool_path, "-overwrite_original", "-All=", file_path]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.stderr.strip():
                return False
            return result.stdout.strip()
        elif properties:
            command = [exiftool_path, "-overwrite_original"]
            for property in properties:
                command.append(f"-{property}=")
            command.append(file_path)
            result = subprocess.run(command, capture_output=True, text=True)
            if result.stderr.strip():
                return False
            return result.stdout.strip()