import os
import cv2
import numpy as np
import pytesseract
from PIL import Image
from constants import JPG_DIR
from random import randint


def split_area(image_path_list, minLineLength=5000, maxLineGap=1000, margin=10):
    image_path_list.sort()
    for image_index, image_path in enumerate(image_path_list):
        image = cv2.imread(image_path)
        '''
        # 복사용지를 스캔하여 사용하는경우 블러처리하여 노이즈 제거
        # blur = cv2.bilateralFilter(image, 10, 75, 75)
        # gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        '''
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
            for x
            in cv2.HoughLinesP(edges, 1, 3*np.pi / 360, 100, minLineLength, maxLineGap)
        ]
        lines.sort(key=lambda lines: sum(lines[0]))
        del lines[1::2]

        # # Debug
        # for i, line in enumerate(lines):
        #     print(i, lines[i])
        #     for x1, y1, x2, y2 in line:
        #         cv2.putText(image, str(i), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), 12)
        #         cv2.line(image, (x1, y1), (x2, y2), (0,255,0), 3)

        if image_index == 0:
            print("맨 앞장")
            title = image[0:lines[0][0][3]-margin, 0:lines[0][0][2]]
            school = image[lines[0][0][3]+margin*2:lines[1][0][3]-margin, lines[1][0][0]:lines[1][0][2]]
            content_left = gray[lines[1][0][3]+margin:lines[3][0][3]-margin, 0+margin:lines[2][0][0]-margin]
            content_right = gray[lines[1][0][3]+margin:lines[3][0][3]-margin, lines[2][0][0]+margin:]

            content_left = split_textarea(content_left)
            content_right = split_textarea(content_right)
            
            cv2.imshow('content_left', content_left)
            cv2.imshow('content_right', content_right)
            get_text_from_image_array(title)
            get_text_from_image_array(school)

        elif image_index < len(image_path_list) - 1:
            print("내용있는 장")
            content_left = image[lines[0][0][3]:lines[2][0][3], 0:lines[1][0][0]]
            content_right = image[lines[0][0][3]:lines[2][0][3], lines[1][0][0]:]
            content_left = split_textarea(content_left)
            content_right = split_textarea(content_right)
            cv2.imshow('content_left', content_left)
            cv2.imshow('content_right', content_right)
        else:
            print("맨 뒤장")
            # cv2.imshow('content_left', image[lines[0][0][3]:lines[2][0][3], 0:lines[1][0][0]])
            # get_text_from_image_array(image, "kor+eng+equ")
            image = split_textarea(image)
            cv2.imshow('paper', image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

def binary_labeling(src):
    _,  src_bin = cv2.threshold(src, 127, 255, cv2.THRESH_OTSU)
    cnt, labels, stats, centeroids = cv2.connectedComponentsWithStats(src_bin)
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for i in range(1, cnt):
        (x, y, w, h, area) = stats[i]

        if area < 1300:
            continue

        # print(x, y, w, h)
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_text_from_image_array(image_array, language="kor+eng+equ"):
    blur = cv2.bilateralFilter(image_array, 10, 75, 75)
    image_array = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    pytesseract.get_languages(config="--oem 3 --psm 6")
    print(pytesseract.image_to_string(
        image_array,
        lang=language # "eng+equ"
    ))

def split_textarea(image_area):
    # Find the contours
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (250,250))
    erode = cv2.erode(image_area, vertical_kernel, iterations=4)
    # cv2.imshow('erode', erode)
    contours, _ = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[::-1]
    # heiarachy = heiarachy[0][::-1]
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        # cv2.rectangle(image_area, (x, y), (x + w, y + h), (0, 0, 255), 3)
        # rect = cv2.minAreaRect(contour)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # cv2.drawContours(image_area, [box], 0, (0, 0, 255), 2)
        cv2.putText(image_area, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), 12)
    return image_area
