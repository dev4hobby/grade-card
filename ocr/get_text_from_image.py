import os
from PIL import Image
from constants import JPG_DIR
import cv2
import numpy as np
from random import randint
import pytesseract

pytesseract.get_languages(config="--oem 6 --psm 6")
image = cv2.imread(os.path.join(JPG_DIR, "1/0.jpg"))
# blur = cv2.bilateralFilter(image, 10, 75, 75)
# gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 200, apertureSize=3)

minLineLength= 1200
maxLineGap = 500

lines = [
    x.tolist()
    for x
    in cv2.HoughLinesP(edges, 1, 3*np.pi / 360, 100, minLineLength, maxLineGap)
]
lines.sort(key=lambda lines: sum(lines[0]))
del lines[1::2]

for i, line in enumerate(lines):
    # print(i, lines[i]) # for debug
    for x1, y1, x2, y2 in line:
        cv2.putText(image, str(i), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), 12)
        cv2.line(image, (x1, y1), (x2, y2), (0,255,0), 3)

cv2.imshow('paper', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# binary grouping
# _,  src_bin = cv2.threshold(src, 127, 255, cv2.THRESH_OTSU)
# cnt, labels, stats, centeroids = cv2.connectedComponentsWithStats(src_bin)
# dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# for i in range(1, cnt):
#     (x, y, w, h, area) = stats[i]

#     if area < 1300:
#         continue

#     print(x, y, w, h)
#     cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 2)

# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# print(pytesseract.image_to_string(
#     threshold_image,
#     lang="kor+env"
# ))

