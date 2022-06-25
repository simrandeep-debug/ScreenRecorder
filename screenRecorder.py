
## import the required modules 

import cv2
import numpy as np
import pyautogui

## create a video writer object which contains 4 parameters :
## filename, codec, fps and resolution .
  
filename = "ScreenRecording.avi"
codec = cv2.VideoWriter_fourcc(*"XVID")
fps = 60.0
resolution = (1920, 1080)

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)