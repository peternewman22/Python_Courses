import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# search from greyscale images
img = cv2.imread("photo.jpg")
gs_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gs_img,
scaleFactor=1.05,
minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3) # colour is RGB and last parameter is pixel width of rectangle

print(type(faces))
print(faces)

cv2.imshow("Gray",gs_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
