import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

# loading and viewing the image
img = cv2.imread('C:Task_3.jpeg')
# cv2.imshow("original", img)

# creating boxes
box, label, count = cv.detect_common_objects(img)
output = draw_bbox(img, box, label, count)

output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 8))
plt.axis("off")
plt.imshow(output)
plt.show()

# print name and number of objects
print("number of objects in image are " + str(len(count)))
print(label)