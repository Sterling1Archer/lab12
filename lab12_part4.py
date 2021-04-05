import cv2 as cv
import numpy as np

img = cv.imread('temple.jpeg') #load the image into img variable
res = cv.resize(img,(0,0),fx=1, fy=1, interpolation = cv.INTER_CUBIC) #resize img

cv.imwrite("temple2.jpg", cv.Canny(res, 499, 281)) # detects the edges of the first image compared to the second and writes it to a file
cv.imshow("temple", cv.imread("temple2.jpg")) # show the modified image
cv.waitKey()#wait till key press to end program
cv.destroyAllWindows() #kill all active windwos and close the program

#This program could be used to detect the edges of object in a photo which can be used for software
#that can detect where objects are and help with object avoidance in robots for example.