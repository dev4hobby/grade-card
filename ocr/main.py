import os
from utils import get_files_from_dir, classify_by_extension
from pdf_converter import pdf2jpg
from img_processor import split_area
from constants import DATA_DIR, JPG_DIR

if __name__ == "__main__":
    file_map_by_ext = classify_by_extension(get_files_from_dir(DATA_DIR))

    if "jpg" not in file_map_by_ext:
        if "pdf" in file_map_by_ext:
            pdf2jpg(file_map_by_ext["pdf"], JPG_DIR)

        file_map_by_ext = classify_by_extension(get_files_from_dir(DATA_DIR))

    if "jpg" in file_map_by_ext:
        split_area(file_map_by_ext["jpg"])
