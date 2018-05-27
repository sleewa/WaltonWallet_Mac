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
from PublishForm import Ui_publishForm
from AccountForm import Ui_AccountForm
import matplotlib
import datetime
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键

    def __init__(self, parent=None, width=5, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=70)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def test(self,addr):
        if addr != '':
            ret3 = Core_func.getTransactionRecord_day(addr, '30')

            y = []
            x = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,
                 1]
            for i in range(len(ret3[1])):
                y.append(int(ret3[1][i]['history_balance']))
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()

            return ret3[1][0]['history_balance']

        else:
            y = [0]
            x = [0]
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()

            return 0


    def testM(self):
        y=[]
        x = [30,29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ret3 = Core_func.getTokenMarket()
        if ret3[0] == 1:
            for i in range(len(ret3[1])):
                y.append(int(ret3[1][i]['TokenPriceUSD']))
            self.axes.plot(x, y,'r-',1)
            self.axes.set_axis_off()
            return ret3[1][0]['TokenPriceUSD']

    def testB(self,addr):
        if addr != '':
            ret3 = Core_func.getTransactionRecord_day(addr, '30')

            y = []
            x = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,
                 1]
            for i in range(len(ret3[1])):
                y.append(int(ret3[1][i]['history_balance']))
            #y.append(0)
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()
            return  ret3[1][i]['history_balance']
        else:
            y = [0]
            x = [0]
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()
            return  0

    def testR(self,addr):
        if addr != '':
            ret3 = Core_func.getMiningRecord(addr)
            if len(ret3[1])!=0:
                y = []
                x = []
                for i in range(len(ret3[1])):
                    x.append(i)
                    y.append(int(ret3[1][i]['totol_reward']))
                #y.append(0)
                #x.append(0)

                #print(ret3[1][2]['timestamp'][0:10])
                self.axes.plot(x, y, 'r-', 1)
                self.axes.set_axis_off()
                return ret3[1][i]['totol_reward']
            else:
                y = [0]
                x = [0]
                self.axes.plot(x, y, 'r-', 1)
                self.axes.set_axis_off()
                return 0
        else:
            y = [0]
            x = [0]
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()
            return 0




