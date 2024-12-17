import os
from pathlib import Path
def clean_files(folder_path):
    folder_path=Path(folder_path)
    for file_path in folder_path.iterdir():
        if file_path.is_dir():
            clean_files(file_path)
        else:
            file_path.unlink()