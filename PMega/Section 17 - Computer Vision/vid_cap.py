import cv2
import time
from datetime import datetime
import pandas


video = cv2.VideoCapture(0)  # there's only one webcam, so 1

first_frame = None # we'll store the numpy arroy here
#a = 0

status_list = [None,None]
times = []
df = pandas.DataFrame(columns=["Start","End"])
while True:
    #a += 1
    check, frame = video.read()  # check = is the camera on? frame = captures video
    status = 0 #no motion in current Frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21),0) #removes noise and increases accuracy of difference

    if first_frame is None:
        first_frame = gray
        continue

    """Calculating the delta/distance frame"""
    delta_frame = cv2.absdiff(first_frame,gray)
    # print(check)
    # print(frame)

    """ Now we set some thresholds"""
    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]

    """ Smoothing threshold Frame"""
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) #bigger = smoother
    # time.sleep(3)

    """ Detecting Contours"""
    (_,cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2]==1:
        times.append(datetime.now())
    """ Showing windows"""
    cv2.imshow("Capturing", frame)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Colour Frame",frame )
    # gs_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)




    key = cv2.waitKey(1)

    if key == ord('q'):
        break
        if status == 1:
            times.append(datetime.now())
print(status_list)
print(times)

for i in range(0,len(times),2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

#print(a)
video.release()  # stop filming
cv2.destroyAllWindows
