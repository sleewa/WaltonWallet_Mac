# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewContactForm.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(474, 419)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 330, 291, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 120, 371, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setToolTip("")
        self.lineEdit_6.setStatusTip("")
        self.lineEdit_6.setWhatsThis("")
        self.lineEdit_6.setAccessibleName("")
        self.lineEdit_6.setAccessibleDescription("")
        self.lineEdit_6.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(40, 240, 371, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setToolTip("")
        self.lineEdit_7.setStatusTip("")
        self.lineEdit_7.setWhatsThis("")
        self.lineEdit_7.setAccessibleName("")
        self.lineEdit_7.setAccessibleDescription("")
        self.lineEdit_7.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_51 = QtWidgets.QLabel(Form)
        self.label_51.setGeometry(QtCore.QRect(40, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_51.setObjectName("label_51")
        self.line_38 = QtWidgets.QFrame(Form)
        self.line_38.setGeometry(QtCore.QRect(40, 150, 371, 16))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.line_41 = QtWidgets.QFrame(Form)
        self.line_41.setGeometry(QtCore.QRect(40, 270, 371, 16))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.label_52 = QtWidgets.QLabel(Form)
        self.label_52.setGeometry(QtCore.QRect(30, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_52.setObjectName("label_52")
        self.pushButton_36 = QtWidgets.QPushButton(Form)
        self.pushButton_36.setGeometry(QtCore.QRect(410, 110, 41, 41))
        self.pushButton_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_36.setAutoFillBackground(False)
        self.pushButton_36.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_36.setIcon(icon)
        self.pushButton_36.setIconSize(QtCore.QSize(77, 77))
        self.pushButton_36.setAutoDefault(False)
        self.pushButton_36.setFlat(True)
        self.pushButton_36.setObjectName("pushButton_36")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.closeenterpsw = QtWidgets.QPushButton(Form)
        self.closeenterpsw.setGeometry(QtCore.QRect(430, 0, 41, 31))
        self.closeenterpsw.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon1)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_9.setText(_translate("Form", "Save"))
        self.label_51.setText(_translate("Form", "Name:"))
        self.label_52.setText(_translate("Form", "Recipient Address:"))
        self.label_15.setText(_translate("Form", "New Contact"))

