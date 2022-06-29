
## import the required modules 

import numpy
import cv2 
import pyautogui
from cv2 import waitKey

# display screen resolution, get it using pyautogui itself
# pyautogui.size() will return resolution depending upon screen's resolution.

sizeOfScreen = tuple(pyautogui.size())

# define the codec using VideoWriter.
# FOURCC is a 4-byte code used to specify the video codec. More codecs can be found at FOURCC web page 
# depending upon the need and requirement 

codec = cv2.VideoWriter_fourcc(*"XVID")

# frames per second, this value can be experimented 
framesPerSecond = 5

# create the video write object
out = cv2.VideoWriter("recording_Output.avi", codec, framesPerSecond, (sizeOfScreen))

##########################################################

##### continue taking screenshot using pyautogui and convert that into an array 
##### Print the array / Show the output 
while (True):

    currentScreen = pyautogui.screenshot() # Take a screenshot

    frameData = numpy.array(currentScreen) # convert the screen snippet to a numpy array

    # by default, color schema is BGR, it is important to conver that to RGB schema 
    frameData = cv2.cvtColor(frameData, cv2.COLOR_BGR2RGB)

    out.write(frameData)

    # show the frame
    cv2.imshow("screenshot", frameData)
    # if the user clicks q, it exits
    if (cv2.waitKey(1) == ord("q") or cv2.waitKey(1) == ord('Q') ):
        out.write("q or Q pressed, halt the execution")
        break


##### to avoid unnecessary memory utilisation 
##### it is important to kill the object and release the memory (Video Writer object)

out.release()
cv2.destroyAllWindows() ## to destroy the GUI windows 