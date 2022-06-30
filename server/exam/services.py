from utils.image import (
    find_edges,
    find_lines,
    get_text_from_image_array,
    split_page_area_by_index,
    serialize_image,
)
from utils.converter import convert_bytes_as_pages
from utils.aws import upload_bytes_to_s3
from django.conf import settings


def convert_document_to_images(pdf_file, min_line_length, max_line_gap, margin):
    file_name = pdf_file.name
    _bytes = pdf_file.read()
    pages = convert_bytes_as_pages(_bytes)
    urls = []

    result = {"common": [], "last": []}
    for i, page in enumerate(pages):
        edges = find_edges(page)
        if i == len(pages) - 1:
            min_line_length = 8000
            max_line_gap = 2000
        lines = find_lines(edges, min_line_length, max_line_gap)
        info = split_page_area_by_index(file_name, page, lines, i, len(pages)-1)
        if info.get("common"):
            result["common"] += info["common"]
        if info.get("last"):
            result["last"] += [_.split("\n")[:-1] for _ in info["last"]]
    
    for data in zip(result["common"], result["last"]):
        image_ndarray = data[0]
        item_info = data[1][0].split('.')
        answer = ""
        if len(item_info) == 1:
            for text in data[1]:
                if len(text.split('.')) == 1:
                    answer += text
                else:
                    item_info = [text.replace('.', '')]
            # TODO: 수식 및 기타 기호에 대한 대응이 필요한경우 구분자 변경 필요
            answer = ' '.join(answer).replace(' ', '_divide_')
        else:
            answer = item_info[1]
        file_name_without_ext = file_name.split('.')[0]
        key = f"{file_name_without_ext}/{item_info[0]}_{answer}.jpg"
        urls.append(upload_bytes_to_s3(key, serialize_image(image_ndarray)))
    return urls