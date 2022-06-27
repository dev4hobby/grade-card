from . import (
    os,
    np,
    cv2,
    pytesseract,
)
from .constants import JPG_DIR, OUTPUT_DIR
from .directory import create_directory

def get_text_from_image_array(image_array, language="eng"):
    kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    image_array = 255 - image_array
    image_array = cv2.dilate(image_array, kern, iterations=1)
    image_array = 255 - image_array
    text_info = pytesseract.image_to_string(image_array, lang=language, config = '--psm 6 --oem 3 -c tessedit_char_whitelist=-.0123456789')
    return text_info

def find_edges(page):
    image = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(gray, 50, 200, apertureSize=3)
    return edges

def find_lines(edges, min_line_length, max_line_gap):
    lines = [
        _.tolist()
        for _ in cv2.HoughLinesP(
            edges, 1, 3 * np.pi / 360, 100, min_line_length, max_line_gap
        )
    ]

    lines.sort(key=lambda lines: sum(lines[0]))
    del lines[1::2]
    return lines

async def split_text_area(image, option={"morph_pos":(150, 150), "erode_iter":3, "last":False}):
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (option["morph_pos"][0], option["morph_pos"][1]))
    erode = cv2.erode(image, vertical_kernel, iterations=option["erode_iter"])

    # contour를 찾으려면 흑백 전환을 시켜야한다. 그래서 흑백으로 변환한다.
    erode = 255 - erode

    # contour 찾기
    contours, hierarchy = cv2.findContours(
        erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    contours = contours[::-1]
    if option["last"]:
        contours = contours[1:-1]

    # box 그리기
    result = {
        "common": [],
        "last": [],
    }
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        if option["last"]:
            rectarea = image[y : y + h, x : x + w]
            result["last"].append(get_text_from_image_array(rectarea, "kor+eng"))
        else:
            result["common"].append(image[y:y+h, x:x+w])
    return result

async def split_page_area_by_index(file_name, image, lines, index:int, max_index:int, margin:int=15):
    text_list = []
    image_info = {"common": [], "last": []}
    option={"morph_pos":(150, 150), "erode_iter":3, "last":False}
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if index == 0:
        title = image[0 : lines[0][0][3] - margin, 0 : lines[0][0][2]]
        school = image[lines[0][0][3] + margin * 2 : lines[1][0][3] - margin, lines[1][0][0] : lines[1][0][2]]
        content_left = gray[lines[1][0][3] + margin : lines[3][0][3] - margin, 0 + margin : lines[2][0][0] - margin]
        content_right = gray[lines[1][0][3] + margin : lines[3][0][3] - margin, lines[2][0][0] + margin :]
        text_list.append(get_text_from_image_array(title, language="kor+eng"))
        text_list.append(get_text_from_image_array(school, language="kor+eng"))    
    elif index < max_index:
        content_left = gray[lines[0][0][3] + margin : lines[2][0][3] - margin, 0 + margin : lines[1][0][0] - margin]
        content_right = gray[lines[0][0][3] + margin : lines[2][0][3] - margin, lines[1][0][0] + margin :]
    else:
        content_left = gray[lines[0][0][3] + margin : lines[2][0][3] - margin, 0 + margin : lines[1][0][0] - margin]
        content_right = gray[lines[0][0][3] + margin : lines[2][0][3] - margin, lines[1][0][0] + margin :]
        option = option = {
            "morph_pos":(20, 20),
            "erode_iter":2,
            "last": True
        }
    left_result = await split_text_area(image=content_left, option = option)
    right_result = await split_text_area(image=content_right, option = option)

    image_info["common"] += left_result["common"]
    image_info["common"] += right_result["common"]
    image_info["last"] += left_result["last"]
    image_info["last"] += right_result["last"]
    return image_info

def serialize_image(ndarray):
    return cv2.imencode(".jpg", ndarray)[1].tobytes()
