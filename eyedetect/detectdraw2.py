#病人A 双眼     #备份618上午心电图样式，x，y显示在一张图中，只画了一只眼睛的统计图
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("liangxie.avi")
frame_count = 0
all_frames = []
ax = []  
ay = []  
plt.ion()
while (True):
    ret, frame = cap.read()
    #print(frame.shape)
    if ret is False:
        break
    frame_count = frame_count + 1
    all_frames.append(frame_count)
   # print (frame_count)
    roi1 = frame[0: 120, 0:160]
    gray_roi1 = roi1[:,:,0]
    gray_roi1 = cv2.GaussianBlur(gray_roi1, (7, 7), 0)
    _,threshold1 = cv2.threshold(gray_roi1, 30, 255, cv2.THRESH_BINARY_INV)
    contours1, _ = cv2.findContours(threshold1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours1 = sorted(contours1, key=lambda x: cv2.contourArea(x), reverse=True)

    
    
    
    roi2 = frame[0: 120, 160:320]
  #  cv2.imshow("show",roi)
    
    rows, cols, _ = roi2.shape
    #gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
   
    gray_roi2 = roi2[:,:,0]
    gray_roi2 = cv2.GaussianBlur(gray_roi2, (7, 7), 0)
   # cv2.imshow("gray_roi",gray_roi)

    _,threshold2 = cv2.threshold(gray_roi2, 30, 255, cv2.THRESH_BINARY_INV)
    contours2, _ = cv2.findContours(threshold2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2 = sorted(contours2, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours2:   #右边眼
        (x, y, w, h) = cv2.boundingRect(cnt)

        #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi2, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi2, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi2, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        #print("x=",x+w/2)
        #print("y=",y+h/2)
        x2=x+w/2
        y2=y+h/2
        font = cv2.FONT_HERSHEY_SIMPLEX
        roi2 = cv2.putText(roi2,"X="+str(x2),(10, 15),font , 0.5, (255, 255, 255), 1)
        roi2 = cv2.putText(roi2,"Y="+str(y2),(10, 30),font , 0.5, (255, 255, 255), 1)
        break
 
    for cnt in contours1:  #左边眼
        (x, y, w, h) = cv2.boundingRect(cnt)

        #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi1, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi1, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi1, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        #print("x=",x+w/2)
        #print("y=",y+h/2)
        x1=x+w/2
        y1=y+h/2
        font = cv2.FONT_HERSHEY_SIMPLEX
        roi1 = cv2.putText(roi1,"X="+str(x1),(10, 15),font , 0.5, (255, 255, 255), 1)
        roi1 = cv2.putText(roi1,"Y="+str(y1),(10, 30),font , 0.5, (255, 255, 255), 1)
        break 

    ax.append(x1)
    ay.append(y1)
   # all_frames.append(frame_count)
   
    plt.clf()
    plt.plot(all_frames, ax)
    plt.plot(all_frames, ay)
    plt.axis([0,700,30,110])
    plt.pause(0.01)
    plt.ioff()

    if cv2.waitKey(20) & 0xff == ord('q'):
        break
   
    cv2.namedWindow("lefteye",0)
    cv2.namedWindow("righteye",0)
    cv2.imshow("lefteye", roi1)
    cv2.imshow("righteye", roi2)
   # cv2.imshow("Threshold", threshold2)
    #key = cv2.waitKey(30)
#for i in range(frame_count):
    
cap.release()
cv2.destroyAllWindows()