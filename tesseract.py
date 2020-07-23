import cv2
import numpy
import win32gui
import pyautogui
import time

from fishing_config import *

# Config parsing
# From bottom right - left, up; max width, line height.
known_sizes = {
    4: (5, 98, 567, 40)
}

if gui_scale in known_sizes:
    relative_sub_area = known_sizes[gui_scale]
else:
    raise("Yeet")

mc_hwnd = None
def winEnumHandler(hwnd, ctx):
    global mc_hwnd
    if win32gui.IsWindowVisible(hwnd):
        if "Minecraft 1." in win32gui.GetWindowText(hwnd):
            mc_hwnd = hwnd

win32gui.EnumWindows( winEnumHandler, None )

if mc_hwnd is None:
    raise("No MC window found")

rect = win32gui.GetWindowRect(mc_hwnd)
x1 = rect[0]
y1 = rect[1]
x2 = rect[2]
y2 = rect[3]

# If in weird-screen mode
if x1 == -8 and y1 == -8:
    x2 += x1
    y2 += y1
    x1 = 0
    y1 = 0
print("Window %s:" % win32gui.GetWindowText(mc_hwnd))
print("\tLocation top left: (%d, %d)" % (x1, y1))
print("\tLocation bot right: (%d, %d)" % (x2, y2))

segments_to_sample = 5
bottom_right_x = x2 - relative_sub_area[0]
bottom_right_y = y2 - relative_sub_area[1]
top_left_x = bottom_right_x - relative_sub_area[2]
top_left_y = bottom_right_y - (segments_to_sample * relative_sub_area[3])

time.sleep(3)

j = 0
for i in range(100):
    img = pyautogui.screenshot(region=(top_left_x, top_left_y, bottom_right_x - top_left_x, bottom_right_y - top_left_y))
    imarr = numpy.array(img)
    segs = []
    time.sleep(1)
    for i in range(segments_to_sample):
        segs.append(imarr[-(((i+1) * relative_sub_area[3]) + 1):-((i * relative_sub_area[3]) + 1), :])

    for seg in segs:
        gray = cv2.cvtColor(seg, cv2.COLOR_RGB2GRAY)
        gray, img_bin = cv2.threshold(gray,128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        gray = cv2.bitwise_not(img_bin)
        cv2.imwrite(f'imgs/{j}.jpg', gray)
        j += 1

cv2.imshow('done', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()