import cv2 as cv
import numpy as np

img = cv.imread('warsaw-skyscraper.jpg') #load image into img variable

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #turn the image into a grayscale and store in gray variable
edges = cv.Canny(gray, 50, 120) #detect edges and store in edges variable
minLineLength = 20 #sets parameters for lines
maxLineGap = 5

lines = cv.HoughLinesP(edges, 1, np.pi/180.0, 20, minLineLength, maxLineGap) #save lines detected in image into lines variable

for x1, y1, x2, y2 in lines[index]:
    cv.line(img, (x1, y1), (x2, y2), (0,255,0),2)#modify image size
    cv.imshow("edges", edges) #show images with edges detected
    cv.imshow("lines", img)#show image displaying the lines traced on the edges
cv.waitKey() #wait for key press to end program
cv.destroyAllWindows()#kill all windows and end program