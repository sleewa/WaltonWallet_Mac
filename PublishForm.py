# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PublishForm.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_publishForm(object):
    def setupUi(self, publishForm):
        publishForm.setObjectName("publishForm")
        publishForm.resize(390, 182)
        publishForm.setStyleSheet("")
        self.pushButton_9 = QtWidgets.QPushButton(publishForm)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 120, 231, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:18px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.closeenterpsw = QtWidgets.QPushButton(publishForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(350, 0, 41, 31))
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.textEdit = QtWidgets.QTextEdit(publishForm)
        self.textEdit.setGeometry(QtCore.QRect(30, 40, 301, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(publishForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 181))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pic/图表.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton_9.raise_()
        self.closeenterpsw.raise_()
        self.textEdit.raise_()

        self.retranslateUi(publishForm)
        QtCore.QMetaObject.connectSlotsByName(publishForm)

    def retranslateUi(self, publishForm):
        _translate = QtCore.QCoreApplication.translate
        publishForm.setWindowTitle(_translate("publishForm", "Form"))
        self.pushButton_9.setText(_translate("publishForm", "Confirm"))

