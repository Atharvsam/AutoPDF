# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AutoPDF_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AutoPDF_MainWindow(object):
    def setupUi(self, AutoPDF_MainWindow):
        AutoPDF_MainWindow.setObjectName("AutoPDF_MainWindow")
        AutoPDF_MainWindow.resize(1132, 736)
        AutoPDF_MainWindow.setAutoFillBackground(False)
        AutoPDF_MainWindow.setStyleSheet("background-color:rgb(81, 74, 74)")
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
        self.importPushButton.setStyleSheet("background-color:rgb(0, 255, 0);\n"
"border-radius:20;\n"
"border:3px solid yellow")
        self.importPushButton.setObjectName("importPushButton")
        self.bwPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.bwPushButton.setGeometry(QtCore.QRect(80, 169, 215, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bwPushButton.setFont(font)
        self.bwPushButton.setObjectName("bwPushButton")
        self.prevPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.prevPushButton.setGeometry(QtCore.QRect(695, 666, 43, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prevPushButton.setFont(font)
        self.prevPushButton.setStyleSheet("background-color:rgb(108, 122, 185)")
        self.prevPushButton.setObjectName("prevPushButton")
        self.nextPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.nextPushButton.setGeometry(QtCore.QRect(996, 666, 43, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nextPushButton.setFont(font)
        self.nextPushButton.setObjectName("nextPushButton")
        self.pageStatusLabel = QtWidgets.QLabel(AutoPDF_MainWindow)
        self.pageStatusLabel.setGeometry(QtCore.QRect(751, 666, 231, 32))
        self.pageStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pageStatusLabel.setObjectName("pageStatusLabel")
        self.delAllPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.delAllPushButton.setGeometry(QtCore.QRect(500, 690, 131, 28))
        self.delAllPushButton.setStyleSheet("background-color: rgb(255, 23, 112);\n"
"color: rgb(255, 255, 102);")
        self.delAllPushButton.setObjectName("delAllPushButton")
        self.delPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.delPushButton.setGeometry(QtCore.QRect(500, 640, 121, 31))
        self.delPushButton.setStyleSheet("background-color: rgb(255, 118, 84);\n"
"color: rgb(125, 20, 132);")
        self.delPushButton.setObjectName("delPushButton")
        self.manCropPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.manCropPushButton.setGeometry(QtCore.QRect(80, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.manCropPushButton.setFont(font)
        self.manCropPushButton.setStyleSheet("background-color:rgb(117, 115, 105)")
        self.manCropPushButton.setObjectName("manCropPushButton")
        self.autoCropPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.autoCropPushButton.setGeometry(QtCore.QRect(80, 240, 215, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.autoCropPushButton.setFont(font)
        self.autoCropPushButton.setStyleSheet("background-color: rgb(54, 93, 218);")
        self.autoCropPushButton.setObjectName("autoCropPushButton")
        self.crtPDFPushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.crtPDFPushButton.setGeometry(QtCore.QRect(80, 650, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.crtPDFPushButton.setFont(font)
        self.crtPDFPushButton.setStyleSheet("background-color: rgb(255, 187, 28);")
        self.crtPDFPushButton.setObjectName("crtPDFPushButton")
        self.detFacePushButton = QtWidgets.QPushButton(AutoPDF_MainWindow)
        self.detFacePushButton.setGeometry(QtCore.QRect(360, 170, 215, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.detFacePushButton.setFont(font)
        self.detFacePushButton.setStyleSheet("background-color: rgb(194, 94, 255);")
        self.detFacePushButton.setObjectName("detFacePushButton")

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
        self.delAllPushButton.setText(_translate("AutoPDF_MainWindow", "Remove All Pages"))
        self.delPushButton.setText(_translate("AutoPDF_MainWindow", "Delete This Page"))
        self.manCropPushButton.setText(_translate("AutoPDF_MainWindow", "Manual Crop"))
        self.autoCropPushButton.setText(_translate("AutoPDF_MainWindow", "Auto Crop"))
        self.crtPDFPushButton.setText(_translate("AutoPDF_MainWindow", "Create PDF"))
        self.detFacePushButton.setText(_translate("AutoPDF_MainWindow", "Detect Faces"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoPDF_MainWindow = QtWidgets.QWidget()
    ui = Ui_AutoPDF_MainWindow()
    ui.setupUi(AutoPDF_MainWindow)
    AutoPDF_MainWindow.show()
    sys.exit(app.exec_())
