#!/usr/bin/env python
# coding: utf-8

# In[1]:Write your code to find the histogram of gray scale image and color image channels

import numpy as np
Gray_image = cv2.imread("image1.png")
Color_image = cv2.imread("image2.png")
grey=cv2.cvtColor(gray_image,cv2.COLOR_BGR2GRAY)
gray_hist = cv2.calcHist([grey],[0],None,[1100],[0,1100])
plt.figure()
plt.imshow(grey)
plt.show()
plt.title("Histogram")
plt.xlabel("Grayscale Value")
plt.ylabel("Pixel Count")
plt.stem(gray_hist)
plt.show()



# In[2]:Display the histogram of gray scale image and any one channel histogram from color image

import numpy as np
Gray_image = cv2.imread("image1.png")
Color_image = cv2.imread("image2.png")
grey=cv2.cvtColor(gray_image,cv2.COLOR_BGR2GRAY)
gray_hist = cv2.calcHist([grey],[0],None,[1100],[0,1100])
plt.figure()
plt.imshow(grey)
plt.show()
plt.title("Histogram")
plt.xlabel("Grayscale Value")
plt.ylabel("Pixel Count")
plt.stem(gray_hist)
plt.show()


# In[3]:Write the code to perform histogram equalization of the image. 



gray_image = cv2.imread("Exp-3 image.jpg")
grey=cv2.cvtColor(gray_image,cv2.COLOR_BGR2GRAY)
plt.imshow(grey)
plt.show()
equ = cv2.equalizeHist(grey)
plt.imshow(equ)
plt.show()
color_image=cv2.imread('image2.png')
grey=cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
plt.imshow(color_image)
plt.show()
eq = cv2.equalizeHist(grey)
plt.imshow(eq)
plt.show()









