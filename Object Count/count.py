#First we need to import our dependencies:
import cv2
import numpy as np

#read our image:
img = cv2.imread('C:/Users/sejal/python/MiniProject/Coins.jpg')

#then we will be converting it into grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#after that, we doing thresholding on image
_, thresh = cv2.threshold(img, 225, 255, cv2.THRESH_BINARY_INV)
kernal = np.ones((2, 2), np.uint8)

#then we are doing dilation process, removing black distortion:
dilation = cv2.dilate(thresh, kernal, iterations=2)

#next step is finding contour shapes:
contours, hierarchy = cv2.findContours(
    dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Then we are getting number of contours (objects found):
objects = str(len(contours))

#We can now print number of objects on an image
text = "Obj:"+str(objects)
cv2.putText(dilation, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
            0.4, (240, 0, 159), 1)

#For the lasr step we can show, original, threshold and dilation image:
cv2.imshow('Original', img)
cv2.imshow('Thresh', thresh)
cv2.imshow('Dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()           