# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dialog_poachers.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 388)
        Dialog.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(Dialog)
        self.centralWidget.setGeometry(QtCore.QRect(0, 0, 411, 391))
        self.centralWidget.setStyleSheet("#centralWidget {\n"
"    background: center url(:/poachers.jpg) 50% 50%;\n"
"}")
        self.centralWidget.setObjectName("centralWidget")
        self.shoot_time_label_3 = QtWidgets.QLabel(self.centralWidget)
        self.shoot_time_label_3.setGeometry(QtCore.QRect(30, 210, 341, 61))
        self.shoot_time_label_3.setStyleSheet("font: 14pt \"Comfortaa\";\n"
"color: black;\n"
"background-color: rgba(188, 110, 110, 200);")
        self.shoot_time_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.shoot_time_label_3.setObjectName("shoot_time_label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 411, 401))
        self.pushButton.setStyleSheet("background-color: rgba(255, 0, 0, 64);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.button_ok = QtWidgets.QPushButton(self.centralWidget)
        self.button_ok.setGeometry(QtCore.QRect(30, 330, 341, 31))
        self.button_ok.setStyleSheet("font: 14pt \"Comfortaa\";\n"
"background-color: rgb(170, 0, 0);")
        self.button_ok.setObjectName("button_ok")
        self.poachers_label_3 = QtWidgets.QLabel(self.centralWidget)
        self.poachers_label_3.setGeometry(QtCore.QRect(90, 50, 221, 121))
        self.poachers_label_3.setStyleSheet("font: 20pt \"Comfortaa\";\n"
"background-color: rgba(188, 110, 110, 200);\n"
"color: black;")
        self.poachers_label_3.setScaledContents(False)
        self.poachers_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.poachers_label_3.setObjectName("poachers_label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.shoot_time_label_3.setText(_translate("Dialog", "Время выстрела:\n"
"h часов m минут назад"))
        self.button_ok.setText(_translate("Dialog", "OK"))
        self.poachers_label_3.setText(_translate("Dialog", "Браконьеры\n"
"виновны!"))
from resources.resources import *
