import cv2 as cv #import open cv
import sys #importing operating system dependent functionality
img = cv.imread('temple.jpeg') #load the image into the program
res = cv.resize(img,(0,0),fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)#Resizes the image and stores it in to a new image variable

if img is None: #detect if there was an issue opening the image
    sys.exit("The image could not be read.") #Exit the program and display the error

cv.imshow("OpenCV Image", res) #Show the image loaded into variable img
    
cv.waitKey(0) # waits indefinitely for a keystroke
cv.destroyAllWindows() #destroys all open windows in the program.
