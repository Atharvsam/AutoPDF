import cv2
import numpy as np
from PyQt5 import QtGui

class previewManager():

    def __init__(self):
        
        self.image_list = []
        self.bwImageList = []
        self.image_index = 0
        self.current_image = None
        self.limit_crossed = False
        self.bw_mode = False

    def get_images(self, image_list):
        self.image_list = image_list

    def next_image(self):
        self.image_index += 1

        _list = self.bwImageList if self.bw_mode else self.image_list

        if self.image_index>=len(_list):
            self.limit_crossed = True
            self.image_index -= 1

        if self.limit_crossed != True:
            self.current_image = _list[self.image_index]

        self.limit_crossed = False

        return self.current_image

    def prev_image(self):
        self.image_index -= 1

        _list = self.bwImageList if self.bw_mode else self.image_list

        if self.image_index<0:
            self.limit_crossed = True
            self.image_index += 1
        
        if self.limit_crossed != True:
            self.current_image = _list[self.image_index]

        self.limit_crossed = False

        return self.current_image