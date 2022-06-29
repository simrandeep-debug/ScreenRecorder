
## import the required modules 

import numpy
import cv2 
import pyautogui

# display screen resolution, get it using pyautogui itself
sizeOfScreen = tuple(pyautogui.size())

# define the codec
# to encode/decode a data stream / media 
codec = cv2.VideoWriter_fourcc(*"XVID")

# frames per second, this value can be experimented 
framesPerSecond = 12.0

# create the video write object
out = cv2.VideoWriter("recording_Output.avi", codec, framesPerSecond, (sizeOfScreen))

##########################################################

##### continue taking screenshot using pyautogui and convert that into an array 
##### Print the array / Show the output 
while (True):

    currentScreen = pyautogui.screenshot() # Take a screenshot

    frameData = numpy.array(currentScreen) # convert the screen snippet to a numpy array