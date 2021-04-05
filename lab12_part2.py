import numpy as np #import numpy
import cv2 as cv #import opencv
cap = cv.VideoCapture('George Carlin on Consumerism - Edited Audio.avi') #load the video into variable cap
if not cap.isOpened(): #if there's an issue opening the video file.
    print("Cannot open camera")#print the issue
    exit()#exit the program
while True:
    # Capture frame-by-frame
    ret, frame = cap.read() #capture frame by frame of the video file and store it in ret
    # if frame is read correctly ret is True
    if not ret:#if there's an issue with reading the frame, assume end of file.
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)#turns fram into grayscale
    
    # Display the resulting frame
    #cv.imshow('frame', gray) #displays the frame in grayscale
    cv.imshow('frame', frame) #displays the frame in original color
    
    if cv.waitKey(1) == ord('q'):#wait for keystroke to quit or end after 1 second
        break
# When everything done, release the capture
cap.release()  #notifies the system that the program is no longer using the file.
cv.destroyAllWindows() #kill all the active windows of the program and ends it.

#This program could be used to capture a video from either another video, or a camera,
#and then save it to a video file to be observed later. Perhaps recording video of plants
#growing over time, then watch the timelapse afterwards.