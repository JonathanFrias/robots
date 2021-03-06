import numpy as np
import cv2

# openCV will only work with Numpy Arrays
# the three item represented in HSV (Hue, Saturation, and Value) 
ORANGE = { 'lower': np.array([5, 50, 110],np.uint8),  'upper': np.array([15, 255, 255],np.uint8) };

RED = (0,0,255)

def detectColor(image, color):


    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, color['lower'], color['upper'])

    # Do a bitwise and with the original and mask. This will provide an insection. 
    # All pixels in the mask that correspond to the original will be recognized as a 
    # binary 1
    output = cv2.bitwise_and(image, image, mask = mask)

    return output

def findContours(image):


    # Frame capture need to be in gray scale in order to threshold image
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Paramaters:
    # 1. source image
    # 2. threshold value: Pixels greater than 127 will converted to black 255
    #                  Pixels less than 127 will converted to white
    # 3. Max color value 255 black 
    # 4. Amount of channels in the image. Grayscale image only has one channel or color intensity. 
    # Returns threshold-ed imaga
    ret,thresh = cv2.threshold(grayscale,80,255,0)


    # Parameters:
    # 1. source image
    # 2. Contour retrieval mode used
    # 3. Contour approximation method used
    # Returns a list contour object. A contour object contain info on each point that make up the contour
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    return contours

class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
    	return self.x

    def getY(self):
    	return self.y

