import cv2 

from os import listdir
from os.path import isfile, join
import numpy
import pandas as pd 


#read all images
mypath='/Users/disenwang/Github_stuff/picture_analysis/img'

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

images = numpy.empty(len(onlyfiles), dtype=object)

hsv = numpy.empty(len(onlyfiles), dtype=object)

for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
  # convert to HSV color space
  hsv[n] = cv2.cvtColor(images[n],cv2.COLOR_BGR2HSV)
  
  
# Compute average HSV of each picture
i = n+1
hsv_value = [[] for _ in range(i)]

# I used average HSV value of all pixels as the HSV value of the image
for k in range(0, len(onlyfiles)):
    hsv_value[k] = hsv[k].mean(axis=(0,1))
    
    
    
x = numpy.vstack(hsv_value)

df = pd.DataFrame(x)
df.to_csv("/Users/disenwang/Github_stuff/picture_analysis/img_output2.csv")



# Compute individual picture's hsv
img1 = cv2.imread("/Users/disenwang/Github_stuff/picture_analysis/img/148201.jpg")

hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV).mean(axis=(0,1))



# Read the name of images

name_hsv = list(zip(onlyfiles,hsv_value))

df2 = pd.DataFrame(name_hsv)
df2.to_csv("/Users/disenwang/Github_stuff/picture_analysis/img_output3.csv")


# Change the value of single image 
mage = cv2.imread('../images/test/image_1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

image[:,:,2] = 200 # Changes the V value

out = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imshow('image',out)
k = cv2.waitKey(0)
cv2.destroyAllWindows()