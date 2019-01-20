import cv2 
import numpy as np 
import time 
def basic():
    #That will create nd-numpy array with all zero fill in
    #it's a 3d array of zeros, zero represents black color
    #result will be 
    #Image file with 512 * 512 pixel 
    #Total number of color combination is 512*512*3 
    image = np.zeros((512, 512, 3), np.uint8)

    #(x,y) position, numpy size pixel value of the image
    #For this image we have X scale is 512 and Y scale is 
    #512. If we want to draw a line inbetween then 
    #cordinates will be (0,256) and (512,256) 
    cv2.line(image, (0,256),(512,256), (255,0,0), 2 )

    #Tag with the label numpy image 
    cv2.imshow('numpy image', image)

    #Wait for 5000 mili second
    cv2.waitKey(5000)

    #Then this will close the window
    cv2.destroyAllWindows()

basic()
