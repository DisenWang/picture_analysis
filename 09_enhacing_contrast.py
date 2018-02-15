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
  
  
# Computer average HSV of each picture
i = 99
hsv_value = [[] for _ in range(i)]

# I used average HSV value of all pixels as the HSV value of the image
for k in range(0, len(onlyfiles)):
    hsv_value[k] = cv2.cvtColor(hsv[k],cv2.COLOR_BGR2HSV).mean(axis=(0,1))
    
    
x = numpy.vstack(hsv_value)

df = pd.DataFrame(x)
df.to_csv("/Users/disenwang/Github_stuff/picture_analysis/img_output.csv")