from PyQt5 import QtCore, QtGui, QtWidgets
from Preview_Manager import previewManager


class Ui_detFace(object):

    def __init__(self):
        self.face_list = None
        self.preview_manager = previewManager()

    def setupUi(self, detFace, face_list):
        self.face_list = face_list
        self.preview_manager.image_list = self.face_list
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
        self.prevPushButton.clicked.connect(self.prevPushButton)

        self.nextPushButton = QtWidgets.QPushButton(detFace)
        self.nextPushButton.setGeometry(QtCore.QRect(280, 370, 51, 31))
        self.nextPushButton.setStyleSheet("background-color: rgb(165, 224, 255);\n"
"border-radius:10;\n"
"border:5px solid yellow")
        self.nextPushButton.setObjectName("nextPushButton")
        self.nextPushButton.clicked.connect(self.nextPushButtonAction)

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


    def prevPushButtonAction(self):
        image = self.preview_manager.prev_image()
        image = cv2.resize(image, (200,200))
        if self.preview_manager.bw_mode:
            self.detFaceLabel.setPixmap(
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
            self.detFaceLabel.setPixmap(
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

    def nextPushButtonAction(self):
        image = self.preview_manager.next_image()
        image = cv2.resize(image, (200,200))
        if self.preview_manager.bw_mode:
            self.detFaceLabel.setPixmap(
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
            self.detFaceLabel.setPixmap(
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
        self.statusLabel.setText("{0}/{1}".format(self.preview_manager.image_index+1, len(self.preview_manager.image_list)))

