
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

cv2.namedWindow("LiveRecording", cv2.WINDOW_NORMAL )
cv2.resizeWindow("LiveRecording", 500, 500)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()
  
    # Convert the screenshot to a numpy array
    frame = np.array(img)
  
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
    # Write it to the output file
    out.write(frame)
      
    # Optional: Display the recording screen
    cv2.imshow('Live', frame)
      
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
  
# Release the Video writer
out.release()
  
# Destroy all windows
cv2.destroyAllWindows()