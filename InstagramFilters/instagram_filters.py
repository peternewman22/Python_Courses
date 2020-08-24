import cv2
import numpy as np
from enum import Enum

class Const(Enum):
    AppName = 'instapp'
    Img = "test_image.jpg"
    trackbar_contrast = 'contrast'
    trackbar_brightness = 'brightness'
    trackbar_grayscale = 'grayscale'
    trackbar_filter = 'filter'


def dummy():
    pass

original_img = cv2.imread(Const.Img.value)
grayscale_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
# create stuff
cv2.namedWindow(Const.AppName.value)
cv2.createTrackbar(Const.trackbar_contrast.value, Const.AppName.value, 1, 100, dummy)
cv2.createTrackbar(Const.trackbar_brightness.value, Const.AppName.value, 50, 100, dummy)
cv2.createTrackbar(Const.trackbar_filter.value, Const.AppName.value, 0, 1, dummy) # TODO: update to number of filters
cv2.createTrackbar(Const.trackbar_grayscale.value, Const.AppName.value, 0, 1, dummy)

# main loop
while True:
# TODO: read all the trackbar values
    grayscale = cv2.getTrackbarPos(Const.trackbar_grayscale.value, Const.AppName.value)
# TODO: apply filters
# TODO: apply brightness and contrast
# wait for keypress
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    elif key == ord('s'):
        pass # TODO: implement save function

    # show image
    if grayscale == 0:
        cv2.imshow(Const.AppName.value, original_img)
    elif grayscale == 1:
        cv2.imshow(Const.AppName.value, grayscale_img)
    
        
cv2.destroyAllWindows()