import cv2
import numpy as np

class bw():
    def __init__(self):
        pass
    
    def gray(image):
        grayImage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return grayImage

    def face(image):
        faceCascade=cv2.CascadeClassifier(cascPath)
        grayImage=cv2.cvtColor(originalImage, cv2.COLOR_2GBGRRAY)
        faces=faceCascade.detectMultiScale
        (
            gray,
            scaleFactor=1.1,
            minNeighbour=5,
            minSize=(30,30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        return faces