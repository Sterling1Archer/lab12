import numpy as np
import cv2 as cv
import sys

img1 = cv.imread('temple.jpeg') # load the first image into img1 variable
img2 = cv.imread('temple2.jpg') # load the second image into the img2 variable

alpha = 0.2 #sets how much fade there will be
dst = cv.addWeighted(img1,1-alpha,img2,alpha,0) #blend the two images together and store in dst variable
cv.imshow('dst',dst)#display the new blended image
cv.waitKey(0)#wait for key press to end program
cv.destroyAllWindows()#kill all windows and end program

#The potential application for this is creating an interactive GUI with animations, similar to power point transitions.