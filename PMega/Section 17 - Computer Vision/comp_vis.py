import cv2
import os

img = cv2.imread("galaxy.jpg",1) # note: 0 = greyscale, -1 = transparent

"""print(type(img))
print(img)
print(img.shape)
print(img.ndim)

#resized_img = cv2.resize(img,(1000,500))
resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_resized.jpg", resized_img)
cv2.waitKey(2000) #ms
cv2.destroyAllWindows() """
