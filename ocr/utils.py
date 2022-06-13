import os
from collections import defaultdict


def get_files_from_dir(dir: str) -> list:
    files = []
    for root, dirs, filenames in os.walk(dir):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


def classify_by_extension(files: list) -> defaultdict:
    file_map = defaultdict(list)
    for filename in files:
        splited_filename = filename.split(".")
        ext = splited_filename[-1]
        name = ".".join(splited_filename[:-1])
        file_map[ext].append(filename)
    return file_map


def create_directory(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)
