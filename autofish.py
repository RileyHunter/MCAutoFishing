import pyautogui
from sub_capture_tool import SubCaptureTool
import time
import joblib
import numpy as np
import cv2

sct = SubCaptureTool()
time.sleep(5)
clf = joblib.load('model.joblib')

while True:
    time.sleep(0.2)
    for image in sct.capture():
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        gray = cv2.bitwise_not(img_bin)
        if gray.shape[0] == 39:
            app = np.zeros(gray.shape[1])
            gray = np.append(gray, [app], axis=0)
        features = np.concatenate(gray)
        pred = clf.predict([features])
        if pred == 'fishing_bobber_splashes':
            do_fishing()

def do_fishing():
    time.sleep(0.2)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(4)