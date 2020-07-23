import pyautogui
import time
import numpy
from PIL import Image
import atexit
from pynput import mouse

screenWidth, screenHeight = pyautogui.size()

taskbarHeight = 40
windowHeight = 28

cursorX = (screenWidth / 2)
cursorY = (((screenHeight - (taskbarHeight + windowHeight)) / 2) + windowHeight) - 3
cursorDiameter = (screenHeight / 36) - 8 # ??

time.sleep(5)

ims = []
for i in range(10):
    time.sleep(0.2)
    ims.append(pyautogui.screenshot(region=(cursorX, cursorY - cursorDiameter, cursorDiameter, cursorDiameter)))

w,h=ims[0].size
N=len(ims)

arr=numpy.zeros((h,w,3),numpy.float)

for im in ims:
    imarr=numpy.array(im,dtype=numpy.float)
    arr=arr+imarr/N

arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)
avgColor = arr.mean(axis=0).mean(axis=0)
#avg=Image.fromarray(arr,mode="RGB")
#avg.show()

print("Ready!")

# events = 20
# def on_click(x, y, button, pressed):
#     global events 
#     events -= 1
#     if events <= 0:
#         listener.stop()
#     if pressed:
#         im = pyautogui.screenshot(region=(cursorX, cursorY - cursorDiameter, cursorDiameter, cursorDiameter))
#         arr=numpy.array(im,dtype=numpy.uint8)
#         avgSampleColor = arr.mean(axis=0).mean(axis=0)
#         print("===")
#         print(avgColor)
#         print(avgSampleColor)

# listener = mouse.Listener(
#     on_click=on_click)
# listener.start()

# while events > 0:
#     pass

while True:
    time.sleep(0.05)
    im = pyautogui.screenshot(region=(cursorX, cursorY - cursorDiameter, cursorDiameter, cursorDiameter))
    arr=numpy.array(im,dtype=numpy.uint8)
    avgSampleColor = arr.mean(axis=0).mean(axis=0)
    diffs = avgColor - avgSampleColor
    squares = numpy.square(diffs)
    sumSquaredDiff = numpy.sum(squares)
    if sumSquaredDiff > 1000:
        im = pyautogui.screenshot(region=(cursorX, cursorY - cursorDiameter, cursorDiameter, cursorDiameter))
        im.show()