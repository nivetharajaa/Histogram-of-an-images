# Histogram-of-an-images
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Read the gray and color image using imread()

### Step2:
Print the image using imshow().



### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### step4:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step5:
The Histogram of gray scale image and color image is shown.


## Program:

# Developed By: Nivetha A
# Register Number: 212222230101

### Input Grayscale Image and Color Image
```
import cv2
import matplotlib.pyplot as plt
gray_image=cv2.imread('image1.png')
grey=cv2.cvtColor(gray_image,cv2.COLOR_BGR2GRAY)
plt.imshow(grey)
plt.axis('on')
plt.show()
```
![image](https://github.com/user-attachments/assets/3927585e-5685-40e6-8c98-923f11fdb865)

```
color_image=cv2.imread('image2.png')
plt.imshow(color_image)
plt.axis('on')
plt.show()
```
![image](https://github.com/user-attachments/assets/e002bbfa-2b25-49d5-bb54-822d4b7cac86)

### Histogram of Grayscale Image and any channel of Color Image
```
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
```
![image](https://github.com/user-attachments/assets/17bf9b15-02de-4bba-b51d-b27965b083ca)

![image](https://github.com/user-attachments/assets/a17981af-edd5-41e1-9a82-94c433fbfc1b)

```
color_hist = cv2.calcHist([Color_image],[0],None,[2600],[0,2600])
plt.figure() 
plt.imshow(color_image)
plt.show()
plt.title("Histogram")
plt.xlabel("Grayscale Value")
plt.ylabel("Pixel Count")
plt.stem(color_hist)
plt.show()
```
![image](https://github.com/user-attachments/assets/35dfd15d-c703-4184-aa2f-c32b35217b77)

![image](https://github.com/user-attachments/assets/83c8543e-9c6d-4c40-82dc-424fc6d28d8f)

### Histogram Equalization of Grayscale Image.
```
gray_image = cv2.imread("Exp-3 image.jpg")
grey=cv2.cvtColor(gray_image,cv2.COLOR_BGR2GRAY)
plt.imshow(grey)
plt.show()
```
![image](https://github.com/user-attachments/assets/fd87491b-9a39-474f-b5c0-b252d0cd4133)
```
equ = cv2.equalizeHist(grey)
plt.imshow(equ)
plt.show()
```
![image](https://github.com/user-attachments/assets/118f842a-21ac-4ad0-ac0b-bbd1282062ee)
```
color_image=cv2.imread('image2.png')
grey=cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
plt.imshow(color_image)
plt.show()
```
![image](https://github.com/user-attachments/assets/0776275c-5dfd-4330-ab21-cc720d052247)
```
eq = cv2.equalizeHist(grey)
plt.imshow(eq)
plt.show()
```
![image](https://github.com/user-attachments/assets/f5185aff-a4de-4fe1-a980-e61998002080)



## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
