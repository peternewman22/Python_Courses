import os
import cv2

# get list of files:
# print(os.listdir())
file_list = os.listdir()

image_list = []
# now making my actual file list
for x in file_list:
    if x[-3:] == "jpg":
        image_list.append(x)

# print(image_list)
def batch_resize(img_list):
    for x in img_list:
        img = cv2.imread(x,1)
        resized_img = cv2.resize(img,(100,100))
        cv2.imwrite("{}_batchresized.jpg".format(x[:-4],), resized_img)

batch_resize(image_list)
