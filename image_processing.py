# -*- coding: utf-8 -*-
# importing libraries
import cv2
import numpy as np

# reading in image
image_path = './img/puppies.jpeg'
img = cv2.imread(image_path)

# check we have read in the image correctly
if img is not None:
    print ('Image Read Successfully!')
else:
    print ('Error Reading Image')
    
# resizing for screen
img = cv2.resize(img, (960, 540))
    
# displaying image
cv2.imshow('Cute Puppies', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# saving image to file
cv2.imwrite('./img/puppies_gray.jpeg', img_gray)