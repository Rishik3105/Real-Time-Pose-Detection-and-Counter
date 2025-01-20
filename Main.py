import cv2 as cv
import time
import numpy as np
import Pose_module as pm

cap=cv.VideoCapture(0)
wcam=1000
hcam=500
cap.set(3,wcam)
cap.set(4,hcam)
count=0 # used to count 
dir=0 # when hand is going up direction will be zero
       # when the hand is going down the direction will be one 
detector=pm.poseDetector()
while True:
    success,img=cap.read()
    #cv.resize(1280,720)
    img=detector.findPose(img,False) # gives only those points that are given in findAngle() function
    lmlist=detector.findPosition(img,False)
    if len(lmlist)!=0:
        angle=detector.findAngle(img,12,14,16) # for right arm
        #detector.findAngle(img,11,13,15) # for left arm 
        #change the landmark points to get the angle between the points 
        per=np.interp(angle,(160,35),(0,100))
    if per==100:
        if dir==0:
            count+=0.5
            dir=1
    if per ==0:
        if dir ==1:
            count+=0.5
            dir==0
    cv.putText(img,str(int(per)),(10,70),3,cv.FONT_HERSHEY_PLAIN,(255,0,255),3)
    cv.putText(img,str(f'c:{int(count)}'),(30,100),3,cv.FONT_HERSHEY_PLAIN,(255,0,255),3)
    cv.imshow("Image",img)
    if cv.waitKey(1) & 0XFF==ord('q'):
        break
