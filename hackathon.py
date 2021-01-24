import os
import glob
import cv2
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import math
images = [cv2.imread(file) for file in glob.glob("images/*.png")]
names = []
with os.scandir('images/') as entries:
    for entry in entries:
        names.append(entry.name)

a=images[0]
# for j in range(a.shape[0]):
#     for k in range(a.shape[1]):
#         for l in range(3):

#             if(a[a.shape[0]-1][a.shape[1]-1][l]==a[j][k][l]):
#                 a[j][k]=255
# imggplot = plt.imshow(a, vmin=0, vmax=255)
# plt.show()
# Reading the input image
img = a

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5,5), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
# img_erosion = cv2.erode(a, kernel, iterations=1)
img_dilation = cv2.dilate(a, kernel, iterations=1)

cv2.imshow('Input', a)
# cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
