import os
from pdf2image import convert_from_path
from utils import create_directory


def pdf2jpg(pdf_files: list, jpg_dir: str):
    for pdf_file in pdf_files:
        pages = convert_from_path(pdf_file, 500)
        file_name = ".".join(pdf_file.split("/")[-1].split(".")[:-1])
        create_directory(os.path.join(jpg_dir, file_name))
        for i, page in enumerate(pages):
            page.save(os.path.join(jpg_dir, file_name, f"{i}.jpg"), "JPEG")

if __name__ == "__main__":
    from constants import PDF_DIR, JPG_DIR
    from os import path
    pdf2jpg([path.join(PDF_DIR, "2.pdf")], JPG_DIR)