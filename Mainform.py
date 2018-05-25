import sys
import win32ui
from typing import Type
import win32gui
import Warning_Form
import Core_func
from web3.auto import w3
import json
import os
import webbrowser
import sys
import time
import shutil
import cytoolz._signatures
import cytoolz.utils
import qrcode
import requests

import datetime
from eth_account import Account
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout,QDialog,QFileDialog,QTableWidgetItem,
                             QLineEdit, QFrame, QAbstractItemView)
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from Mainform_QT import *
from SendForm import Ui_SendForm
from RecieveForm import Ui_ReceiveForm
from MulWalForm import Ui_MulWalForm
from ConInfoForm import Ui_ConInfoForm
from PubAddrForm import Ui_PubAddrForm
from NewContactForm import Ui_NewContactForm
from MessForm import  Ui_MessForm


class messform(QWidget, Ui_MessForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MessForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnconfirm = self.ui.pushButton_9
        btnconfirm.clicked.connect(self.closeform)

    def show_w2(self):  # 显示窗体2
        rownum = ex.ui.LogMessage.currentIndex()
        print(rownum)
        self.show()

    def savechange(self):
        ex.m_wallet.accountname = self.ui.lineEdit_7.text()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()

class newcontactform(QWidget, Ui_NewContactForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NewContactForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsave = self.ui.pushButton_9
        btnsave.clicked.connect(self.savechange)
        #self.ui.lineEdit_6.changeEvent.connect(self.showqrcode)
        #self.ui.lineEdit_6.keyPressEvent(self,self.showqrcode)

    def show_w2(self):  # 显示窗体2
        self.show()

    def savechange(self):
        ################
        # waiting to add checking same wallet already existed
        ################
        Rcount = ex.ui.ContactsT.rowCount()
        ex.ui.ContactsT.setRowCount(Rcount + 1)
        newItemAddr = QTableWidgetItem(self.ui.lineEdit_6.text())
        newItemName = QTableWidgetItem(self.ui.lineEdit_7.text())

        ex.ui.ContactsT.setItem(Rcount, 1, newItemAddr)
        ex.ui.ContactsT.setItem(Rcount, 0, newItemName)
        ex.ui.ContactsT.setCellWidget(Rcount, 2, ex.consend)
        ex.ui.ContactsT.setCellWidget(Rcount, 3, ex.conedit)
        ex.ui.ContactsT.setCellWidget(Rcount, 4, ex.condelete)



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()

class pubaddrForm(QWidget, Ui_PubAddrForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PubAddrForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btncopy = self.ui.pushButton_35
        btncopy.clicked.connect(self.copyaddr)
        #self.ui.lineEdit_6.changeEvent.connect(self.showqrcode)
        #self.ui.lineEdit_6.keyPressEvent(self,self.showqrcode)

    def show_w2(self):  # 显示窗体2
        self.show()
        self.showqrcode()

    def showqrcode(self):
        self.ui.lineEdit_8.setText(ex.m_wallet.address)
        strAddressAndAmount = ex.m_wallet.address# + "," + value
        self.imgpub = qrcode.make(strAddressAndAmount)
        self.imgpub.save("pic\\recieve.png")
        self.ui.label.setPixmap(QPixmap("pic\\recieve.png"))
        self.ui.label.setAutoFillBackground(1)

    def copyaddr(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(ex.m_wallet.address)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()

class mulwalform(QWidget, Ui_MulWalForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MulWalForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsave = self.ui.pushButton_9
        btnsave.clicked.connect(self.savechange)


    def show_w2(self):  # 显示窗体2
        self.show()

    def savechange(self):
        ex.m_wallet.accountname = self.ui.lineEdit_7.text()


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()

class recieveform(QWidget, Ui_ReceiveForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReceiveForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btncopy = self.ui.pushButton_34
        btncopy.clicked.connect(self.copyaddr)
        #self.ui.lineEdit_6.changeEvent.connect(self.showqrcode)
        #self.ui.lineEdit_6.keyPressEvent(self,self.showqrcode)



    def showqrcode(self):
        self.ui.lineEdit_8.setText(ex.m_wallet.address)
        value = self.ui.lineEdit_6.text()
        strAddressAndAmount = ex.m_wallet.address# + "," + value
        self.imgpub = qrcode.make(strAddressAndAmount)
        self.imgpub.save("pic\\recieve.png")
        self.ui.label.setPixmap(QPixmap("pic\\recieve.png"))
        self.ui.label.setAutoFillBackground(1)

    def show_w2(self):  # 显示窗体2
        self.show()
        self.showqrcode()

    def copyaddr(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(ex.m_wallet.address)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()

class sendform(QWidget, Ui_SendForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SendForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsend = self.ui.pushButton_9
        btnsend.clicked.connect(self.showenterphrase)
        self.Trans = Transaction
        self.ui.radioButton.toggle()
        self.ui.radioButton.toggled.connect(self.change2Eco)
        self.ui.radioButton.setChecked(0)
        self.ui.radioButton_2.toggle()
        self.ui.radioButton_2.toggled.connect(self.change2Sta)
        self.ui.radioButton_2.setChecked(1)
        self.ui.radioButton_2.isChecked()
        self.ui.radioButton_3.toggle()
        self.ui.radioButton_3.toggled.connect(self.change2Qui)
        self.ui.radioButton_3.setChecked(0)
        self.ui.radioButton_4.toggle()
        self.ui.radioButton_4.toggled.connect(self.change2Cus)
        self.ui.radioButton_4.setChecked(0)


    def change2Eco(self):
        if self.ui.radioButton.isChecked():
            self.ui.lineEdit_8.setText('60000')
            self.ui.lineEdit_9.setText('0.000000018')

    def change2Sta(self):
        if self.ui.radioButton_2.isChecked():
            self.ui.lineEdit_8.setText('200000')
            self.ui.lineEdit_9.setText('0.000000036')

    def change2Qui(self):
        if self.ui.radioButton_3.isChecked():
            self.ui.lineEdit_8.setText('1000000')
            self.ui.lineEdit_9.setText('0.000000072')

    def change2Cus(self):
        if self.ui.radioButton_4.isChecked():
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_9.clear()
            self.ui.lineEdit_8.setPlaceholderText('Enter Gas Limit')
            self.ui.lineEdit_9.setPlaceholderText('Enter Gas Price')

    def show_w2(self):  # 显示窗体2
        balance = requests.get(
            "https://waltonchain.net:18950/api/getBalance/" + ex.m_wallet.address).json()
        a = str(balance)
        self.ui.label_52.setText(a.split(',')[1][11:] + 'WTCT')
        self.show()



    def showenterphrase(self):
        #waiting to add passsword checking
        self.Trans.value = self.ui.lineEdit_6.text().strip()
        self.Trans.Type = 'Send'
        self.Trans.Gas = self.ui.lineEdit_8.text().strip()
        self.Trans.Gasprice = self.ui.lineEdit_9.text().strip()
        #need to get blocknumber and time
        ret = Core_func.Transaction_out(ex.m_wallet.privateKey, self.ui.lineEdit_7.text().strip(), self.ui.lineEdit_6.text().strip(), self.ui.lineEdit_8.text().strip(), self.ui.lineEdit_9.text().strip())
        if ret[0] == 1:
            self.Trans.rawTransaction = ret[1]
            self.Trans.toaddr = self.ui.lineEdit_7.text().strip()
            self.Trans.fromaddr = ex.m_wallet.address
            Rcount = ex.ui.TransactionHistory.rowCount()
            ex.ui.TransactionHistory.setRowCount(Rcount + 1)
            newItemTime = QTableWidgetItem(time.strftime('%Y/%m/%d',time.localtime(time.time())))
            newItemAddr = QTableWidgetItem(ex.m_wallet.address)
            newItemStatus = QTableWidgetItem(self.Trans.status)
            newItemValue = QTableWidgetItem('-'+self.Trans.value+'WTCT')
            ex.ui.TransactionHistory.setItem(Rcount, 0, newItemTime)
            ex.ui.TransactionHistory.setItem(Rcount, 1, newItemAddr)
            ex.ui.TransactionHistory.setItem(Rcount, 2, newItemStatus)
            ex.ui.TransactionHistory.setItem(Rcount, 3, newItemValue)

            Rcount = ex.ui.LogMessage.rowCount()
            ex.ui.LogMessage.setRowCount(Rcount + 1)
            #time needs to be confirmed
            newItemTime = QTableWidgetItem(time.strftime('%Y/%m/%d',time.localtime(time.time())))
            newItemContent = QTableWidgetItem('From:'+self.Trans.fromaddr +'\n'+ 'To:'+self.Trans.toaddr +'\n'+ 'Value:'+self.Trans.value)
            newItemType = QTableWidgetItem(self.Trans.Type)
            ex.ui.LogMessage.setItem(Rcount, 0, newItemType)
            ex.ui.LogMessage.setItem(Rcount, 1, newItemTime)
            ex.ui.LogMessage.setItem(Rcount, 2, newItemContent)

            self.closeform()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_6.clear()


        else:
            print('err')


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()

class Example(QDialog,QWidget):

    def __init__(self):
        super().__init__()

        self.mwOpen = QPushButton(self)  # type: QPushButton
        self.mwOpen.setStyleSheet(''' border:0px; ''')
        self.mwOpen.setIcon(QIcon("pic/open1233.png"))
        self.mwOpen.setIconSize(QSize(70, 50))
        self.mwOpen.clicked.connect(self.pressbtn1)

        self.mwEdit = QPushButton(self)  # type: QPushButton
        self.mwEdit.setStyleSheet(''' border:0px; ''')
        self.mwEdit.setIcon(QIcon("pic/editA.png"))
        self.mwEdit.setIconSize(QSize(70, 50))


        self.mwDelete = QPushButton(self)  # type: QPushButton
        self.mwDelete.setStyleSheet(''' border:0px; ''')
        self.mwDelete.setIcon(QIcon("pic/deleteA.png"))
        self.mwDelete.setIconSize(QSize(70, 50))
        self.mwDelete.clicked.connect(self.delWallet)

        self.mwSaveKey = QPushButton(self)  # type: QPushButton
        self.mwSaveKey.setStyleSheet(''' border:0px; ''')
        self.mwSaveKey.setIcon(QIcon("pic/saveA.png"))
        self.mwSaveKey.setIconSize(QSize(70, 50))
        self.mwSaveKey.clicked.connect(self.savekey)

        self.consend = QPushButton(self)  # type: QPushButton
        self.consend.setStyleSheet(''' border:0px; ''')
        self.consend.setIcon(QIcon("pic/sendA.png"))
        self.consend.setIconSize(QSize(70, 50))
        self.consend.clicked.connect(self.pressbtn1)

        self.conedit = QPushButton(self)  # type: QPushButton
        self.conedit.setStyleSheet(''' border:0px; ''')
        self.conedit.setIcon(QIcon("pic/editA.png"))
        self.conedit.setIconSize(QSize(70, 50))

        self.condelete = QPushButton(self)  # type: QPushButton
        self.condelete.setStyleSheet(''' border:0px; ''')
        self.condelete.setIcon(QIcon("pic/deleteA.png"))
        self.condelete.setIconSize(QSize(70, 50))
        self.condelete.clicked.connect(self.delWallet)

        self.initUI()

    #shift Pages tool btn
    def pressbtn1(self):
        self.ui.mywallet.setIcon(QIcon("pic/mywallet1.png"))
        self.ui.statistic.setIcon(QIcon("pic/statistics0.png"))
        self.ui.message.setIcon(QIcon('pic/message0.png'))
        self.ui.contact.setIcon(QIcon("pic/contact0.png"))
        self.ui.mining.setIcon(QIcon("pic/mining0.png"))
        self.ui.mw.setIcon(QIcon("pic/mw0.png"))
        self.ui.cw.setIcon(QIcon("pic/cw0.png"))
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.NewWalletstacked.setCurrentIndex(0)
        self.ui.lineEdit_8.setText(self.m_wallet.address)
        self.ui.lineEdit_9.setText(self.m_wallet.privateKey)

    def pressbtn2(self):
        self.ui.mywallet.setIcon(QIcon("pic/mywallet0.png"))
        self.ui.statistic.setIcon(QIcon("pic/statistics1.png"))
        self.ui.message.setIcon(QIcon("pic/message0.png"))
        self.ui.contact.setIcon(QIcon("pic/contact0.png"))
        self.ui.mining.setIcon(QIcon("pic/mining0.png"))
        self.ui.mw.setIcon(QIcon("pic/mw0.png"))
        self.ui.cw.setIcon(QIcon("pic/cw0.png"))
        self.ui.stackedWidget.setCurrentIndex(2)

    def pressbtn3(self):
        self.ui.mywallet.setIcon(QIcon("pic/mywallet0.png"))
        self.ui.statistic.setIcon(QIcon("pic/statistics0.png"))
        self.ui.message.setIcon(QIcon("pic/message1.png"))
        self.ui.contact.setIcon(QIcon("pic/contact0.png"))
        self.ui.mining.setIcon(QIcon("pic/mining0.png"))
        self.ui.mw.setIcon(QIcon("pic/mw0.png"))
        self.ui.cw.setIcon(QIcon("pic/cw0.png"))
        self.ui.stackedWidget.setCurrentIndex(3)

    def pressbtn4(self):
        self.ui.mywallet.setIcon(QIcon("pic/mywallet0.png"))
        self.ui.statistic.setIcon(QIcon("pic/statistics0.png"))
        self.ui.message.setIcon(QIcon("pic/message0.png"))
        self.ui.contact.setIcon(QIcon("pic/contact1.png"))
        self.ui.mining.setIcon(QIcon("pic/mining0.png"))
        self.ui.mw.setIcon(QIcon("pic/mw0.png"))
        self.ui.cw.setIcon(QIcon("pic/cw0.png"))
        self.ui.stackedWidget.setCurrentIndex(4)

    def pressbtn5(self):
        self.ui.mywallet.setIcon(QIcon("pic/mywallet0.png"))
        self.ui.statistic.setIcon(QIcon("pic/statistics0.png"))
        self.ui.message.setIcon(QIcon("pic/message0.png"))
        self.ui.contact.setIcon(QIcon("pic/contact0.png"))
        self.ui.mining.setIcon(QIcon("pic/mining1.png"))
        self.ui.mw.setIcon(QIcon("pic/mw0.png"))
        self.ui.cw.setIcon(QIcon("pic/cw0.png"))
        self.ui.stackedWidget.setCurrentIndex(5)

    def pressbtn6(self):
        self.ui.mywallet.setIcon(QIcon("pic/mywallet0.png"))
        self.ui.statistic.setIcon(QIcon("pic/statistics0.png"))
        self.ui.message.setIcon(QIcon("pic/message0.png"))
        self.ui.contact.setIcon(QIcon("pic/contact0.png"))
        self.ui.mining.setIcon(QIcon("pic/mining0.png"))
        self.ui.mw.setIcon(QIcon("pic/mw1.png"))
        self.ui.cw.setIcon(QIcon("pic/cw0.png"))
        self.ui.stackedWidget.setCurrentIndex(6)

    def pressbtn0(self):
        self.ui.mywallet.setIcon(QIcon("pic/mywallet0.png"))
        self.ui.statistic.setIcon(QIcon("pic/statistics0.png"))
        self.ui.message.setIcon(QIcon("pic/message0.png"))
        self.ui.contact.setIcon(QIcon("pic/contact0.png"))
        self.ui.mining.setIcon(QIcon("pic/mining0.png"))
        self.ui.mw.setIcon(QIcon("pic/mw0.png"))
        self.ui.cw.setIcon(QIcon("pic/cw1.png"))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.importstack.setCurrentIndex(0)
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_4.clear()

    def pressCreatNewWallet(self):
        self.ui.importstack.setCurrentIndex(1)
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_4.clear()

    def pressimportbykeystore(self):
        self.ui.importstack.setCurrentIndex(4)
        self.ui.lineEdit_26.clear()
        self.ui.lineEdit_6.clear()

    def presspressimportbyPri(self):
        self.ui.importstack.setCurrentIndex(2)
        self.ui.lineEdit_20.clear()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()


    def presspressimportbyMnem(self):
        self.ui.importstack.setCurrentIndex(3)
        self.ui.lineEdit_15.clear()
        self.ui.lineEdit_16.clear()
        self.ui.lineEdit_17.clear()

    def pressback2import(self):
        self.ui.importstack.setCurrentIndex(0)


    def generateKey(self):
        ret = Core_func.Generate_Three_Key(self.ui.lineEdit_4.text(), self.ui.lineEdit_5.text())
        if ret[0]== 1:
            self.ui.NewWalletstacked.setCurrentIndex(1)
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.lineEdit_21.setText('******')
            self.ui.lineEdit_22.setText(ret[1][0])
            self.ui.lineEdit_23.setText(ret[1][1])
            self.ui.lineEdit_25.setText(ret[1][0][0:10])
            encrypted = ret[1][2]
            #self.m_wallet = Wallet
            self.m_wallet.password = self.ui.lineEdit_4.text()
            self.m_wallet.address = ret[1][0]
            self.m_wallet.privateKey = ret[1][1]
            self.m_wallet.accountname = self.ui.lineEdit_25.text()
            self.addWallet()
            self.ui.lineEdit_8.setText(ret[1][0])
            self.ui.lineEdit_9.setText(ret[1][1])
            DataKeystore = "Data\\Keystore\\"+ret[1][0][2:18]+".keystore"
            fh = open(DataKeystore, "w")
            fh.write(str(encrypted))
            fh.close()
            self.m_wallet.filename = DataKeystore
            self.imgpub = qrcode.make(self.m_wallet.address)
            self.imgpub.save("pic\\public.png")
            self.ui.label_10.setPixmap(QPixmap("pic\\public.png"))
            self.ui.label_10.setAutoFillBackground(1)
            self.imgpri = qrcode.make(ret[1][1])
            self.imgpri.save("pic\\private.png")
            #self.ui.label_10.setPixmap(QPixmap("pic\\private.png"))
            #self.ui.label_10.setAutoFillBackground(1)

    def importsecret(self):
        if  self.ui.lineEdit_18.text() ==  self.ui.lineEdit_19.text():
            enterpri = self.ui.lineEdit_20.text()
            enterpri.strip()
            ret = Core_func.Import_From_Private(enterpri.strip(),self.ui.lineEdit_19.text())
            if ret[0] == 1:
                self.m_wallet.password = self.ui.lineEdit_18.text()
                self.m_wallet.address = ret[1]
                self.m_wallet.privateKey = self.ui.lineEdit_20.text()
                self.m_wallet.accountname = ret[1][0:10]
                encrypted = ret[2]
                DataKeystore = "Data\\Keystore\\" + ret[1][2:18] + ".keystore"
                fh = open(DataKeystore, "w")
                fh.write(str(encrypted))
                fh.close()
                self.m_wallet.filename = DataKeystore
                self.addWallet()
                self.ui.lineEdit_8.setText(ret[1])
                self.ui.lineEdit_9.setText(self.ui.lineEdit_20.text())
                self.imgpub = qrcode.make(self.m_wallet.address)
                self.imgpub.save("pic\\public.png")
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.NewWalletstacked.setCurrentIndex(0)

    def importmnemonic(self):
        ret = Core_func.Import_mnemonic(self.ui.lineEdit_15.text(), self.ui.lineEdit_16.text(), self.ui.lineEdit_17.text())

    def importfile(self):
        dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
        dlg.SetOFNInitialDir('C:')  # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()
        filenames = dlg.GetPathName()
        if len(filenames) != 0:
            string_filename = ""
            for i in range(0, len(filenames)):
                string_filename += str(filenames[i])
            self.ui.lineEdit_26.setText(string_filename)

    def importKetstore(self):
        file = open(self.ui.lineEdit_26.text(), 'r')
        content = file.readline()
        enterpri = self.ui.lineEdit_20.text()
        enterpri.strip()
        ret = Core_func.Import_Keystore(self.ui.lineEdit_6.text(), content)
        if ret[0] ==1:
            self.m_wallet.password = self.ui.lineEdit_6.text()
            self.m_wallet.address = ret[1][0]
            self.m_wallet.privateKey = ret[1][1]
            self.m_wallet.accountname = ret[1][0][0:10]
            encrypted = ret[2]
            DataKeystore = "Data\\Keystore\\" + ret[1][0][2:18] + ".keystore"
            fh = open(DataKeystore, "w")
            fh.write(str(encrypted))
            fh.close()
            self.m_wallet.filename = DataKeystore
            self.addWallet()
            self.ui.lineEdit_8.setText(ret[1][0])
            self.ui.lineEdit_9.setText(ret[1][1])
            self.imgpub = qrcode.make(self.m_wallet.address)
            self.imgpub.save("pic\\public.png")
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.NewWalletstacked.setCurrentIndex(0)

        else:
            print('no')


    def seepassword(self):
        if self.passwordeye == 1:
            self.ui.lineEdit_21.setEchoMode(0)
            self.ui.lineEdit_21.setText(self.m_wallet.password)
            self.ui.pushButton_41.setIcon(QIcon("pic/01.png"))
            self.passwordeye = 0
        else:
            self.ui.lineEdit_21.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_41.setIcon(QIcon("pic/08.png"))
            self.passwordeye = 1

    def seeprivatekey(self):
        if self.privatekeyeye == 1:
            self.ui.lineEdit_9.setEchoMode(0)
            self.ui.lineEdit_9.setText(self.m_wallet.privateKey)
            self.ui.pushButton_35.setIcon(QIcon("pic/01.png"))
            self.privatekeyeye = 0
        else:
            self.ui.lineEdit_9.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_35.setIcon(QIcon("pic/08.png"))
            self.privatekeyeye = 1

    def seeprikey(self):
        if self.prieye == 1:
            self.ui.lineEdit_23.setEchoMode(0)
            self.ui.lineEdit_23.setText(self.m_wallet.privateKey)
            self.ui.pushButton_40.setIcon(QIcon("pic/01.png"))
            self.prieye = 0
            self.ui.label_11.setPixmap(QPixmap("pic\\private.png"))
        else:
            self.ui.lineEdit_23.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_40.setIcon(QIcon("pic/08.png"))
            self.prieye = 1
            self.ui.label_11.setPixmap(QPixmap("pic\\disvispri.png"))

    def addWallet(self):
        ################
        #waiting to add checking same wallet already existed
        ################
        Rcount = self.ui.multWallet.rowCount()
        self.ui.multWallet.setRowCount(Rcount+1)
        newItemAddr = QTableWidgetItem(self.m_wallet.address)
        newItemName = QTableWidgetItem(self.m_wallet.accountname)
        self.ui.multWallet.setItem(Rcount, 1, newItemAddr)
        self.ui.multWallet.setItem(Rcount, 0, newItemName)
        self.ui.multWallet.setCellWidget(Rcount, 2, self.mwOpen)
        self.ui.multWallet.setCellWidget(Rcount, 3, self.mwEdit)
        self.ui.multWallet.setCellWidget(Rcount, 4, self.mwDelete)
        self.ui.multWallet.setCellWidget(Rcount, 5, self.mwSaveKey)

    def delWallet(self):
        ################
        #waiting to add checking same wallet already existed
        ################
        Rcount = self.ui.multWallet.rowCount()
        self.ui.multWallet.setRowCount(Rcount-1)
        os.remove(self.m_wallet.filename)

    def savekey(self):
        ## need to change:copy kfile from data\keystore to specify position
        encrypted = Account.encrypt(self.m_wallet.privateKey, self.m_wallet.password)

        fsave_keystore = QFileDialog.getSaveFileName(self, 'Save Your Keystore File', '.','keystore(*.keystore)')
        if fsave_keystore[0]:
            file_save_keystore = open(fsave_keystore[0], 'w')
            with file_save_keystore:
                data = file_save_keystore.write(json.dumps(encrypted))

    def savename(self):
        self.m_wallet.accountname = self.ui.lineEdit_25.text()

    def copyPublicKey(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(self.m_wallet.address)

    def copymnemword(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(self.m_wallet.mnem)

    def toreddit(self):
        webbrowser.open('https://www.reddit.com/r/waltonchain/')

    def totwitter(self):
        webbrowser.open('https://twitter.com/Waltonchain')

    def totme(self):
        webbrowser.open('https://t.me/waltonchain_en')

    def tostack(self):
        webbrowser.open('https://join.slack.com/t/waltonchain/shared_invite/enQtMjgxMDcxNzU5MDEwLWI1ZTc3MDZlNmI4ZjA1YjhiMDEzN2VlZmY2M2EzNmM4Yjg1NjFjYjlmNTcxOGVlMGRiNWE2M2NlYTg2MWNmNWQ')

    def seepass1(self):
        if self.pass1eye == 1:
            PASS = self.ui.lineEdit_4.text()
            self.ui.lineEdit_4.setEchoMode(0)
            self.ui.lineEdit_4.setText(PASS)
            self.ui.turn2visible1.setIcon(QIcon("pic/01.png"))
            self.pass1eye = 0
        else:
            self.ui.lineEdit_4.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1.setIcon(QIcon("pic/02.png"))
            self.pass1eye = 1
    def seepass2(self):
        if self.pass2eye == 1:
            PASS = self.ui.lineEdit_5.text()
            self.ui.lineEdit_5.setEchoMode(0)
            self.ui.lineEdit_5.setText(PASS)
            self.ui.turn2visible2.setIcon(QIcon("pic/01.png"))
            self.pass2eye = 0
        else:
            self.ui.lineEdit_5.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible2.setIcon(QIcon("pic/02.png"))
            self.pass2eye = 1

    def seepri1(self):
        if self.pri1eye == 1:
            #time.sleep(5)
            PASS = self.ui.lineEdit_20.text()
            self.ui.lineEdit_20.setEchoMode(0)
            self.ui.lineEdit_20.setText(PASS)
            self.ui.turn2visible1_9.setIcon(QIcon("pic/01.png"))
            self.pri1eye = 0
        else:
            self.ui.lineEdit_20.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_9.setIcon(QIcon("pic/02.png"))
            self.pri1eye = 1
    def seephrs1(self):
        if self.phrs1eye == 1:
            PASS = self.ui.lineEdit_18.text()
            self.ui.lineEdit_18.setEchoMode(0)
            self.ui.lineEdit_18.setText(PASS)
            self.ui.turn2visible1_8.setIcon(QIcon("pic/01.png"))
            self.phrs1eye = 0
        else:
            self.ui.lineEdit_18.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_8.setIcon(QIcon("pic/02.png"))
            self.phrs1eye = 1
    def seephrs2(self):
        if self.phrs1eye == 1:
            PASS = self.ui.lineEdit_19.text()
            self.ui.lineEdit_19.setEchoMode(0)
            self.ui.lineEdit_19.setText(PASS)
            self.ui.turn2visible2_5.setIcon(QIcon("pic/01.png"))
            self.phrs1eye = 0
        else:
            self.ui.lineEdit_19.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible2_5.setIcon(QIcon("pic/02.png"))
            self.phrs1eye = 1
    def seepassK(self):
        if self.passKeye == 1:
            PASS = self.ui.lineEdit_6.text()
            self.ui.lineEdit_6.setEchoMode(0)
            self.ui.lineEdit_6.setText(PASS)
            self.ui.turn2visible1_2.setIcon(QIcon("pic/01.png"))
            self.passKeye = 0
        else:
            self.ui.lineEdit_6.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_2.setIcon(QIcon("pic/02.png"))
            self.passKeye = 1
    def seemnem1(self):
        if self.mnemeye == 1:
            PASS = self.ui.lineEdit_17.text()
            self.ui.lineEdit_17.setEchoMode(0)
            self.ui.lineEdit_17.setText(PASS)
            self.ui.turn2visible1_7.setIcon(QIcon("pic/01.png"))
            self.mnemeye = 0
        else:
            self.ui.lineEdit_17.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_7.setIcon(QIcon("pic/02.png"))
            self.mnemeye = 1
    def seephrm1(self):
        if self.phrm1eye == 1:
            PASS = self.ui.lineEdit_15.text()
            self.ui.lineEdit_15.setEchoMode(0)
            self.ui.lineEdit_15.setText(PASS)
            self.ui.turn2visible1_6.setIcon(QIcon("pic/01.png"))
            self.phrm1eye = 0
        else:
            self.ui.lineEdit_15.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_6.setIcon(QIcon("pic/02.png"))
            self.phrm1eye = 1
    def seephrm2(self):
        if self.phrm2eye == 1:
            PASS = self.ui.lineEdit_16.text()
            self.ui.lineEdit_16.setEchoMode(0)
            self.ui.lineEdit_16.setText(PASS)
            self.ui.turn2visible2_4.setIcon(QIcon("pic/01.png"))
            self.phrm2eye = 0
        else:
            self.ui.lineEdit_16.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible2_4.setIcon(QIcon("pic/02.png"))
            self.phrm2eye = 1
    def purple2black(self):
        self.ui.LogMessage.setStyleSheet("color:#000000")
        self.ui.LogMessage.setSelectionBehavior(Core_func.QTableWidget.SelectRows)
        self.ui.LogMessage.horizontalHeader().setVisible(0)
        self.ui.LogMessage.verticalHeader().setVisible(0)
        self.ui.LogMessage.setShowGrid(0)
        self.ui.LogMessage.horizontalHeader().setStretchLastSection(1)
        self.ui.LogMessage.verticalHeader().setDefaultSectionSize(57)
        self.ui.LogMessage.setColumnWidth(0, 150)  # 将设置第1列的单元格成20宽度
        self.ui.LogMessage.setColumnWidth(1, 150)  # 将设置第2列的单元格成30宽度
        self.ui.LogMessage.setColumnWidth(2, 100)  # 将设置第3列的单元格成50宽度
        self.ui.LogMessage.setFrameShape(QFrame.NoFrame)  # 表格无边框
        self.ui.LogMessage.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.ui.LogMessage.setFocusPolicy(Qt.NoFocus)  # 无选中虚线框
        self.ui.LogMessage.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")
    def startmining(self):
        if self.startstop == 1:
            self.startstop = 0
            self.ui.pushButton_30.setStyleSheet("border-width: 1px;"
                                                "border-color: rgb(170, 0, 255);"
                                                "background-color: rgb(170, 0, 255);"
                                                "color: rgb(255, 255, 255);"
                                                "border-radius:20px;"
                                                "border-style:solid; ")
            self.ui.pushButton_30.setText('Stop Mining')


            self.ui.radioButton.setEnabled(0)
            self.ui.radioButton_2.setEnabled(0)
            self.ui.radioButton_3.setEnabled(0)
            self.ui.radioButton_4.setEnabled(0)
            self.ui.radioButton_5.setEnabled(0)
            self.ui.radioButton_6.setEnabled(0)
            self.ui.horizontalSlider.setEnabled(0)
            if self.cpumode == 1:
                print('cpu')
            else:
                print('gpu')
        else:
            self.startstop = 1
            self.ui.pushButton_30.setStyleSheet("border-width: 1px;"
                                                "border-color: rgb(170, 0, 255);"
                                                "background-color: rgb(255, 255, 255);"
                                                "color: rgb(170, 0, 255);"
                                                "border-radius:20px;"
                                                "border-style:solid; ")
            self.ui.pushButton_30.setText('Start Mining')
            self.ui.radioButton.setEnabled(1)
            self.ui.radioButton_2.setEnabled(1)
            self.ui.radioButton_3.setEnabled(1)
            self.ui.radioButton_4.setEnabled(1)
            self.ui.radioButton_5.setEnabled(1)
            self.ui.radioButton_6.setEnabled(1)
            self.ui.horizontalSlider.setEnabled(1)
    def changecpu(self):
        self.ui.radioButton_3.setEnabled(1)
        self.ui.radioButton_4.setEnabled(1)
        self.ui.radioButton_5.setEnabled(1)
        self.ui.radioButton_6.setEnabled(1)
        self.ui.horizontalSlider.setEnabled(1)
        self.cpumode = 1

    def changegpu(self):
        self.ui.radioButton_3.setEnabled(0)
        self.ui.radioButton_4.setEnabled(0)
        self.ui.radioButton_5.setEnabled(0)
        self.ui.radioButton_6.setEnabled(0)
        self.ui.horizontalSlider.setEnabled(0)
        self.cpumode = 0

    def changereg(self):
        self.cpures = ''

    def changefast(self):
        self.cpures = ''

    def changesfast(self):
        self.cpures = ''

    def changeefast(self):
        self.cpures = ''

    def operate(self):
        self.refresh()

    def refresh(self):
        print('time out')

    def initUI(self):
        '显示窗口'
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        self.timer.start(20000)  # 设置计时间隔并启动

        btnminHisrefresh = self.ui.pushButton_45
        btnminHisrefresh.clicked.connect(self.refresh)
        btntraHisrefresh = self.ui.pushButton_46
        btntraHisrefresh.clicked.connect(self.refresh)

        self.m_wallet = Wallet
        #Page of Create Wallet
        stackedW = self.ui.stackedWidget
        btncnw = self.ui.creat_new_wallet
        btncnw.clicked.connect(self.pressCreatNewWallet)
        btnimportKeys = self.ui.import_Keystore
        btnimportKeys.clicked.connect(self.pressimportbykeystore)
        btnimportPri = self.ui.import_Pri
        btnimportPri.clicked.connect(self.presspressimportbyPri)
        btnimportMnem = self.ui.import_MP
        btnimportMnem.clicked.connect(self.presspressimportbyMnem)
        btnmywallet = self.ui.mw_2
        btnmywallet.clicked.connect(self.pressbtn1)

        btnback1 = self.ui.back_to_import
        btnback1.clicked.connect(self.pressback2import)
        btnback2 = self.ui.back_to_import_2
        btnback2.clicked.connect(self.pressback2import)
        btnback3 = self.ui.back_to_import_6
        btnback3.clicked.connect(self.pressback2import)
        btnback4 = self.ui.back_to_import_7
        btnback4.clicked.connect(self.pressback2import)

        btngenerate = self.ui.Gene_Key
        btngenerate.clicked.connect(lambda :self.generateKey())
        btnloginpri = self.ui.login_pri
        btnloginpri.clicked.connect(lambda :self.importsecret())
        btnloginmnem = self.ui.login_mnem
        btnloginmnem.clicked.connect(lambda :self.importmnemonic())
        btnimportfile = self.ui.import_Keystore_2
        btnimportfile.clicked.connect(self.importfile)
        #enter password
        btntosee1 = self.ui.turn2visible1
        btntosee1.clicked.connect(self.seepass1)
        self.pass1eye = 1
        btntosee2 = self.ui.turn2visible2
        btntosee2.clicked.connect(self.seepass2)
        self.pass2eye = 1
        #enter secret
        btntosee3 = self.ui.turn2visible1_9
        btntosee3.clicked.connect(self.seepri1)
        self.pri1eye = 1
        btntosee4 = self.ui.turn2visible1_8
        btntosee4.clicked.connect(self.seephrs1)
        self.phrs1eye = 1
        btntosee5 = self.ui.turn2visible2_5
        btntosee5.clicked.connect(self.seephrs2)
        self.phrs2eye = 1

        #enter mnem
        btntosee6 = self.ui.turn2visible1_7
        btntosee6.clicked.connect(self.seemnem1)
        self.mnemeye = 1
        btntosee7 = self.ui.turn2visible1_6
        btntosee7.clicked.connect(self.seephrm1)
        self.phrm1eye = 1
        btntosee8 = self.ui.turn2visible2_4
        btntosee8.clicked.connect(self.seephrm2)
        self.phrm2eye = 1

        #enter keystore
        btntosee9 = self.ui.turn2visible1_2
        btntosee9.clicked.connect(self.seepassK)
        self.passKeye = 1

        btnloginkeys = self.ui.login_keys

        btnloginkeys.clicked.connect(lambda :self.importKetstore())

        self.ui.importstack.setCurrentIndex(0)


        #all pages shift
        self.ui.NewWalletstacked.setCurrentIndex(0)


        #all pages shift
        stackedW.setCurrentIndex(0)
        btn1 = self.ui.mywallet
        btn1.clicked.connect(self.pressbtn1)
        btn2 = self.ui.statistic
        btn2.clicked.connect(self.pressbtn2)
        btn3 = self.ui.message
        btn3.clicked.connect(self.pressbtn3)
        btn4 = self.ui.contact
        btn4.clicked.connect(self.pressbtn4)
        btn5 = self.ui.mining
        btn5.clicked.connect(self.pressbtn5)
        btn6 = self.ui.mw
        btn6.clicked.connect(self.pressbtn6)
        btn0 = self.ui.cw
        btn0.clicked.connect(self.pressbtn0)

        #new wallet page
        btneye1 = self.ui.pushButton_41
        self.passwordeye = 1
        btneye1.clicked.connect(self.seepassword)
        btnsavekey = self.ui.SaveKey
        btnsavekey.clicked.connect(self.savekey)
        btnsavename = self.ui.SaveName
        btnsavename.clicked.connect(self.savename)

        btneye2 = self.ui.pushButton_40
        self.prieye = 1
        btneye2.clicked.connect(self.seeprikey)

        btncopy1 = self.ui.pushButton_39
        btncopy1.clicked.connect(self.copyPublicKey)
        btncopy2 = self.ui.pushButton_42
        btncopy2.clicked.connect(self.copymnemword)
        #*4

        #my wallet page
        btneyepri = self.ui.pushButton_35
        self.privatekeyeye = 1
        btneyepri.clicked.connect(self.seeprivatekey)
        btncopypub = self.ui.pushButton_34
        btncopypub.clicked.connect(self.copyPublicKey)
        btnreb = self.ui.pushButton_6
        btnreb.clicked.connect(self.toreddit)
        btntwi = self.ui.pushButton_7
        btntwi.clicked.connect(self.totwitter)
        btntme = self.ui.pushButton_5
        btntme.clicked.connect(self.totme)
        btnsta = self.ui.pushButton_8
        btnsta.clicked.connect(self.tostack)

        #Multiple Wallet page
        btn2create = self.ui.pushButton_32
        btn2create.clicked.connect(self.pressbtn0)
        btn2create1 = self.ui.pushButton_33
        btn2create1.clicked.connect(self.pressbtn0)

        # Message page
        btnMark = self.ui.pushButton_37
        btnMark.clicked.connect(self.purple2black)

        #mining page
        btnrebm = self.ui.pushButton_12
        btnrebm.clicked.connect(self.toreddit)
        btntwim = self.ui.pushButton_13
        btntwim.clicked.connect(self.totwitter)
        btntmem = self.ui.pushButton_14
        btntmem.clicked.connect(self.totme)
        btnstam = self.ui.pushButton_11
        btnstam.clicked.connect(self.tostack)

        btnmining = self.ui.pushButton_30
        self.startstop = 1
        btnmining.clicked.connect(self.startmining)

        self.cpumode = 1


        self.ui.radioButton.toggle()
        self.ui.radioButton.toggled.connect(self.changecpu)
        self.ui.radioButton_2.toggle()
        self.ui.radioButton_2.toggled.connect(self.changegpu)
        self.ui.radioButton_3.toggle()
        self.ui.radioButton_3.toggled.connect(self.changereg)
        self.ui.radioButton_4.toggle()
        self.ui.radioButton_4.toggled.connect(self.changefast)
        self.ui.radioButton_5.toggle()
        self.ui.radioButton_5.toggled.connect(self.changesfast)
        self.ui.radioButton_6.toggle()
        self.ui.radioButton_6.toggled.connect(self.changeefast)


        #statistics page
        btnrebs = self.ui.pushButton_17
        btnrebs.clicked.connect(self.toreddit)
        btntwis = self.ui.pushButton_16
        btntwis.clicked.connect(self.totwitter)
        btntmes = self.ui.pushButton_18
        btntmes.clicked.connect(self.totme)
        btnstas = self.ui.pushButton_15
        btnstas.clicked.connect(self.tostack)

        self.ui.LogMessage.setStyleSheet("color:#aa00ff")
        self.ui.LogMessage.setSelectionBehavior(Core_func.QTableWidget.SelectRows)
        self.ui.LogMessage.horizontalHeader().setVisible(0)
        self.ui.LogMessage.verticalHeader().setVisible(0)
        self.ui.LogMessage.setShowGrid(0)
        self.ui.LogMessage.horizontalHeader().setStretchLastSection(1)
        self.ui.LogMessage.verticalHeader().setDefaultSectionSize(57)
        self.ui.LogMessage.setColumnWidth(0, 150)  # 将设置第1列的单元格成20宽度
        self.ui.LogMessage.setColumnWidth(1, 150)  # 将设置第2列的单元格成30宽度
        self.ui.LogMessage.setColumnWidth(2, 100)  # 将设置第3列的单元格成50宽度
        self.ui.LogMessage.setFrameShape(QFrame.NoFrame)  # 表格无边框
        self.ui.LogMessage.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.ui.LogMessage.setFocusPolicy(Qt.NoFocus)  # 无选中虚线框
        self.ui.LogMessage.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        self.ui.ContactsT.horizontalHeader().setVisible(0)
        self.ui.ContactsT.verticalHeader().setVisible(0)
        self.ui.ContactsT.setShowGrid(0)
        self.ui.ContactsT.horizontalHeader().setStretchLastSection(1)
        self.ui.ContactsT.verticalHeader().setDefaultSectionSize(45)
        self.ui.ContactsT.setColumnWidth(0, 200)  # 将设置第1列的单元格成20宽度
        self.ui.ContactsT.setColumnWidth(1, 310)  # 将设置第2列的单元格成30宽度
        self.ui.ContactsT.setColumnWidth(2, 100)  # 将设置第3列的单元格成50宽度
        self.ui.ContactsT.setColumnWidth(3, 100)  # 将设置第2列的单元格成30宽度
        self.ui.ContactsT.setColumnWidth(4, 100)
        self.ui.ContactsT.setFrameShape(QFrame.Box)  # 表格无边框
        self.ui.ContactsT.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.ui.ContactsT.setSelectionMode(QAbstractItemView.NoSelection)  # 单元不可选
        self.ui.ContactsT.setFocusPolicy(Qt.NoFocus)  # 无选中虚线框
        self.ui.ContactsT.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        self.ui.TransactionHistory.horizontalHeader().setVisible(0)
        self.ui.TransactionHistory.verticalHeader().setVisible(0)
        self.ui.TransactionHistory.setShowGrid(0)
        self.ui.TransactionHistory.horizontalHeader().setStretchLastSection(1)
        self.ui.TransactionHistory.verticalHeader().setDefaultSectionSize(40)
        self.ui.TransactionHistory.setColumnWidth(0, 100)  # 将设置第1列的单元格成20宽度
        self.ui.TransactionHistory.setColumnWidth(1, 300)  # 将设置第2列的单元格成30宽度
        self.ui.TransactionHistory.setColumnWidth(2, 105)  # 将设置第3列的单元格成50宽度
        self.ui.TransactionHistory.setColumnWidth(3, 105)  # 将设置第2列的单元格成30宽度
        self.ui.TransactionHistory.setFrameShape(QFrame.Box)  # 表格无边框
        self.ui.TransactionHistory.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.ui.TransactionHistory.setSelectionMode(QAbstractItemView.NoSelection)  # 单元不可选
        self.ui.TransactionHistory.setFocusPolicy(Qt.NoFocus)  # 无选中虚线框
        self.ui.TransactionHistory.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        self.ui.miningHistory.horizontalHeader().setVisible(0)
        self.ui.miningHistory.verticalHeader().setVisible(0)
        self.ui.miningHistory.setShowGrid(0)
        self.ui.miningHistory.horizontalHeader().setStretchLastSection(1)
        self.ui.miningHistory.horizontalHeader().setDefaultSectionSize(200)
        self.ui.miningHistory.verticalHeader().setDefaultSectionSize(40)
        self.ui.miningHistory.setFrameShape(QFrame.Box)  # 表格无边框
        self.ui.miningHistory.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.ui.miningHistory.setSelectionMode(QAbstractItemView.NoSelection)  # 单元不可选
        self.ui.miningHistory.setFocusPolicy(Qt.NoFocus)  # 无选中虚线框
        self.ui.miningHistory.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        self.ui.multWallet.horizontalHeader().setVisible(0)
        self.ui.multWallet.verticalHeader().setVisible(0)
        self.ui.multWallet.setShowGrid(0)
        self.ui.multWallet.horizontalHeader().setStretchLastSection(1)


        # self.ui.multWallet.horizontalHeader().setDefaultSectionSize(0,180)
        self.ui.multWallet.setColumnWidth(0, 150)  # 将设置第1列的单元格成20宽度
        self.ui.multWallet.setColumnWidth(1, 300)  # 将设置第2列的单元格成30宽度
        self.ui.multWallet.setColumnWidth(2, 90)  # 将设置第3列的单元格成50宽度
        self.ui.multWallet.setColumnWidth(3, 90)  # 将设置第2列的单元格成30宽度
        self.ui.multWallet.setColumnWidth(4, 90)  # 将设置第3列的单元格成50宽度
        self.ui.multWallet.setColumnWidth(5, 90)  # 将设置第2列的单元格成30宽度

        self.ui.multWallet.verticalHeader().setDefaultSectionSize(45)
        self.ui.multWallet.setFrameShape(QFrame.Box)  # 表格无边框
        self.ui.multWallet.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.ui.multWallet.setSelectionMode(QAbstractItemView.NoSelection)  # 单元不可选
        self.ui.multWallet.setFocusPolicy(Qt.NoFocus)  # 无选中虚线框
        self.ui.multWallet.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")






        #self.show()  # show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。
class Wallet:
    password = ''
    privateKey = ''
    mnem = ''
    address = ''
    accountname = ''
    filename = ''

class Transaction:
    rawTransaction = ''
    status = ''
    value = ''
    fromaddr = ''
    toaddr = ''
    Type = ''
    Gas = ''
    Gasprice = ''
    Blocknumber = ''
    Time = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sendform = sendform()
    recieveform = recieveform()
    mulwalform =mulwalform()
    pubaddrForm = pubaddrForm()
    newcontactform = newcontactform()
    messform =messform()
    #s = Warning_Form.SecondWindow()
    #ex.ui.cw.clicked.connect(s.handle_click)
    ex.show()
    ex.ui.pushButton_9.clicked.connect(sendform.show_w2)
    ex.ui.pushButton_10.clicked.connect(recieveform.show_w2)
    ex.ui.pushButton_36.clicked.connect(pubaddrForm.show_w2)
    ex.ui.pushButton_38.clicked.connect(newcontactform.show_w2)
    ex.ui.LogMessage.itemClicked.connect(messform.show_w2)
    ex.mwEdit.clicked.connect(mulwalform.show_w2)
    sys.exit(app.exec_())
