from sub_capture_tool import SubCaptureTool
import numpy
import cv2
import time

time.sleep(3)
sct = SubCaptureTool()
j = 0
for i in range(60):
    time.sleep(1)
    for seg in sct.capture():
        gray = cv2.cvtColor(seg, cv2.COLOR_RGB2GRAY)
        gray, img_bin = cv2.threshold(gray,128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        gray = cv2.bitwise_not(img_bin)
        cv2.imwrite(f'imgs/{j}.jpg', gray)
        j += 1

cv2.imshow('done', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
