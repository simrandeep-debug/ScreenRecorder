
## import the required modules 

from cv2 import waitKey
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