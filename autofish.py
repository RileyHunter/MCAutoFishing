import pyautogui
from sub_capture_tool import SubCaptureTool
import time
import joblib
import numpy as np
import cv2

from fishing_config import *

sct = SubCaptureTool(override_resolution)
time.sleep(5)
clf = joblib.load('model.joblib')

def do_fishing():
    time.sleep(time_to_reel)
    pyautogui.click(button='right')
    time.sleep(time_to_recast)
    pyautogui.click(button='right')
    time.sleep(time_to_pause_sampling)

while True:
    time.sleep(0.2)
    for image in sct.capture():
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        gray = cv2.bitwise_not(img_bin)
        features = np.concatenate(gray)
        pred = clf.predict([features])
        if pred != 'garbage':
            print(pred)
        if pred == 'fishing_bobber_splashes':
            do_fishing()
