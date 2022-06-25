
## import the required modules 

import cv2
import numpy as np
import pyautogui

## create a video writer object which contains 4 parameters :
## filename, codec, fps and resolution .
  
# Specify name of Output file
filename = "ScreenRecording.avi"
  
# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 60.0
  
# Specify resolution
resolution = (1920, 1080)

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)