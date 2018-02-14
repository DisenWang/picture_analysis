import cv2 
import numpy as np 
 
img = cv2.imread('/Users/disenwang/Github_stuff/picture_analysis/img/4191357.jpeg',) 
 
 
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


img2 = cv2.imread('/Users/disenwang/Github_stuff/picture_analysis/img/4195712.jpeg',) 
 
 
hsv2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)

output1=hsv.mean(axis=(0,1))



output2=hsv2.mean(axis=(0,1))