class publishform(QWidget, Ui_publishForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_publishForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnconfirm = self.ui.pushButton_9
        btnconfirm.clicked.connect(self.closeform)

    def show_w2(self,str):  # 显示窗体2
        self.ui.textEdit.setText(str)
        self.show()



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

class accountform(QWidget, Ui_AccountForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AccountForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)

        self.ui.Account.horizontalHeader().setVisible(0)
        self.ui.Account.verticalHeader().setVisible(0)
        self.ui.Account.setShowGrid(0)
        self.ui.Account.horizontalHeader().setStretchLastSection(1)
        self.ui.Account.verticalHeader().setDefaultSectionSize(45)
        self.ui.Account.setColumnWidth(0, 200)  # 将设置第1列的单元格成20宽度
        self.ui.Account.setColumnWidth(1, 310)  # 将设置第2列的单元格成30宽度

        self.ui.Account.setFrameShape(QFrame.NoFrame)  # 表格无边框
        self.ui.Account.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.ui.Account.setSelectionMode(QAbstractItemView.NoSelection)  # 单元不可选
        self.ui.Account.setFocusPolicy(Qt.NoFocus)  # 无选中虚线框
        self.ui.Account.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")



        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnconfirm = self.ui.pushButton_9
        btnconfirm.clicked.connect(self.closeform)

    def show_w2(self):  # 显示窗体2

        self.show()



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

    def show_w2(self,QTableWidgetItem):  # 显示窗体2
        ind = Core_func.QTableWidget.indexFromItem(ex.ui.LogMessage,QTableWidgetItem)
        #rownum = ex.ui.LogMessage.selectedItems().index
        print(ind.data())
        print(ind.data().split('tx_hash')[1][1:])
        ret = Core_func.getTransactionInfo(ind.data().split('tx_hash')[1][1:])
        self.ui.lineEdit_12.setText(str(ret[1][0]['blockNumber']))
        self.ui.lineEdit_11.setText(ret[1][0]['timestamp'])
        self.ui.lineEdit_9.setText(str(ret[1][0]['gas']))
        self.ui.lineEdit_10.setText(str(ret[1][0]['gasPrice']))
        self.ui.lineEdit_8.setText(str(ret[1][0]['addressTo']))
        self.ui.lineEdit_7.setText(str(ret[1][0]['addressFrom']))
        self.ui.lineEdit_6.setText(str(ret[1][0]['value']))
        self.ui.textEdit.setText(str(ret[1][0]['tx_hash']))
        self.show()


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
        print(Rcount)
        ex.ui.ContactsT.setRowCount(Rcount + 1)
        newItemAddr = QTableWidgetItem(self.ui.lineEdit_6.text())
        newItemName = QTableWidgetItem(self.ui.lineEdit_7.text())

        ex.ui.ContactsT.setItem(Rcount, 1, newItemAddr)
        ex.ui.ContactsT.setItem(Rcount, 0, newItemName)
        ex.ui.ContactsT.setCellWidget(Rcount, 2, ex.consend)
        ex.ui.ContactsT.setCellWidget(Rcount, 3, ex.conedit)
        ex.ui.ContactsT.setCellWidget(Rcount, 4, ex.condelete)
        #print(ex.ui.ContactsT.currentIndex())
        #self.accountform.ui.Account.setItem(Rcount, 1, newItemAddr)
        #self.accountform.ui.Account.setItem(Rcount, 0, newItemName)


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
        self.accountform =accountform()
        self.publishform = publishform()
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsend = self.ui.pushButton_9
        btnsend.clicked.connect(self.showenterphrase)
        btncont = self.ui.pushButton_34
        btncont.clicked.connect(self.accountform.show_w2)

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
        if len(ex.m_wallet.address) <= 40 :
            self.publishform.show_w2('Please Choose Wallet')
        else:
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
            self.Trans.txhash = '0x36775097df4ed6429dbe31fc56119a66f8c3dfcfda46792f4982117a90521f0a'#ret[1]
            #tx_details = Core_func.getTransactionInfo(self.Trans.txhash)
            #self.Trans.Blocknumber = tx_details['blockNumber']
            #self.Trans.timestamp = tx_details['timestamp']
            self.Trans.toaddr = self.ui.lineEdit_7.text().strip()
            self.Trans.fromaddr = ex.m_wallet.address
            Rcount = ex.ui.TransactionHistory.rowCount()
            ex.ui.TransactionHistory.setRowCount(Rcount + 1)
            newItemTime = QTableWidgetItem(datetime.datetime.now().strftime('%Y-%m-%d'))
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
            newItemTime = QTableWidgetItem(datetime.datetime.now().strftime('%Y-%m-%d'))
            newItemContent = QTableWidgetItem('From:'+self.Trans.fromaddr +'\n'+ 'To:'+self.Trans.toaddr +'\n'+ 'Value:'+self.Trans.value +'                                                                                                                         '+'\n'+ 'tx_hash:'+self.Trans.txhash)
            newItemType = QTableWidgetItem(self.Trans.Type)
            ex.ui.LogMessage.setItem(Rcount, 0, newItemType)
            ex.ui.LogMessage.setItem(Rcount, 1, newItemTime)
            ex.ui.LogMessage.setItem(Rcount, 2, newItemContent)
            self.publishform.show_w2('transaction successfully')
            self.closeform()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_6.clear()


        else:
            self.publishform.show_w2('transaction failed')


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


    def buttonsdef(self):
        mwOpen = QPushButton(self)  # type: QPushButton
        mwOpen.setStyleSheet(''' border:0px; ''')
        mwOpen.setIcon(QIcon("pic/open1233.png"))
        mwOpen.setIconSize(QSize(70, 50))
        mwOpen.clicked.connect(self.pressbtn1)

        mwEdit = QPushButton(self)  # type: QPushButton
        mwEdit.setStyleSheet(''' border:0px; ''')
        mwEdit.setIcon(QIcon("pic/editA.png"))
        mwEdit.setIconSize(QSize(70, 50))

        mwDelete = QPushButton(self)  # type: QPushButton
        mwDelete.setStyleSheet(''' border:0px; ''')
        mwDelete.setIcon(QIcon("pic/deleteA.png"))
        mwDelete.setIconSize(QSize(70, 50))
        mwDelete.clicked.connect(self.delWallet)

        mwSaveKey = QPushButton(self)  # type: QPushButton
        mwSaveKey.setStyleSheet(''' border:0px; ''')
        mwSaveKey.setIcon(QIcon("pic/saveA.png"))
        mwSaveKey.setIconSize(QSize(70, 50))
        mwSaveKey.clicked.connect(self.savekey)

        consend = QPushButton(self)  # type: QPushButton
        consend.setStyleSheet(''' border:0px; ''')
        consend.setIcon(QIcon("pic/sendA.png"))
        consend.setIconSize(QSize(70, 50))
        consend.clicked.connect(self.pressbtn1)

        conedit = QPushButton(self)  # type: QPushButton
        conedit.setStyleSheet(''' border:0px; ''')
        conedit.setIcon(QIcon("pic/editA.png"))
        conedit.setIconSize(QSize(70, 50))

        condelete = QPushButton(self)  # type: QPushButton
        condelete.setStyleSheet(''' border:0px; ''')
        condelete.setIcon(QIcon("pic/deleteA.png"))
        condelete.setIconSize(QSize(70, 50))
        condelete.clicked.connect(self.delWallet)

        return (mwOpen,mwEdit,mwDelete,mwSaveKey)
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
        if len(self.ui.lineEdit_4.text()) < 6:
            self.publishform.show_w2('Please enter at least 6 characters')
        elif self.ui.lineEdit_4.text() != self.ui.lineEdit_5.text():
            self.publishform.show_w2('Passphrases do not match')
        else:
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
            else:
                self.publishform.show_w2('error')

    def importsecret(self):
        if  self.ui.lineEdit_18.text() ==  self.ui.lineEdit_19.text():
            enterpri = self.ui.lineEdit_20.text()
            enterpri.strip()
            if len(enterpri.strip())== 64:
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
                else:
                    self.publishform.show_w2('Please enter right password')
            else:
                self.publishform.show_w2('Private Key is illegal')
        else:
            self.publishform.show_w2('Passphrases do not match')

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
        else:
            self.publishform.show_w2('Please choose a right Keystore')

    def importKetstore(self):
        file = open(self.ui.lineEdit_26.text(), 'r')
        content = file.readline()
        if content[-5:] == 'store':
            enterpri = self.ui.lineEdit_20.text()
            enterpri.strip()
            if len(enterpri.strip()) < 6:
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
                    self.publishform.show_w2('Please enter right password')
            else:
                self.publishform.show_w2('Please enter at least 6 characters')
        else:
            self.publishform.show_w2('Please choose a right Keystore')

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
        #ret = self.buttonsdef()
        #self.ui.multWallet.setCellWidget(Rcount, 2, ret[0])
        self.ui.multWallet.setCellWidget(Rcount, 3, self.mwEdit)
        self.ui.multWallet.setCellWidget(Rcount, 4, self.mwDelete)
        self.ui.multWallet.setCellWidget(Rcount, 5, self.mwSaveKey)
        self.initchart()

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
        Rcount = self.ui.multWallet.rowCount()
        self.ui.multWallet.setRowCount(Rcount )
        newItemAddr = QTableWidgetItem(self.m_wallet.address)
        newItemName = QTableWidgetItem(self.m_wallet.accountname)
        self.ui.multWallet.setItem(Rcount-1, 1, newItemAddr)
        self.ui.multWallet.setItem(Rcount-1, 0, newItemName)
        self.ui.multWallet.setCellWidget(Rcount-1, 2, self.mwOpen)
        self.ui.multWallet.setCellWidget(Rcount-1, 3, self.mwEdit)
        self.ui.multWallet.setCellWidget(Rcount-1, 4, self.mwDelete)
        self.ui.multWallet.setCellWidget(Rcount-1, 5, self.mwSaveKey)

        self.publishform.show_w2('Saved successfully')

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
            ######################################
            self.miningtatus = 1
            ######################################
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
            ######################################
            self.miningtatus = 0
            ######################################
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
        #self.refresh()
        print('tick')

    def refresh(self):
        '''
        coun = self.ui.TransactionHistory.rowCount()#self.m_wallet.address
        #tx_hashlist = str(ret[1]).split('tx_hash')
        if self.sendform.Trans.status == 'Submitted':
            ret = Core_func.getTransactionRecord(self.m_wallet.address)
            for i in range(len(ret[1])):
                print(self.sendform.Trans.txhash)
                print(ret[1][i]['tx_hash'])

                if self.sendform.Trans.txhash == ret[1][i]['tx_hash']:
                    self.sendform.Trans.status = '0/12'
                    self.sendform.Trans.blocknumber = int(ret[1][i]['blockNumber'])
        elif self.sendform.Trans.status != 'Succeed':
            RET = Core_func.getLatestBlock()
            if RET > self.sendform.Trans.blocknumber :
                if RET - self.sendform.Trans.blocknumber <12:
                    self.sendform.Trans.status = str(RET-self.sendform.Trans.blocknumber)+'/12'
                else:
                    self.sendform.Trans.status = 'Succeed'
        #print(ret[1][1]['tx_hash'])
        newItemStatus = QTableWidgetItem(self.sendform.Trans.status)
        self.ui.TransactionHistory.setItem(coun, 2, newItemStatus)

        '''
        """
        if self.m_wallet.address!='':
            ret3 = Core_func.getTransactionRecord_day(self.m_wallet.address, '20')
            self.ui.TransactionHistory.setRowCount(0)
            for i in range(len(ret3[1])):
                Rcount = self.ui.TransactionHistory.rowCount()
                self.ui.TransactionHistory.setRowCount(Rcount + 1)
                newItemtime = QTableWidgetItem(ret3[1][i]['timestamp'][0:10])
                newItemblock = QTableWidgetItem(str(ret3[1][i]['blockNumer']))
                newItemreward = QTableWidgetItem(str(ret3[1][i]['totol_reward']) + 'WTCT')
                newItemreward = QTableWidgetItem(str(ret3[1][i]['totol_reward']) + 'WTCT')

                self.ui.TransactionHistory.setItem(Rcount, 0, newItemtime)
                self.ui.TransactionHistory.setItem(Rcount, 1, newItemblock)
                self.ui.TransactionHistory.setItem(Rcount, 2, newItemreward)
                self.ui.TransactionHistory.setItem(Rcount, 2, newItemreward)
        """

    def refreshTop(self):
        if self.syncstatus == 0:
            self.ui.toolButton_25.setText(' Syncing')
            self.ui.toolButton_25.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_25.setIcon(QIcon("pic/grayqukuai.png"))
            self.ui.toolButton_21.setText(' Syncing')
            self.ui.toolButton_21.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_21.setIcon(QIcon("pic/grayqukuai.png"))
            self.ui.toolButton_28.setText(' Syncing')
            self.ui.toolButton_28.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_28.setIcon(QIcon("pic/grayqukuai.png"))
            self.ui.toolButton_37.setText(' Syncing')
            self.ui.toolButton_37.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_37.setIcon(QIcon("pic/grayqukuai.png"))
            self.ui.toolButton_39.setText(' Syncing')
            self.ui.toolButton_39.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_39.setIcon(QIcon("pic/grayqukuai.png"))
            self.ui.toolButton_31.setText(' Syncing')
            self.ui.toolButton_31.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_31.setIcon(QIcon("pic/grayqukuai.png"))
            self.ui.toolButton_34.setText(' Syncing')
            self.ui.toolButton_34.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_34.setIcon(QIcon("pic/grayqukuai.png"))
        else:
            self.ui.toolButton_25.setText(' Completed')
            self.ui.toolButton_25.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_25.setIcon(QIcon("pic/purperqukuai.png"))
            self.ui.toolButton_21.setText(' Completed')
            self.ui.toolButton_21.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_21.setIcon(QIcon("pic/purperqukuai.png"))
            self.ui.toolButton_28.setText(' Completed')
            self.ui.toolButton_28.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_28.setIcon(QIcon("pic/purperqukuai.png"))
            self.ui.toolButton_31.setText(' Completed')
            self.ui.toolButton_31.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_31.setIcon(QIcon("pic/purperqukuai.png"))
            self.ui.toolButton_34.setText(' Completed')
            self.ui.toolButton_34.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_34.setIcon(QIcon("pic/purperqukuai.png"))
            self.ui.toolButton_37.setText(' Completed')
            self.ui.toolButton_37.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_37.setIcon(QIcon("pic/purperqukuai.png"))
            self.ui.toolButton_39.setText(' Completed')
            self.ui.toolButton_39.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_39.setIcon(QIcon("pic/purperqukuai.png"))
        if self.miningtatus == 0:
            self.ui.toolButton_26.setText(' Mining')
            self.ui.toolButton_26.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_26.setIcon(QIcon("pic/graymining.png"))
            self.ui.toolButton_22.setText(' Mining')
            self.ui.toolButton_22.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_22.setIcon(QIcon("pic/graymining.png"))
            self.ui.toolButton_29.setText(' Mining')
            self.ui.toolButton_29.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_29.setIcon(QIcon("pic/graymining.png"))
            self.ui.toolButton_32.setText(' Mining')
            self.ui.toolButton_32.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_32.setIcon(QIcon("pic/graymining.png"))
            self.ui.toolButton_35.setText(' Mining')
            self.ui.toolButton_35.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_35.setIcon(QIcon("pic/graymining.png"))
            self.ui.toolButton_38.setText(' Mining')
            self.ui.toolButton_38.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_38.setIcon(QIcon("pic/graymining.png"))
            self.ui.toolButton_41.setText(' Mining')
            self.ui.toolButton_41.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_41.setIcon(QIcon("pic/graymining.png"))
        else:
            self.ui.toolButton_26.setText(' Mining')
            self.ui.toolButton_26.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_26.setIcon(QIcon("pic/mining1.png"))
            self.ui.toolButton_29.setText(' Mining')
            self.ui.toolButton_29.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_29.setIcon(QIcon("pic/mining1.png"))
            self.ui.toolButton_22.setText(' Mining')
            self.ui.toolButton_22.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_22.setIcon(QIcon("pic/mining1.png"))
            self.ui.toolButton_32.setText(' Mining')
            self.ui.toolButton_32.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_32.setIcon(QIcon("pic/mining1.png"))
            self.ui.toolButton_35.setText(' Mining')
            self.ui.toolButton_35.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_35.setIcon(QIcon("pic/mining1.png"))
            self.ui.toolButton_38.setText(' Mining')
            self.ui.toolButton_38.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_38.setIcon(QIcon("pic/mining1.png"))
            self.ui.toolButton_41.setText(' Mining')
            self.ui.toolButton_41.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_41.setIcon(QIcon("pic/mining1.png"))
        if self.peers == 0:
            self.ui.toolButton_24.setText(' Peers Connected:0')
            self.ui.toolButton_24.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_24.setIcon(QIcon("pic/tubiaoer.png"))
            self.ui.toolButton_23.setText(' Peers Connected:0')
            self.ui.toolButton_23.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_23.setIcon(QIcon("pic/tubiaoer.png"))
            self.ui.toolButton_27.setText(' Peers Connected:0')
            self.ui.toolButton_27.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_27.setIcon(QIcon("pic/tubiaoer.png"))
            self.ui.toolButton_30.setText(' Peers Connected:0')
            self.ui.toolButton_30.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_30.setIcon(QIcon("pic/tubiaoer.png"))
            self.ui.toolButton_36.setText(' Peers Connected:0')
            self.ui.toolButton_36.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_36.setIcon(QIcon("pic/tubiaoer.png"))
            self.ui.toolButton_33.setText(' Peers Connected:0')
            self.ui.toolButton_33.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_33.setIcon(QIcon("pic/tubiaoer.png"))
            self.ui.toolButton_40.setText(' Peers Connected:0')
            self.ui.toolButton_40.setStyleSheet('color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_40.setIcon(QIcon("pic/tubiaoer.png"))
        else:
            self.ui.toolButton_24.setText(' Peers Connected:'+'')
            self.ui.toolButton_24.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_24.setIcon(QIcon("pic/tubiao1.png"))
            self.ui.toolButton_23.setText(' Peers Connected:' + '')
            self.ui.toolButton_23.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_23.setIcon(QIcon("pic/tubiao1.png"))
            self.ui.toolButton_27.setText(' Peers Connected:' + '')
            self.ui.toolButton_27.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_27.setIcon(QIcon("pic/tubiao1.png"))
            self.ui.toolButton_33.setText(' Peers Connected:' + '')
            self.ui.toolButton_33.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_33.setIcon(QIcon("pic/tubiao1.png"))
            self.ui.toolButton_36.setText(' Peers Connected:' + '')
            self.ui.toolButton_36.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_36.setIcon(QIcon("pic/tubiao1.png"))
            self.ui.toolButton_30.setText(' Peers Connected:' + '')
            self.ui.toolButton_30.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_30.setIcon(QIcon("pic/tubiao1.png"))
            self.ui.toolButton_40.setText(' Peers Connected:' + '')
            self.ui.toolButton_40.setStyleSheet('color: #aa00ff;border:0px;')
            self.ui.toolButton_40.setIcon(QIcon("pic/tubiao1.png"))

    def initchart(self):
        ###########
        dr = Figure_Canvas()
        ret1 = dr.test(self.m_wallet.address)  # 画图
        graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!
        self.ui.lineEdit_35.setText('Current: '+str((int(ret1))/(10**9))+' WTCT')
        nowtime = datetime.datetime.now()
        detaday = datetime.timedelta(days=30)
        da_days = nowtime - detaday
        self.ui.lineEdit_36.setText(da_days.strftime('%Y-%m-%d'))
        self.ui.lineEdit_37.setText(nowtime.strftime('%Y-%m-%d'))
        ###########
        drMarket = Figure_Canvas()
        ret2 = drMarket.testM()  # 画图
        graphicsceneM = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicsceneM.addWidget(drMarket)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView_2.setScene(graphicsceneM)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView_2.show()  # 最后，调用show方法呈现图形！Voila!!
        self.ui.lineEdit_39.setText(str(ret2)+ ' USD')

        self.ui.lineEdit_38.setText(da_days.strftime('%Y-%m-%d'))
        self.ui.lineEdit_40.setText(nowtime.strftime('%Y-%m-%d'))
        ###########
        drB = Figure_Canvas()
        drB.testB(self.m_wallet.address)  # 画图
        graphicsceneB = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicsceneB.addWidget(drB)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView_5.setScene(graphicsceneB)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView_5.show()  # 最后，调用show方法呈现图形！Voila!!

        self.ui.lineEdit_41.setText(da_days.strftime('%Y-%m-%d'))
        self.ui.lineEdit_42.setText(nowtime.strftime('%Y-%m-%d'))
        ###########
        drR = Figure_Canvas()
        ret4 = drR.testR(self.m_wallet.address)  # 画图
        graphicsceneR = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicsceneR.addWidget(drR)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView_6.setScene(graphicsceneR)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView_6.show()  # 最后，调用show方法呈现图形！Voila!!

        self.ui.lineEdit_43.setText(da_days.strftime('%Y-%m-%d'))
        self.ui.lineEdit_44.setText(nowtime.strftime('%Y-%m-%d'))
        self.ui.lineEdit_45.setText(str(ret4))

        ###########
    def initmining(self):
        if self.m_wallet.address!='':
            ret5 = Core_func.getMiningRecord(self.m_wallet.address)
            self.ui.miningHistory.setRowCount(0)
            for i in range(len(ret5[1])):
                Rcount = self.ui.miningHistory.rowCount()
                self.ui.miningHistory.setRowCount(Rcount + 1)
                newItemtime = QTableWidgetItem(ret5[1][i]['timestamp'][0:10])
                newItemblock = QTableWidgetItem(str(ret5[1][i]['blockNumer']))
                newItemreward = QTableWidgetItem(str(ret5[1][i]['totol_reward'])+'WTCT')

                self.ui.miningHistory.setItem(Rcount, 0, newItemtime)
                self.ui.miningHistory.setItem(Rcount, 1, newItemblock)
                self.ui.miningHistory.setItem(Rcount, 2, newItemreward)


    def initmap(self):
        pen = QPen()
        pen.setColor(QColor(255, 0, 0))
        pen.setBrush(QColor(255, 0, 0))
        source = Core_func.getCurrentNodesDistribution()
        sou = json.dumps(source[1]).strip('}')
        # sou = sou.strip('}')
        rce = sou.split(',')
        graphicsceneCR = QtWidgets.QGraphicsScene()
        nodemax = 0
        self.nationlist = ('AU', 3330, 1505,
                           'BR', 1370, 1365,
                           'CN', 3030, 865,
                           'CA', 690, 520,
                           'DE', 2005, 640,
                           'FR', 1920, 705,
                           'GB', 1880, 620,
                           'HK', 3115, 1000,
                           'IN', 2730, 1000,
                           'JP', 3375, 830,
                           'KR', 3255, 835,
                           'MY', 2985, 1195,
                           'RU', 2980, 480,
                           'SG', 3000, 1220,
                           'TH', 2275, 1070,
                           'US', 820, 795,

                           'AE', 2485, 1000,
                           'AR', 1225, 1635,
                           'BE', 1960, 667,
                           'BG', 2180, 778,
                           'GR', 2150, 820,
                           'RO', 2175, 730,
                           'TR', 2260, 820,
                           'BY', 2200, 625,
                           'PL', 2125, 645,
                           'DK', 2025, 590,
                           'EE', 2185, 550,
                           'CZ', 2070, 680,
                           'FI', 2200, 465,
                           'SE', 2080, 485,
                           'NO', 1995, 515,
                           'CH', 1998, 720,
                           'IT', 2045, 760,
                           'NL', 1970, 645,
                           'IE', 1830, 630,
                           'AT', 2065, 710,
                           'SI', 2080, 733,
                           'YU', 2135, 760,
                           'ES', 1870, 805,
                           'PT', 1825, 815,
                           'CY ', 2265, 868,
                           'MD', 2215, 715,
                           'CL', 1140, 1670,
                           'CO', 1120, 1215,
                           'NZ', 3785, 1695,
                           'TW', 3190, 990,
                           'IL', 2310, 915,
                           'DO', 1175, 1050,
                           'LU', 1990, 680,
                           'GE', 2375, 780,
                           'CR', 1020, 1152,
                           'HU', 2110, 720,
                           'CU', 1080, 1025,
                           'LV', 2180, 575,
                           'LT', 2165, 602,
                           'MA', 1830, 915,
                           'PE', 1095, 1350,
                           'PR', 1205, 1060,
                           'SK', 2120, 695,
                           'AM', 2390, 805,
                           'TJ', 2655, 825,
                           'TM', 2520, 815,
                           'ZA', 2165, 1595,

                           'LY', 2090, 960,
                           'NG', 1990, 1160,
                           'ID', 3120, 1270,
                           'MX', 815, 1000,
                           'PK', 2650, 930,
                           'VN', 3065, 1125,
                           'VE', 1210, 1180,
                           'SA', 2380, 1000,
                           'KH', 3025, 1125,
                           'AZ', 2420, 803,
                           'MM', 2930, 1025,
                           'EC', 1075, 1270,
                           'HN', 990, 1095,
                           'IS', 1710, 450,
                           'JM', 1088, 1061,
                           'JO', 2300, 920,
                           'SN', 1755, 1105,
                           'SC', 2505, 1304,
                           'UA', 2245, 690,
                           'UY', 1315, 1615)
        for i in rce:
            nodei = int(i.split(':')[1])
            if nodei > nodemax:
                nodemax = nodei
        for i in rce:
            # nodei = (i.split(':')[1])
            # print(int(i.split(':')[1]))
            # nodemax += nodei
            # print(i.split(':')[0][2:-1])
            webnation = i.split(':')[0][2:-1]
            for j in range(len(self.nationlist)):
                if self.nationlist[j] == webnation:
                    # print(float(self.nationlist[j+1])/4000*661, float(self.nationlist[j+2])/1991*241)
                    # print(float(self.nationlist[j+1])/4000*661+50, float(self.nationlist[j+2])/1991*241+10)

                    graphicsceneCR.addEllipse(float(self.nationlist[j + 1]) / 4000 * 661 + 90,
                                              float(self.nationlist[j + 2]) / 1991 * 241 + 20,
                                              3 + int(i.split(':')[1]) / nodemax * 15,
                                              3 + int(i.split(':')[1]) / nodemax * 10, pen)

                    graphicsceneCR.addEllipse(float(self.nationlist[j + 1]) / 4000 * 661,
                                              float(self.nationlist[j + 2]) / 1991 * 241, 0.00001, 0.00001, pen)
        # print(max(nodemax))
        # print(max(nodenum))
        # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        # for i in NODEnum:
        #   graphicsceneCR.addEllipse(40, 40, 4, 4, pen)
        # graphicsceneCR.addEllipse(40, 40, 4, 4,pen)
        # graphicsceneCR.addEllipse(10,10,60,60,pen)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.ui.graphicsView_7.setScene(graphicsceneCR)
        self.ui.graphicsView_7.show()  # 最后，调用show方法呈现图形！Voila!!

    def initUI(self):
        '显示窗口'
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.m_wallet = Wallet

        self.publishform = publishform()
        self.initchart()
        self.initmap()
        self.sendform = sendform()
        #self.nationpos()
        #self.timer = QTimer(self)  # 初始化一个定时器
        #self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        #self.timer.start(20000)  # 设置计时间隔并启动

        btnminHisrefresh = self.ui.pushButton_45
        btnminHisrefresh.clicked.connect(self.initmining)
        btntraHisrefresh = self.ui.pushButton_46
        btntraHisrefresh.clicked.connect(self.refresh)

        self.timertran = QTimer(self)  # 初始化一个定时器  transaction status
        self.timertran.timeout.connect(self.refresh)  # 计时结束调用operate()方法
        self.timertran.start(153000)  # 设置计时间隔并启动

        self.timermining = QTimer(self)  # 初始化一个定时器  transaction status
        self.timermining.timeout.connect(self.initmining)  # 计时结束调用operate()方法
        self.timermining.start(267000)  # 设置计时间隔并启动

        self.timerchart = QTimer(self)  # 初始化一个定时器  statistics
        self.timerchart.timeout.connect(self.initchart)  # 计时结束调用operate()方法
        self.timerchart.start(80000)  # 设置计时间隔并启动initmap

        self.timermap = QTimer(self)  # 初始化一个定时器  statistics
        self.timermap.timeout.connect(self.initmap)  # 计时结束调用operate()方法
        self.timermap.start(1730000)  # 设置计时间隔并启动

        self.timertop = QTimer(self)  # 初始化一个定时器  topstatus
        self.timertop.timeout.connect(self.refreshTop)  # 计时结束调用operate()方法
        self.timertop.start(30000)  # 设置计时间隔并启动
        self.miningtatus = 0
        self.syncstatus = 0
        self.peers = 0

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
        self.ui.pushButton_9.clicked.connect(self.sendform.show_w2)

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
        self.ui.ContactsT.setFrameShape(QFrame.NoFrame)  # 表格无边框
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
        self.ui.TransactionHistory.setFrameShape(QFrame.NoFrame)  # 表格无边框
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
        self.ui.miningHistory.setFrameShape(QFrame.NoFrame)  # 表格无边框
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

        self.initmining()

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
    txhash = ''
    status = 'Submitted'
    value = ''
    fromaddr = ''
    toaddr = ''
    Type = ''
    Gas = ''
    Gasprice = ''
    Blocknumber = ''
    timestamp = ''

class nationpos:
    nationlist= ('AU' ,3330, 1505,
    'BR' ,1370, 1365,
    'CN' ,3030, 865,
    'CA' ,690, 520,
    'DE' ,2005, 640,
    'FR' ,1920, 705,
    'GB' ,1880, 620,
    'HK' ,3115, 1000,
    'IN' ,2730, 1000,
    'JP' ,3375, 830,
    'KR' ,3255, 835,
    'MY' ,2985, 1195,
    'RU' ,2980, 480,
    'SG' ,3000, 1220,
    'TH' ,2275, 1070,
    'US' ,820, 795,

    'AE' ,2485, 1000,
    'AR' ,1225, 1635,
    'BE' ,1960, 667,
    'BG' ,2180, 778,
    'GR' ,2150, 820,
    'RO' ,2175, 730,
    'TR' ,2260, 820,
    'BY' ,2200, 625,
    'PL' ,2125, 645,
    'DK' ,2025, 590,
    'EE',2185, 550,
    'CZ' ,2070, 680,
    'FI',2200, 465,
    'SE' ,2080, 485,
    'NO',1995, 515,
    'CH',1998, 720,
    'IT' ,2045, 760,
    'NL' ,1970, 645,
    'IE',1830, 630,
    'AT' ,2065, 710,
    'SI' ,2080, 733,
    'YU',2135, 760,
    'ES' ,1870, 805,
    'PT' ,1825, 815,
    'CY ',2265, 868,
    'MD' ,2215, 715,
    'CL' ,1140, 1670,
    'CO',1120, 1215,
    'NZ' ,3785, 1695,
    'TW' ,3190, 990,
    'IL' ,2310, 915,
    'DO' ,1175, 1050,
    'LU' ,1990, 680,
    'GE' ,2375, 780,
    'CR' ,1020, 1152,
    'HU' ,2110, 720,
    'CU' ,1080, 1025,
    'LV' ,2180, 575,
    'LT' ,2165, 602,
    'MA' ,1830, 915,
   'PE'  ,1095, 1350,
    'PR' ,1205, 1060,
    'SK' ,2120, 695,
    'AM' ,2390, 805,
    'TJ' ,2655, 825,
    'TM' ,2520, 815,
    'ZA' ,2165, 1595,

    'LY' ,2090, 960,
    'NG' ,1990, 1160,
    'ID' ,3120, 1270,
    'MX' ,815, 1000,
    'PK' ,2650, 930,
    'VN' ,3065, 1125,
    'VE' ,1210, 1180,
    'SA' ,2380, 1000,
    'KH' ,3025, 1125,
    'AZ' ,2420, 803,
    'MM' ,2930, 1025,
    'EC' ,1075, 1270,
    'HN',990, 1095,
    'IS' ,1710, 450,
    'JM' ,1088, 1061,
    'JO' ,2300, 920,
    'SN',1755, 1105,
    'SC',2505, 1304,
    'UA' ,2245, 690,
    'UY',1315, 1615)

    AU = [3330, 1505]
    BR = [1370, 1365]
    CN = [3030, 865]
    CA = [690, 520]
    DE = [2005, 640]
    FR = [1920, 705]
    GB = [1880, 620]
    HK = [3115, 1000]
    IN = [2730, 1000]
    JP = [3375, 830]
    KR = [3255, 835]
    MY = [2985, 1195]
    RU = [2980, 480]
    SG = [3000, 1220]
    TH = [2275, 1070]
    US = [820, 795]

    AE = [2485, 1000]
    AR = [1225, 1635]
    BE = [1960, 667]
    BG = [2180, 778]
    GR = [2150, 820]
    RO = [2175, 730]
    TR = [2260, 820]
    BY = [2200, 625]
    PL = [2125, 645]
    DK = [2025, 590]
    EE = [2185, 550]
    CZ = [2070, 680]
    FI = [2200, 465]
    SE = [2080, 485]
    NO = [1995, 515]
    CH = [1998, 720]
    IT = [2045, 760]
    NL = [1970, 645]
    IE = [1830, 630]
    AT = [2065, 710]
    SI = [2080, 733]
    YU = [2135, 760]
    ES = [1870, 805]
    PT = [1825, 815]
    CY = [2265, 868]
    MD = [2215, 715]
    CL = [1140, 1670]
    CO = [1120, 1215]
    NZ = [3785, 1695]
    TW = [3190, 990]
    IL = [2310, 915]
    DO = [1175, 1050]
    LU = [1990, 680]
    GE = [2375, 780]
    CR = [1020, 1152]
    HU = [2110, 720]
    CU = [1080, 1025]
    LV = [2180, 575]
    LT = [2165, 602]
    MA = [1830, 915]
    PE = [1095, 1350]
    PR = [1205, 1060]
    SK = [2120, 695]
    AM = [2390, 805]
    TJ = [2655, 825]
    TM = [2520, 815]
    ZA = [2165, 1595]

    LY = [2090, 960]
    NG = [1990, 1160]
    ID = [3120, 1270]
    MX = [815, 1000]
    PK = [2650, 930]
    VN = [3065, 1125]
    VE = [1210, 1180]
    SA = [2380, 1000]
    KH = [3025, 1125]
    AZ = [2420, 803]
    MM = [2930, 1025]
    EC = [1075, 1270]
    HN = [990, 1095]
    IS = [1710, 450]
    JM = [1088, 1061]
    JO = [2300, 920]
    SN = [1755, 1105]
    SC = [2505, 1304]
    UA = [2245, 690]
    UY = [1315, 1615]
#class Communicate(Core_func.QObject):
#    closeApp = Core_func.pyqtSignal()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    #publishform = publishform()
    recieveform = recieveform()
    mulwalform =mulwalform()
    pubaddrForm = pubaddrForm()
    newcontactform = newcontactform()
    messform =messform()
    #s = Warning_Form.SecondWindow()
    #ex.ui.cw.clicked.connect(s.handle_click)
    ex.show()
    ex.ui.pushButton_10.clicked.connect(recieveform.show_w2)
    ex.ui.pushButton_36.clicked.connect(pubaddrForm.show_w2)
    ex.ui.pushButton_38.clicked.connect(newcontactform.show_w2)
    ex.ui.LogMessage.itemClicked.connect(messform.show_w2)
    ex.mwEdit.clicked.connect(mulwalform.show_w2)
    sys.exit(app.exec_())
