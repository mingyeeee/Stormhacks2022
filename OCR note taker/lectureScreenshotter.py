# import the necessary packages
from lib2to3.pygram import Symbols
import numpy as np
import pyautogui
import cv2
import time
import os
from equationidentifier import *

time.sleep(5)
count = 1
prevScreen = pyautogui.screenshot()
prevScreen = cv2.cvtColor(np.array(prevScreen), cv2.COLOR_RGB2BGR)

prevPixelCount = 0
while(True):
    # take screenshot
    curScreen = pyautogui.screenshot()
    curScreen = cv2.cvtColor(np.array(curScreen), cv2.COLOR_RGB2BGR)
    
    # compare the two screenshots and find the difference
    # convert the images to grayscale
    prevScreenGray = cv2.cvtColor(prevScreen, cv2.COLOR_BGR2GRAY)
    curScreenGray = cv2.cvtColor(curScreen, cv2.COLOR_BGR2GRAY)
    # subtract the images
    diff = cv2.absdiff(curScreenGray, prevScreenGray)

    # threshold the difference image
    ret, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    #count number of non-zero pixels
    currentPixelCount = cv2.countNonZero(thresh)
    print(currentPixelCount)
    # reset the previous screen with current screen
    prevScreen = curScreen

    # if the number of non-zero pixels increases by a factor of 10, then screen has changed
    if prevPixelCount*20 < currentPixelCount:
        print("Screen has changed")
        # save the screenshot
        cv2.imwrite("screenshot.png", curScreen)
        # run tesseract on the image
        cmd = "tesseract screenshot.png out"
        returned_value = os.system(cmd)
        # open the output file and read the text
        f = open("out.txt", "r", encoding="utf8")
        string_format = f.read()
        #print(string_format)
        #checking for equations
        query = initial_formatter(string_format)

        data_match = sampler("symbols.txt")

        if negative_nums(query) and symbol(query, data_match) == True:
            #SAVE SCREENSHOT
            print("saving screenshot")
            cv2.imwrite(f"{count}.png", curScreen)
            count += 1
    else:
        print("Screen has not changed")

    prevPixelCount = currentPixelCount
    time.sleep(3)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break