#!/usr/bin/env python
# coding: utf-8

# In[5]:


# no 1
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("pyimg.jpg",0)

#find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])

#show the plotting graph of an img
plt.plot(histr)
plt.show()


# In[6]:


# no 2
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("pyimg.jpg",0)

#alternative way to find histogram of an img
#ravel -> convert multi dimention array into contiguos flat array 
hist,bins = np.histogram(img.ravel(), 256, [0,256])

#show the plotting graph of an img
plt.plot(hist)
plt.show()


# In[15]:


# no 3
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("pyimg.jpg",1)

color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])

#show the plotting graph of an img
plt.show()


# In[20]:


# no 4
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("pyimg.jpg",0)

#create mask
#opencv -> b,g,r
#matplot -> r,g,b
mask = np.zeros(img.shape[:2], np.uint8)
mask[50:400, 250:600] = 255
masked_img = cv2.bitwise_and(img,img,mask=mask)

#acculate histogram with mask and without mask
#check the third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

#ploting graph
plt.subplot(221), plt.imshow(img,'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img,'gray')
plt.subplot(224), plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()


# In[ ]:




