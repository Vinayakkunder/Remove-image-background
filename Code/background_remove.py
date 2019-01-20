# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:38:58 2019

@author: DarkArmy
"""

import cv2
import numpy as np
 
img = cv2.imread('IMG_20190106_170921.jpg')

#converting image into its hsv form
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#selecting the color range to be extracted
lower_green = np.array([10, 0, 60])        #lowest range
upper_green = np.array([92, 255, 255])     #highest range

#creating mask for image segmentation 
mask = cv2.inRange(hsv, lower_green, upper_green)

#extracting the foreground from the image
fg = cv2.bitwise_and(img, img, mask=mask)

#saving the extracted image
cv2.imwrite('fg1.jpg',fg)   #Foreground image