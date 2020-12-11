import cv2
import numpy as np

class image_filter():

    def gray(image):
        grayImage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return grayImage

    def face(image):
        faceCascade=cv2.CascadeClassifier('frontalface.xml')
        grayImage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbour=5,
            minSize=(30,30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        return faces