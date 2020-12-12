import cv2
import numpy as np
import imutils
import math


class autoCrop():

    def __init__(self):
        
        self.image = None
        self.gray = None
        self.thresh = None
        self.lookUp = np.empty((1,256), np.uint8)
        self.gamma = 0.0
        self.hist_bin = None
        self.percentage = 0.0
        self.perc_diff = 0.0
        self.last_thresh = None

    def smallest_x(self, pnts):
        k = pnts[0][0][0]
        for j in pnts:
            if k>j[0][0]:
                k = j[0][0]
        return k

    def largest_x(self, pnts):
        k = pnts[0][0][0]
        for j in pnts:
            if k<j[0][0]:
                k = j[0][0]
        return k

    def smallest_y(self, pnts):
        k = pnts[0][0][1]
        for j in pnts:
            if k>j[0][1]:
                k = j[0][1]
        return k

    def largest_y(self, pnts):
        k = pnts[0][0][1]
        for j in pnts:
            if k<j[0][1]:
                k = j[0][1]
        return k

    def euclid_dist_farthest(self, pnt, x, y):
        dist = 0
        point = (0,0)

        for j in pnt:
            dist_new = int(math.sqrt(pow(j[0][0]-x,2)+pow(j[0][1]-y,2)))
            if dist < dist_new:
                dist = dist_new
                point = (j[0][0],j[0][1])

        return point

    def auto_gamma(self, image, strides=0.3):
        
        self.image = image
        self.copy_image = self.image.copy()

        self.last_perc = 100.0
        self.curr_perc = 100.0
        self.gamma = 0.0
        while self.gamma<5.0:
            self.image = self.copy_image
            for j in range(256):
                self.lookUp[0,j] = np.clip(pow(j/255.0, self.gamma) * 255.0, 0, 255)

            self.image = cv2.LUT(self.image, self.lookUp)
            self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.gray = cv2.GaussianBlur(self.gray, (5,5), 0)

            ret, self.thresh = cv2.threshold(self.gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            self.hist_bin = cv2.calcHist([self.thresh], [0], None, [2], [0,256])
            total = self.hist_bin[0][0] + self.hist_bin[1][0]

            self.percentage = (self.hist_bin[1][0]/total)*100

            self.perc_diff = self.last_perc - self.percentage

            if self.percentage<=75.0 or self.perc_diff>10:
                if self.percentage<=75:
                    self.last_thresh = self.thresh
                    return self.thresh
                if self.perc_diff>10:
                    return self.last_thresh
            self.gamma+=0.3

    def manual_gamma(self, image, gamma):
        self.gamma = gamma
        self.image = image
        self.copy_image = self.image.copy()
        for j in range(256):
            self.lookUp[0,j] = np.clip(pow(j/255.0, self.gamma) * 255.0, 0, 255)

        self.image = cv2.LUT(self.image, self.lookUp)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.gray = cv2.GaussianBlur(self.gray, (5,5), 0)

        ret, self.thresh = cv2.threshold(self.gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return self.thresh

    def main(self, img):

        self.thresh = self.manual_gamma(img, gamma=2.36)

        contours = cv2.findContours(self.thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(contours)

        area = 0
        _pnts = None

        for pnts in cnts:
            M = cv2.moments(pnts)
            if area < M['m00']:
                area = M['m00']
                _pnts = pnts
                #approx = cv2.approxPolyDP(_p, 0.15*cv2.arcLength(_p, True), True)
            #center_x = int(M["m10"]/M["m00"])
            #center_y = int(M["m01"]/M["m00"])

        #cv2.drawContours(copy_image, [_p], -1, (0,0,255), 2)
        #print(_p)
        #print(approx)

        x1 = self.smallest_x(_pnts)
        y1 = self.smallest_y(_pnts)
        x2 = self.largest_x(_pnts)
        y2 = self.largest_y(_pnts)

        point1 = self.euclid_dist_farthest(_pnts, x1, y1)
        point2 = self.euclid_dist_farthest(_pnts, x1, y2)
        max_x = max(point1[0], point2[0])

        curr_state = np.float32([[x1, y1], [point2[0], point2[1]], [x1, y2], [point1[0], point1[1]]])
        finl_state = np.float32([[0, 0], [self.copy_image.shape[1], 0], [0, self.copy_image.shape[0]], [self.copy_image.shape[1], self.copy_image.shape[0]]])

        persp = cv2.getPerspectiveTransform(curr_state, finl_state)

        return cv2.warpPerspective(self.copy_image, persp, (self.copy_image.shape[1], self.copy_image.shape[0]))



