
#load img

import cv2
#imread -> second parameter option
#1 - normal => cv2.IMREAD_COLOR
#0 - gray scale => cv2.IMREAD_GRAYSCALE
#-1 - unchanged => cv2.IMREAD_UNCHANGED
img = cv2.imread('E:/Files/SLIIT/LECTURE/YEAR 4/SEM 1/IUP/Lec 1/pyimg.jpg',0)
cv2.imshow('Input Window', img)
cv2.waitKey()
cv2.destroyAllWindows()


#--------------------------------------------------


#save image

import cv2
img = cv2.imread('E:/Files/SLIIT/LECTURE/YEAR 4/SEM 1/IUP/Lec 1/pyimg.jpg',0)
cv2.imshow('Input Window', img)
status = cv2.imwrite('E:/Files/SLIIT/LECTURE/YEAR 4/SEM 1/IUP/Lec 1/changed.jpg',img)
print("Image Successfully Saved ?", status)
cv2.waitKey()
cv2.destroyAllWindows()


#-------------------------------------------------


#access pixel value
#if u have coloured img return BGR else one pixel value

import cv2
img = cv2.imread('E:/Files/SLIIT/LECTURE/YEAR 4/SEM 1/IUP/Lec 1/pyimg.jpg',1)
px = img[50, 100] #img(x,y)
print(px) #B,G,R or Just Value
cv2.imshow('Input Window', img)
cv2.waitKey()
cv2.destroyAllWindows()


#-----------------------------------------------------


#access pixel value

import cv2
img = cv2.imread('E:/Files/SLIIT/LECTURE/YEAR 4/SEM 1/IUP/Lec 1/pyimg.jpg',1)
px = img[50, 100] #img(x,y)
print(px)
img[50,100] = [240, 222, 111] #if grayscale just value -> img[50,100] = 100
px = img[50, 100]
print(px) # print(img[50, 100])
cv2.imshow('Input Window', img)
cv2.waitKey()
cv2.destroyAllWindows()


#-----------------------------------------------------


#properties

import cv2
img = cv2.imread('E:/Files/SLIIT/LECTURE/YEAR 4/SEM 1/IUP/Lec 1/pyimg.jpg',1)
print(img.shape) #size (h,w,number of color channel if b&w single hannel)
print(img.size)
print(img.dtype)
cv2.imshow('Input Window', img)
cv2.waitKey()
cv2.destroyAllWindows()


#-------------------------------------------------------


#convert to gray scale

import cv2

#color
img = cv2.imread('E:/Files/SLIIT/LECTURE/YEAR 4/SEM 1/IUP/Lec 1/pyimg.jpg',1)
cv2.imshow('Input Window', img)

#grayscale
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Output Window', img_g)

#binary
res,binary = cv2.threshold(img_g, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Window', binary)

cv2.waitKey()
cv2.destroyAllWindows()





