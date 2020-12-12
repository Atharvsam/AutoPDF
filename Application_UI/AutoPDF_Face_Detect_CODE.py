# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AutoPDF_Face_Detect_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_detFace(object):
    def setupUi(self, detFace):
        detFace.setObjectName("detFace")
        detFace.resize(477, 488)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        detFace.setWindowIcon(icon)
        detFace.setStyleSheet("background-color:rgb(81,74,74);")
        self.detFaceLabel = QtWidgets.QLabel(detFace)
        self.detFaceLabel.setGeometry(QtCore.QRect(130, 100, 200, 200))
        self.detFaceLabel.setText("")
        self.detFaceLabel.setObjectName("detFaceLabel")
        self.prevPushButton = QtWidgets.QPushButton(detFace)
        self.prevPushButton.setGeometry(QtCore.QRect(120, 370, 51, 31))
        self.prevPushButton.setStyleSheet("background-color: rgb(165, 224, 255);\n"
"border-radius:10;\n"
"border:5px solid yellow")
        self.prevPushButton.setObjectName("prevPushButton")
        self.prevPushButton_2 = QtWidgets.QPushButton(detFace)
        self.prevPushButton_2.setGeometry(QtCore.QRect(280, 370, 51, 31))
        self.prevPushButton_2.setStyleSheet("background-color: rgb(165, 224, 255);\n"
"border-radius:10;\n"
"border:5px solid yellow")
        self.prevPushButton_2.setObjectName("prevPushButton_2")
        self.previewLabel = QtWidgets.QLabel(detFace)
        self.previewLabel.setGeometry(QtCore.QRect(180, 50, 91, 31))
        self.previewLabel.setStyleSheet("color:rgb(255,255,255)")
        self.previewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewLabel.setObjectName("previewLabel")
        self.stateLabel = QtWidgets.QLabel(detFace)
        self.stateLabel.setGeometry(QtCore.QRect(200, 380, 55, 16))
        self.stateLabel.setStyleSheet("color:rgb(255,255,255)")
        self.stateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stateLabel.setWordWrap(True)
        self.stateLabel.setObjectName("stateLabel")

        self.retranslateUi(detFace)
        QtCore.QMetaObject.connectSlotsByName(detFace)

    def retranslateUi(self, detFace):
        _translate = QtCore.QCoreApplication.translate
        detFace.setWindowTitle(_translate("detFace", "AutoPDF - Detected Face"))
        self.prevPushButton.setText(_translate("detFace", "<"))
        self.prevPushButton_2.setText(_translate("detFace", ">"))
        self.previewLabel.setText(_translate("detFace", "<html><head/><body><p><span style=\" font-size:14pt;\">Preview</span></p></body></html>"))
        self.stateLabel.setText(_translate("detFace", "0/0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    detFace = QtWidgets.QWidget()
    ui = Ui_detFace()
    ui.setupUi(detFace)
    detFace.show()
    sys.exit(app.exec_())
