#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


#capture the video
cap = cv2.VideoCapture("pyvideo.mp4")


# In[3]:


while(cap.isOpened()):
    ret,frame = cap.read()
    
    #convert color rgb to hsv
    hsv = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    
    #define lower blue and upper blue
    lower_blue = np.array([50,50,110]) #lower blue
    upper_blue = np.array([255,255,130]) #upper blue
    
    #threshold the HSV img to get only the blue
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    
    res = cv2.bitwise_and(frame,frame,mask = mask)
    
    #create 3 sepperate window for the original video, binary video and result video
    
    org = cv2.resize(frame,(500,500))
    cv2.imshow("Original", org)
    
    mask_V = cv2.resize(mask,(500,500))
    cv2.imshow("Binary", mask_V)
    
    result = cv2.resize(res,(500,500))
    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
        

cap.release()
cv2.destroyAllWindows()


# In[ ]:




