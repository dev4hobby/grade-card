import os
from pdf2image import convert_from_path
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')


def get_files_from_dir(dir: str) -> list:
    files = []
    for root, dirs, filenames in os.walk(dir):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def classify_by_extension(files: list) -> defaultdict:
    file_map = defaultdict(list)
    for filename in files:
        splited_filename = filename.split('.')
        ext = splited_filename[-1]
        name = '.'.join(splited_filename[:-1])
        file_map[ext].append(filename)
    return file_map

def create_directory(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)

def convert_pdf_to_jpg(pdf_files: list, jpg_dir: str):
    for pdf_file in pdf_files:
        # print("PDF FILE >> ", pdf_file)
        # print("JPG DIR >> ", jpg_dir)
        pages = convert_from_path(pdf_file, 500)
        file_name = '.'.join(pdf_file.split('/')[-1].split('.')[:-1])
        create_directory(os.path.join(jpg_dir, file_name))
        for i, page in enumerate(pages):
            page.save(os.path.join(jpg_dir, file_name, f'{i}.jpg'), 'JPEG')

if __name__ == "__main__":
    file_map_by_ext = classify_by_extension(
        get_files_from_dir(DATA_DIR)
    )
    
    if 'pdf' in file_map_by_ext:
        convert_pdf_to_jpg(
            file_map_by_ext['pdf'],
            os.path.join(DATA_DIR, 'jpg')
        )