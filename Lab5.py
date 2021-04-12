#!/usr/bin/env python
# coding: utf-8

# In[8]:


# No 1
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_raw = cv2.imread('apples.jpg', 1) #bgr
img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB) #rgb

img_neg = cv2.bitwise_not(img)

plt.imshow(img)
plt.show()

plt.imshow(img_neg)
plt.show()


# In[18]:


# No 2
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gamma.jpg', 0)
gamma = 0.6

img_2 = np.power(img,gamma)

plt.imshow(img, cmap='gray')
plt.show()

plt.imshow(img_2, cmap='gray')
plt.show()


# In[23]:


# No 3
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gamma.jpg', 0)
gamma = 1.2

img_2 = np.power(img,gamma)

plt.imshow(img, cmap='gray')
plt.show()

plt.imshow(img_2, cmap='gray')
plt.show()


# In[32]:


# No 4
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('log.jpg', 0)

# Apply log trans method
c = 255/np.log(1+np.max(img))
log_img = c*(np.log(img+1))

# specify data type
# float converted to int
log_img = np.array(log_img, dtype = np.uint8)

plt.imshow(img, cmap='gray')
plt.show()

plt.imshow(log_img, cmap='gray')
plt.show()


# In[ ]:




