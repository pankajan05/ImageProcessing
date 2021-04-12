#!/usr/bin/env python
# coding: utf-8

# In[8]:


# No 1
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pyimg.jpg',0)

#create histogram
hist1 = cv2.calcHist([img],[0],None,[256],[0,256])

#create histogram equalization
eqlImage = cv2.equalizeHist(img)
hist2 = cv2.calcHist([eqlImage],[0],None,[256],[0,256])

#plot
plt.subplot(121),plt.plot(hist1)
plt.subplot(122),plt.plot(hist2)

result = np.hstack((img,eqlImage))
cv2.imshow('Result', result)

cv2.waitKey()
cv2.destroyAllWindows()


# In[6]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pybrg.jpg',0)

#create histogram
hist1 = cv2.calcHist([img],[0],None,[256],[0,256])

#create histogram equalization
eqlImage = cv2.equalizeHist(img)
hist2 = cv2.calcHist([eqlImage],[0],None,[256],[0,256])

#plot
plt.subplot(221),plt.plot(hist1)
plt.subplot(222),plt.plot(hist2)

result = np.hstack((img,eqlImage))
cv2.imshow('Result', result)

cv2.waitKey()
cv2.destroyAllWindows()


# In[7]:


# No 3 
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_d = cv2.imread('pyimg.jpg',0)
img_b = cv2.imread('pybrg.jpg',0)

#create histogram
hist1 = cv2.calcHist([img_d],[0],None,[256],[0,256])
hist2 = cv2.calcHist([img_b],[0],None,[256],[0,256])

#create histogram equalization
eqlImage1 = cv2.equalizeHist(img_d)
eqlImage2 = cv2.equalizeHist(img_b)

hist3 = cv2.calcHist([eqlImage1],[0],None,[256],[0,256])
hist4 = cv2.calcHist([eqlImage2],[0],None,[256],[0,256])

#plot
plt.subplot(221),plt.plot(hist1)
plt.subplot(222),plt.plot(hist2)
plt.subplot(223),plt.plot(hist3)
plt.subplot(224),plt.plot(hist4)

plt.xlim([0,256])

result = np.hstack((img_d,eqlImage1))
cv2.imshow('Result Dark', result)

result = np.hstack((img_b,eqlImage2))
cv2.imshow('Result Bright', result)

cv2.waitKey()
cv2.destroyAllWindows()


# In[3]:


# No 4
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('colimg.jpg',1)

# convert image from RGB to HSV
# V <- value
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#create histogram equalization on V-channel
img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:, :, 2])

#Convert img HSV to RGB
img2 = cv2.cvtColor(img_hsv,cv2.COLOR_HSV2RGB) 


hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

#plot
plt.subplot(221),plt.plot(hist1)
plt.subplot(222),plt.plot(hist2)

result = np.hstack((img,img2))
cv2.imshow('Result', result)

cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




