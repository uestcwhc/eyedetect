#病人A 双眼
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("liangxie.avi")
frame_count = 0
all_frames = []
axeye1 = []  
ayeye1 = []
axeye2 = []  
ayeye2 = []
#plt.axis([0,700,30,110])
plt.ion()
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)
#fig = plt.gcf()
#fig.set_size_inches(20, 20)
ax1_2 = ax1.twinx()
ax2_2 = ax2.twinx()
ax2.set_xticks([0,700,30,110])
ax2_2.set_yticks([0,700,30,110])


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

    for cnt in contours2: #右边眼
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
    axeye2.append(x2)
    ayeye2.append(y2)
    ax2.cla()
    ax2_2.cla()

       
    line4, = ax2_2.plot(all_frames, ayeye2,'red',label="right eye y axis")
    line3, = ax2.plot(all_frames, axeye2,label="right eye x axis")
    ax2.legend(handles=(line3,line4),loc='best')
    ax2_2.set(xlim=(0,2600),ylim=(35,110))
    ax2.set(xlim=(0,2600),ylim=(35,110))
    ax2.set_xlabel("time")
    ax2.set_ylabel("x position")
    #ax2_2.set_xlabel("time")
    ax2_2.set_ylabel("y position")
    plt.pause(0.001)
    plt.ioff()
    
    
    for cnt in contours1:   #左边眼
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
    axeye1.append(x1)
    ayeye1.append(y1)
    ax1.cla()
    ax1_2.cla()
    line2, = ax1_2.plot(all_frames, ayeye1,'red',label= "left eye y axis")
    line1, = ax1.plot(all_frames, axeye1,label="left eye x axis")
    ax1.legend(handles=(line1,line2),loc='best')
    #ax1.plot()
    ax1_2.set(xlim=(0,2600),ylim=(35,110))
    ax1.set(xlim=(0,2600),ylim=(35,110))
    #plt.ax1([0,700,30,110])
   # plt.ax1_2([0,700,30,110])
    ax1.set_xlabel("time")
    ax1.set_ylabel("x position")
    ax1_2.set_ylabel("y positon")

    plt.pause(0.001)
    plt.ioff()
    #all_frames.append(frame_count)
#     plt.clf()
#     plt.plot(all_frames, ax)
#     plt.plot(all_frames, ay)
#     plt.axis([0,700,30,110])
#     plt.pause(0.001)
#     plt.ioff()
    # for i in range(frame_count):
        
    
    if cv2.waitKey(30) & 0xff == ord('q'):
        break
   
    cv2.namedWindow("lefteye",0)
    cv2.namedWindow("righteye",0)
    cv2.imshow("lefteye", roi1)
    cv2.imshow("righteye", roi2)
   # cv2.imshow("Threshold", threshold2)
    #key = cv2.waitKey(30)
#for i in range(frame_count):
plt.savefig('figure.png')    
cap.release()
cv2.destroyAllWindows()