import os
import cv2
import numpy as np
import pytesseract
from PIL import Image
from constants import JPG_DIR
from random import randint
from constants import OUTPUT_DIR, JPG_DIR
from os import path
from utils import create_directory

last_count = 1

def split_area(image_path_list, minLineLength=5000, maxLineGap=1000, margin=15, debug=False):
    image_path_list.sort()
    for image_index, image_path in enumerate(image_path_list):
        image = cv2.imread(image_path)
        """
        # 복사용지를 스캔하여 사용하는경우 블러처리하여 노이즈 제거
        # blur = cv2.bilateralFilter(image, 10, 75, 75)
        # gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        """
        # Grayscale and threshold the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        # Find edge, to split area
        edges = cv2.Canny(gray, 50, 200, apertureSize=3)

        if image_index == len(image_path_list) - 1:
            minLineLength = 8000
            maxLineGap = 2000

        lines = [
            x.tolist()
            for x in cv2.HoughLinesP(
                edges, 1, 3 * np.pi / 360, 100, minLineLength, maxLineGap
            )
        ]
        lines.sort(key=lambda lines: sum(lines[0]))
        del lines[1::2]

        if image_index == 0:
            print("맨 앞장")
            title = image[0 : lines[0][0][3] - margin, 0 : lines[0][0][2]]
            school = image[
                lines[0][0][3] + margin * 2 : lines[1][0][3] - margin,
                lines[1][0][0] : lines[1][0][2],
            ]
            content_left = gray[
                lines[1][0][3] + margin : lines[3][0][3] - margin,
                0 + margin : lines[2][0][0] - margin,
            ]
            content_right = gray[
                lines[1][0][3] + margin : lines[3][0][3] - margin,
                lines[2][0][0] + margin :,
            ]
            if debug:
                cv2.imshow("content_left_origin", content_left)
                cv2.moveWindow("content_left_origin", 0, 0)
                cv2.imshow("content_right_origin", content_right)
                cv2.moveWindow("content_right_origin", 400, 0)
                content_left = split_textarea(content_left, image_path = image_path)
                content_right = split_textarea(content_right, image_path = image_path)
                cv2.imshow("content_left", content_left)
                cv2.moveWindow("content_left", 800, 0)
                cv2.imshow("content_right", content_right)
                cv2.moveWindow("content_right", 1200, 0)
            else:
                get_text_from_image_array(title)
                get_text_from_image_array(school)
                split_textarea(image_area=content_left, image_path = image_path)
                split_textarea(image_area=content_right, image_path = image_path)
            

        elif image_index < len(image_path_list) - 1:
            content_left = gray[
                lines[0][0][3] + margin : lines[2][0][3] - margin,
                0 + margin : lines[1][0][0] - margin,
            ]
            content_right = gray[
                lines[0][0][3] + margin : lines[2][0][3] - margin,
                lines[1][0][0] + margin :,
            ]
            if debug:
                print("내용있는 장")
                cv2.imshow("content_left_origin", content_left)
                cv2.moveWindow("content_left_origin", 0, 0)
                cv2.imshow("content_right_origin", content_right)
                cv2.moveWindow("content_right_origin", 400, 0)
                content_left = split_textarea(content_left)
                content_right = split_textarea(content_right)
                cv2.imshow("content_left", content_left)
                cv2.moveWindow("content_left", 800, 0)
                cv2.imshow("content_right", content_right)
                cv2.moveWindow("content_right", 1200, 0)
            else:
                split_textarea(image_area=content_left, image_path = image_path)
                split_textarea(image_area=content_right, image_path = image_path)
        else:
            content_left = gray[
                lines[0][0][3] + margin : lines[2][0][3] - margin,
                0 + margin : lines[1][0][0] - margin,
            ]
            

            content_right = gray[
                lines[0][0][3] + margin : lines[2][0][3] - margin,
                lines[1][0][0] + margin :,
            ]
            
            
            if debug:
                print("정답지")
                last_area = split_textarea(gray, image_path = image_path, save=False)
                cv2.imshow("paper", last_area)
            else:
                last_left_area = split_textarea(content_left, image_path = image_path, save=False, option = {
                    "morph_pos":(20, 20),
                    "erode_iter":2,
                    "last": True
                })
                cv2.imshow("last_area", last_left_area)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        if debug:
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            pass

def binary_labeling(src):
    _, src_bin = cv2.threshold(src, 127, 255, cv2.THRESH_OTSU)
    cnt, labels, stats, centeroids = cv2.connectedComponentsWithStats(src_bin)
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for i in range(1, cnt):
        (x, y, w, h, area) = stats[i]

        if area < 1300:
            continue

        # print(x, y, w, h)
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_text_from_image_array(image_array, language="eng"):
    # # text more bold
    # image_array = cv2.GaussianBlur(image_array, (5, 5), 0)
    # kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # image_array = 255 - image_array
    # image_array = cv2.erode(image_array, kern, iterations=1)
    # image_array = cv2.dilate(image_array, kern, iterations=1)
    # image_array = 255 - image_array
    pytesseract.get_languages(config="--oem 3 --psm 6")
    print(pytesseract.image_to_string(image_array, lang=language, config = '--psm 6 --oem 3 -c tessedit_char_whitelist=-.0123456789ㅡ'))  # "eng+equ"
    cv2.imshow("image_array", image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_array


def split_textarea(image_area, image_path, option={"morph_pos":(150, 150), "erode_iter":3, "last":False}, save=True):
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (option["morph_pos"][0], option["morph_pos"][1]))
    erode = cv2.erode(image_area, vertical_kernel, iterations=option["erode_iter"])

    # contour를 찾으려면 흑백 전환을 시켜야한다. 그래서 흑백으로 변환한다.
    erode = 255 - erode

    # contour 찾기
    contours, hierarchy = cv2.findContours(
        erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    contours = contours[::-1]
    if option["last"]:
        contours = contours[1:-1]

    file_path = image_path.replace(JPG_DIR+"/", "")
    dir_path = "/".join(file_path.split("/")[:-1])
    # box 그리기
    for i, contour in enumerate(contours):
        global last_count
        x, y, w, h = cv2.boundingRect(contour)
        
        # debug
        # cv2.rectangle(image_area, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if option["last"]:
            rectarea = image_area[y : y + h, x : x + w]
            # cv2.rectangle(image_area, (x, y), (x + w, y + h), (0, 255, 0), 2)
            get_text_from_image_array(rectarea, "kor+eng")
        else:
            output_dir = path.join(OUTPUT_DIR ,dir_path)
            if not path.exists(output_dir):
                create_directory(output_dir)
            output_path = path.join(output_dir, f"{last_count}.jpg")
            print("output path >> ",output_path)
            cv2.imwrite(output_path, image_area[y:y+h, x:x+w])
            last_count += 1

    return image_area
