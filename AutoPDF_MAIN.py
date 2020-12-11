from PyQt5 import QtCore, QtGui, QtWidgets
from Preview_Manager import previewManager
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QStringListModel

import os
import cv2
import numpy as np

class Ui_AutoPDF_MainWindow(object):

    def __init__(self):

        self.preview_manager = previewManager()
        self.imageList = []
        self.bwImageList = []

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

        self.retranslateUi(AutoPDF_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(AutoPDF_MainWindow)

    def retranslateUi(self, AutoPDF_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        AutoPDF_MainWindow.setWindowTitle(_translate("AutoPDF_MainWindow", "AutoPDF"))
        self.documentPreviewLabel.setText(_translate("AutoPDF_MainWindow", "Document Preview"))
        self.importPushButton.setText(_translate("AutoPDF_MainWindow", "Import"))
        self.bwPushButton.setText(_translate("AutoPDF_MainWindow", "Black And White"))
        self.prevPushButton.setText(_translate("AutoPDF_MainWindow", "<"))
        self.nextPushButton.setText(_translate("AutoPDF_MainWindow", ">"))
        self.pageStatusLabel.setText(_translate("AutoPDF_MainWindow", "0/0 Page"))

    def importPushButtonAction(self):

        if self.fileDialog.exec_():
            self.imagePaths = self.fileDialog.selectedFiles()
            for paths in self.imagePaths:
                self.preview_manager.image_list.append(cv2.resize(cv2.imread(paths),(344,541)))
            self.previewImageLabel.setPixmap(
                QtGui.QPixmap.fromImage(
                    QtGui.QImage(
                        self.preview_manager.image_list[0].data, 
                        self.preview_manager.image_list[0].shape[1], 
                        self.preview_manager.image_list[0].shape[0],
                        QtGui.QImage.Format_RGB888
                    ).rgbSwapped()
                )
            )

    def bwPushButtonAction(self):
        for imgs in self.preview_manager.image_list:
            self.bwImageList.append()

    def nextPushButtonAction(self):
        pass

    def prevPushButtonAction(self):
        pass

    def updateStatusLabel(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoPDF_MainWindow = QtWidgets.QWidget()
    ui = Ui_AutoPDF_MainWindow()
    ui.setupUi(AutoPDF_MainWindow)
    AutoPDF_MainWindow.show()
    sys.exit(app.exec_())
