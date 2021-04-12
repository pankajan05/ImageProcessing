#!/usr/bin/env python
# coding: utf-8

# In[4]:


# No 1
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("saltandpepper2.png",1)

#no need dtype, just int is valid np.float32 
kernal = np.ones((5,5),dtype=int)/25 
dst = cv2.filter2D(img,-1,kernal)

result = np.hstack((img,dst))
cv2.imshow('Result', result)

cv2.waitKey(0)


# In[11]:


# No 1 - kernel not based on 1
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("saltandpepper2.png",1)

#no need dtype, just int is valid np.float32 
kernal1 = np.array([[1,2,1],
                  [2,4,2],
                  [1,2,1]])
kernal1 = kernal1/16
dst1 = cv2.filter2D(img,-1,kernal1)

#no need dtype, just int is valid np.float32 
kernal = np.ones((3,3),dtype=int)/9 
dst = cv2.filter2D(img,-1,kernal)

result = np.hstack((img,dst1,dst))
cv2.imshow('Result', result)

cv2.waitKey(0)


# In[16]:


# No 2
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("saltandpepper2.png",1)

dst_b = cv2.blur(img,(7,7)) #cv2.blur(img, kernel size)
dst_x = cv2.boxFilter(img,-1,(7,7)) #cv2.boxFilter(img,depth,size)

result = np.hstack((img,dst_b,dst_x))
cv2.imshow('Result', result)

cv2.waitKey(0)


# In[24]:


# No 3
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("saltandpepper1.png",1)

dst_m = cv2.medianBlur(img,3) #(img, kernel size)
dst_g = cv2.GaussianBlur(img,(11,11),0) #(img,size,standard deviation)

result = np.hstack((img,dst_m,dst_g))
cv2.imshow('Result', result)

cv2.waitKey(0)


# In[1]:


# No 4
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("hubble.png",1)

# custom kernel of 15x15 and apply to the input img
kernel = np.ones((15,15),np.float32) / 225

dst = cv2.filter2D(img,-1,kernel) #(img, kernel size)

# apply thresholding
ret,thresh = cv2.threshold(dst,120,255,cv2.THRESH_BINARY)

result = np.hstack((img,dst,thresh))
cv2.imshow('Result', result)

cv2.waitKey(0)


# In[ ]:




