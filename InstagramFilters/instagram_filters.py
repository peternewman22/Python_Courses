import cv2
import numpy as np
from enum import Enum

class Const(Enum):
    AppName = 'instapp'

def dummy():
    pass

# create stuff
cv2.namedWindow(Const.AppName.value)
cv2.createTrackbar('contrast', Const.AppName.value, 1, 100, dummy)
cv2.createTrackbar('brighness', Const.AppName.value, 50, 100, dummy)
cv2.createTrackbar('filter', Const.AppName.value, 0, 1, dummy) # TODO: update to number of filters
cv2.createTrackbar('grayscale', Const.AppName.value, 0, 1, dummy)

# main loop
while True:
# TODO: read all the trackbar values
# TODO: apply filters
# TODO: apply brightness and contrast
# wait for keypress
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    
        
cv2.destroyAllWindows()