import cv2
import numpy as np

class image_filter():

    def gray(image):
        grayImage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return grayImage

    def face(image):
        face_list = []
        faceCascade=cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
        grayImage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(
            grayImage,
            1.1,
            minNeighbour=5,
            minSize=(30,30),
            flags=cv2.CV_HAAR_SCALE_IMAGE
        )
        for (x,y,w,h) in faces:
            face_list.append(image[y:y+h, x:x+w])
        return face_list

class image_editing():
    
    def __init__(self):
        self.past_coord = (-1, -1)
        self.drag_active = False
        self.curr_coord = (0, 0)
        self.org_img_copy = None

    def manual_crop(self, org_img_copy):
        org_img_copy = cv2.resize(org_img_copy, (344, 541))
        self.org_img_copy = org_img_copy
        self.copy_img = self.org_img_copy
        cv2.namedWindow('crop_editor')
        cv2.setMouseCallback('crop_editor', self.crop_zone)

        while True:

            cv2.imshow('crop_editor', self.org_img_copy.copy())
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                return False, self.past_coord, self.curr_coord
            elif k == ord('s'):
                cv2.destroyAllWindows()
                return True, self.past_coord, self.curr_coord
            elif k == ord('c'):
                self.org_img_copy = self.copy_img

    def crop_zone(self, event, x, y, flags, param):
        
        if event == cv2.EVENT_LBUTTONDOWN:
            self.org_img_copy = self.copy_img
            self.drag_active = True
            self.past_coord = (x,y)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drag_active = False
            cv2.rectangle(self.org_img_copy, self.past_coord, (x,y), (0,255,0), 1)
        self.curr_coord = (x, y)

imedit = image_editing()