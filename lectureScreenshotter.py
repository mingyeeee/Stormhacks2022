# import the necessary packages
import numpy as np
import pyautogui
import cv2
import time

prevScreen = pyautogui.screenshot()
prevScreen = cv2.cvtColor(np.array(prevScreen), cv2.COLOR_RGB2BGR)
while(True):
    curScreen = pyautogui.screenshot()
    curScreen = cv2.cvtColor(np.array(curScreen), cv2.COLOR_RGB2BGR)
    # convert the images to grayscale
    prevScreenGray = cv2.cvtColor(prevScreen, cv2.COLOR_BGR2GRAY)
    curScreenGray = cv2.cvtColor(curScreen, cv2.COLOR_BGR2GRAY)
    # subtract the images
    diff = cv2.absdiff(curScreenGray, prevScreenGray)

    # threshold the difference image
    ret, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    #count number of non-zero pixels
    num_pixels = cv2.countNonZero(thresh)
    print(num_pixels)
    prevScreen = curScreen
    time.sleep(3)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break