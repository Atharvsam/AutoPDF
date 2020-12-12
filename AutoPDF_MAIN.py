from PyQt5 import QtCore, QtGui, QtWidgets
from Preview_Manager import previewManager
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QStringListModel

import os
import cv2
import numpy as np
import glob
from PIL import Image
import fpdf

from helper_function.main import *
from helper_function.auto_crop_utils import autoCrop

class Ui_AutoPDF_MainWindow(object):

    def __init__(self):

        self.preview_manager = previewManager()
        self.imageList = []
        self.bwImageList = []
        self.bwmode = False
        self.save_img = False
        self.start_coord = (0,0)
        self.end_coord = (0,0)

        self.pdf_list = []

        self.aCrp = autoCrop()

    def setupUi(self, AutoPDF_MainWindow):
        
        AutoPDF_MainWindow.setObjectName("AutoPDF_MainWindow")
        AutoPDF_MainWindow.resize(1132, 736)
        
        self.previewImageLabel = QtWidgets.QLabel(AutoPDF_MainWindow)
        self.previewImageLabel.setGeometry(QtCore.QRect(695, 98, 344, 541))
        self.previewImageLabel.setText("")
        self.previewImageLabel.setObjectName("previewImageLabel")
        
        self.documentPreviewLabel = QtWidgets.QLabel(AutoPDF_MainWindow)
        self.documentPreviewLabel.setGeometry(QtCore.QRect(695, 39, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.documentPreviewLabel.setFont(font)
        self.documentPreviewLabel.setObjectName("documentPreviewLabel")
        
        self.importPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.importPushButton.setGeometry(QtCore.QRect(88, 98, 167, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.importPushButton.setFont(font)
        self.importPushButton.setObjectName("importPushButton")
        self.importPushButton.clicked.connect(self.importPushButtonAction)

        self.fileDialog = QFileDialog()
        self.fileDialog.setFileMode(QFileDialog.ExistingFiles)
        #self.fileDialog.setFilter("Images ("'.jpg','.png','jpeg'")")

        self.imagePaths = QStringListModel()
        
        self.bwPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.bwPushButton.setGeometry(QtCore.QRect(80, 169, 215, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bwPushButton.setFont(font)
        self.bwPushButton.setObjectName("bwPushButton")
        self.bwPushButton.clicked.connect(self.bwPushButtonAction)
        
        self.prevPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.prevPushButton.setGeometry(QtCore.QRect(695, 666, 43, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prevPushButton.setFont(font)
        self.prevPushButton.setObjectName("prevPushButton")
        self.prevPushButton.clicked.connect(self.prevPushButtonAction)

        self.nextPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.nextPushButton.setGeometry(QtCore.QRect(996, 666, 43, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nextPushButton.setFont(font)
        self.nextPushButton.setObjectName("nextPushButton")
        self.nextPushButton.clicked.connect(self.nextPushButtonAction)

        self.pageStatusLabel = QtWidgets.QLabel(AutoPDF_MainWindow)
        self.pageStatusLabel.setGeometry(QtCore.QRect(751, 666, 231, 32))
        self.pageStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pageStatusLabel.setObjectName("pageStatusLabel")

        self.delAllPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.delAllPushButton.setGeometry(QtCore.QRect(500, 690, 131, 28))
        self.delAllPushButton.setObjectName("delAllPushButton")
        self.delAllPushButton.clicked.connect(self.delAllPushButtonAction)
        
        self.delPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.delPushButton.setGeometry(QtCore.QRect(500, 640, 121, 31))
        self.delPushButton.setObjectName("delPushButton")
        self.delPushButton.clicked.connect(self.delPushButtonAction)

        self.manCropPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.manCropPushButton.setGeometry(QtCore.QRect(80, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.manCropPushButton.setFont(font)
        self.manCropPushButton.setObjectName("manCropPushButton")
        self.manCropPushButton.clicked.connect(self.manCropPushButtonAction)

        self.autoCropPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.autoCropPushButton.setGeometry(QtCore.QRect(80, 240, 215, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.autoCropPushButton.setFont(font)
        self.autoCropPushButton.setObjectName("autoCropPushButton")
        self.autoCropPushButton.clicked.connect(self.autoCropPushButtonAction)

        self.crtPDFPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.crtPDFPushButton.setGeometry(QtCore.QRect(80, 650, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.crtPDFPushButton.setFont(font)
        self.crtPDFPushButton.setObjectName("crtPDFPushButton")
        self.crtPDFPushButton.clicked.connect(self.crtPDFPushButtonAction)

        self.retranslateUi(AutoPDF_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(AutoPDF_MainWindow)

    def retranslateUi(self, AutoPDF_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        AutoPDF_MainWindow.setWindowTitle(_translate("AutoPDF_MainWindow", "AutoPDF"))
        AutoPDF_MainWindow.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(81,74,74)"))
        
        self.documentPreviewLabel.setText(_translate("AutoPDF_MainWindow", "Document Preview"))
        self.documentPreviewLabel.setStyleSheet(_translate("AutoPDF_MainWindow", "color:rgb(255,255,255)"))

        self.importPushButton.setText(_translate("AutoPDF_MainWindow", "Import"))
        self.importPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(0,255,0)"))

        self.bwPushButton.setText(_translate("AutoPDF_MainWindow", "Black And White"))
        self.bwPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(255,255,255)"))

        self.prevPushButton.setText(_translate("AutoPDF_MainWindow", "<"))
        self.prevPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(108, 122, 185)"))
        self.nextPushButton.setText(_translate("AutoPDF_MainWindow", ">"))
        self.nextPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(108, 122, 185)"))
        
        self.pageStatusLabel.setText(_translate("AutoPDF_MainWindow", "0/0 Page"))
        self.pageStatusLabel.setStyleSheet(_translate("AutoPDF_MainWindow", "color:rgb(255,255,255)"))
        
        self.delAllPushButton.setText(_translate("AutoPDF_MainWindow", "Remove All Pages"))
        self.delAllPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(255,23,112);color:rgb(255,255,102);"))
        
        self.delPushButton.setText(_translate("AutoPDF_MainWindow", "Delete This Page"))
        self.delPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(255,118,84);color:rgb(125,20,132);"))
        
        self.manCropPushButton.setText(_translate("AutoPDF_MainWindow", "Manual Crop"))
        self.manCropPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(117,115,105)"))

        self.autoCropPushButton.setText(_translate("AutoPDF_MainWindow", "Auto Crop"))
        self.autoCropPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(54,93,218)"))

        self.crtPDFPushButton.setText(_translate("AutoPDF_MainWindow", "Create PDF"))
        self.crtPDFPushButton.setStyleSheet(_translate("AutoPDF_MainWindow", "background-color:rgb(255,187,28)"))

    def importPushButtonAction(self):

        if self.fileDialog.exec_():
            self.imagePaths = self.fileDialog.selectedFiles()
            for paths in self.imagePaths:
                img = cv2.imread(paths)
                self.preview_manager.image_list.append(cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))))
            image = cv2.resize(self.preview_manager.image_list[0],(344,541))
            self.previewImageLabel.setPixmap(
                QtGui.QPixmap.fromImage(
                    QtGui.QImage(
                        image.data, 
                        image.shape[1], 
                        image.shape[0],
                        QtGui.QImage.Format_RGB888
                    ).rgbSwapped()
                )
            )
        self.updateStatusLabel()

    def bwPushButtonAction(self):
        for imgs in self.preview_manager.image_list:
            self.preview_manager.bwImageList.append(image_filter.gray(imgs))
        image = cv2.resize(self.preview_manager.bwImageList[self.preview_manager.image_index], (344,541))
        self.previewImageLabel.setPixmap(
                QtGui.QPixmap.fromImage(
                    QtGui.QImage(
                        image.data, 
                        image.shape[1], 
                        image.shape[0],
                        QtGui.QImage.Format_Grayscale8
                    )
                )
            )
        self.preview_manager.bw_mode = True

    def nextPushButtonAction(self):
        image = self.preview_manager.next_image()
        image = cv2.resize(image, (344,541))
        if self.preview_manager.bw_mode:
            self.previewImageLabel.setPixmap(
                QtGui.QPixmap.fromImage(
                    QtGui.QImage(
                        image.data, 
                        image.shape[1], 
                        image.shape[0],
                        QtGui.QImage.Format_Grayscale8
                    )
                )
            )
        else:
            self.previewImageLabel.setPixmap(
                    QtGui.QPixmap.fromImage(
                        QtGui.QImage(
                            image.data, 
                            image.shape[1], 
                            image.shape[0],
                            QtGui.QImage.Format_RGB888
                        ).rgbSwapped()
                    )
                )
        self.updateStatusLabel()


    def prevPushButtonAction(self):
        image = self.preview_manager.prev_image()
        image = cv2.resize(image, (344,541))
        self.previewImageLabel.setPixmap(
                QtGui.QPixmap.fromImage(
                    QtGui.QImage(
                        image.data, 
                        image.shape[1], 
                        image.shape[0],
                        QtGui.QImage.Format_RGB888
                    ).rgbSwapped()
                )
            )
        self.updateStatusLabel()

    def updateStatusLabel(self):
        self.pageStatusLabel.setText("{0}/{1} Pages".format(self.preview_manager.image_index+1, len(self.preview_manager.image_list)))

    def delPushButtonAction(self):
        if self.preview_manager.bw_mode:
            self.preview_manager.bwImageList.pop(self.preview_manager.image_index)
        else:
            self.preview_manager.image_list.pop(self.preview_manager.image_index)
        self.updateStatusLabel()
    
    def delAllPushButtonAction(self):
        self.preview_manager.image_list = []
        self.preview_manager.bwImageList = []
        self.updateStatusLabel()

    def manCropPushButtonAction(self):
        if self.preview_manager.bw_mode:
            img = self.preview_manager.bwImageList[self.preview_manager.image_index].copy()
        else:
            img = self.preview_manager.image_list[self.preview_manager.image_index].copy()

        self.save_img, self.start_coord, self.end_coord = imedit.manual_crop(img)

    def autoCropPushButtonAction(self):
        if self.preview_manager.bw_mode == False:
            temp_list = []
            for img in self.preview_manager.image_list:
                temp_list.append(self.aCrp.main(img))
            self.preview_manager.image_list = temp_list
            image = cv2.resize(self.preview_manager.image_list[self.preview_manager.image_index], (344,541))
            self.previewImageLabel.setPixmap(
                    QtGui.QPixmap.fromImage(
                        QtGui.QImage(
                            image.data, 
                            image.shape[1], 
                            image.shape[0],
                            QtGui.QImage.Format_RGB888
                        ).rgbSwapped()
                    )
                )

    def crtPDFPushButtonAction(self):
        dir_path = QFileDialog.getSaveFileName(AutoPDF_MainWindow, 'Save File', 'PDF Files (*.py)')
        if os.path.exists('temp'):
            filepaths = glob.glob(os.path.join('temp', "*.png"))
            for path in filepaths:
                os.remove(path)
        else:
            os.mkdir('temp')
        img_list = self.preview_manager.image_list if self.preview_manager.bw_mode!=True else self.preview_manager.bwImageList
        if len(img_list)>0:
            counter = 0
            for img in img_list:
                cv2.imwrite('temp/{0}.png'.format(counter), img)
                counter+=1
            i=0
            while(counter>0):
                self.pdf_list.append(Image.open('temp/{0}.png'.format(i)))
                i+=1
                counter-=1
            
            if dir_path != {}:
                
                temp = []
                for img in self.pdf_list:
                    temp.append(img.convert('RGB'))
                temp_img = temp[0]
                temp.pop(0)
                print(dir_path)
                temp_img.save(dir_path[0], save_all=True, append_images=temp)

            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoPDF_MainWindow = QtWidgets.QWidget()
    ui = Ui_AutoPDF_MainWindow()
    ui.setupUi(AutoPDF_MainWindow)
    AutoPDF_MainWindow.show()
    sys.exit(app.exec_())
