import cv2
import numpy
import win32gui
import pyautogui
import time

from fishing_config import *

class SubCaptureTool:
    def __init__(self, override_pos=False):
        self.override_pos = override_pos
        # Config parsing
        # From bottom right - left, up; max width, line height.
        known_sizes = {
            4: (5, 98, 567, 40)
        }

        if gui_scale in known_sizes:
            self.relative_sub_area = known_sizes[gui_scale]
        else:
            raise("Yeet")

        self.mc_hwnd = None
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                window_text = win32gui.GetWindowText(hwnd)
                if "Minecraft" in window_text:
                    self.mc_hwnd = hwnd

        win32gui.EnumWindows( winEnumHandler, None )

        if self.mc_hwnd is None:
            raise("No MC window found")

        rect = win32gui.GetWindowRect(self.mc_hwnd)
        x1 = rect[0]
        y1 = rect[1]
        x2 = rect[2]
        y2 = rect[3]

        # If in weird-screen mode
        if (x1 == -8 and y1 == -8):
            x2 += x1
            y2 += y1
            x1 = 0
            y1 = 0
        if self.override_pos:
            x1 = 0
            y1 = 0
            x2 = 1920
            y2 = 1040
        print("Window %s:" % win32gui.GetWindowText(self.mc_hwnd))
        print("\tLocation top left: (%d, %d)" % (x1, y1))
        print("\tLocation bot right: (%d, %d)" % (x2, y2))

        self.segments_to_sample = 5
        self.bottom_right_x = x2 - self.relative_sub_area[0]
        self.bottom_right_y = y2 - self.relative_sub_area[1]
        self.top_left_x = self.bottom_right_x - self.relative_sub_area[2]
        self.top_left_y = self.bottom_right_y - (self.segments_to_sample * self.relative_sub_area[3])

    def capture(self):
        img = pyautogui.screenshot(region=(
        self.top_left_x, self.top_left_y, self.bottom_right_x - self.top_left_x, self.bottom_right_y - self.top_left_y
        ))
        imarr = numpy.array(img)
        segs = []
        for i in range(self.segments_to_sample):
            segs.append(imarr[-(((i + 1) * self.relative_sub_area[3]) + 1):-((i * self.relative_sub_area[3]) + 1), :])
        return segs
