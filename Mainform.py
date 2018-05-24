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
import datetime
from eth_account import Account
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout,QDialog,QFileDialog,QTableWidgetItem,
                             QLineEdit, QFrame, QAbstractItemView)
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from Mainform_QT import *




class Example(QDialog,QWidget):

    def __init__(self):
        super().__init__()


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

            ret = Core_func.Import_From_Private( self.ui.lineEdit_20.text())
            if ret[0] == 1:
                self.m_wallet.password = self.ui.lineEdit_18.text()
                self.m_wallet.address = ret[1]
                self.m_wallet.privateKey = self.ui.lineEdit_20.text()
                self.m_wallet.accountname = ret[1][0:10]
                self.addWallet()
                self.ui.lineEdit_8.setText(ret[1])
                self.ui.lineEdit_9.setText(self.ui.lineEdit_20.text())
                self.imgpub = qrcode.make(self.m_wallet.address)
                self.imgpub.save("pic\\public.png")
                self.ui.stackedWidget.setCurrentIndex(1)


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
        ret = Core_func.Import_Keystore(self.ui.lineEdit_6 .text(), content)
        if ret[0] ==1:
            self.m_wallet.password = self.ui.lineEdit_6.text()
            self.m_wallet.address = ret[1][0]
            self.m_wallet.privateKey = ret[1][1]
            self.m_wallet.accountname = ret[1][0][0:10]
            self.addWallet()
            self.ui.lineEdit_8.setText(ret[1][0])
            self.ui.lineEdit_9.setText(ret[1][1])
            self.imgpub = qrcode.make(self.m_wallet.address)
            self.imgpub.save("pic\\public.png")
            self.ui.stackedWidget.setCurrentIndex(1)
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

    def savekey(self):
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

    def initUI(self):
        '显示窗口'
        self.ui = Ui_Form()
        self.ui.setupUi(self)
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

        self.ui.LogMessage.horizontalHeader().setVisible(0)
        self.ui.LogMessage.verticalHeader().setVisible(0)
        self.ui.LogMessage.setShowGrid(0)
        self.ui.LogMessage.horizontalHeader().setStretchLastSection(1)
        self.ui.LogMessage.verticalHeader().setDefaultSectionSize(57)
        self.ui.LogMessage.setColumnWidth(0, 200)  # 将设置第1列的单元格成20宽度
        self.ui.LogMessage.setColumnWidth(1, 310)  # 将设置第2列的单元格成30宽度
        self.ui.LogMessage.setColumnWidth(2, 100)  # 将设置第3列的单元格成50宽度
        self.ui.LogMessage.setColumnWidth(3, 100)  # 将设置第2列的单元格成30宽度
        self.ui.LogMessage.setColumnWidth(4, 100)
        self.ui.LogMessage.setFrameShape(QFrame.Box)  # 表格无边框
        self.ui.LogMessage.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.ui.LogMessage.setSelectionMode(QAbstractItemView.NoSelection)  # 单元不可选
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

        mwOpen = QPushButton("Open")  # type: QPushButton
        mwOpen.setStyleSheet(''' background-color: rgb(255, 255, 255);color: rgb(170, 0, 255); 
                                                            height : 19px; width:70px;border-color: rgb(170, 0, 255);
                                                            font : 12px "Bahnschrift Light"; ''')
        #mwOpen.setIconSize(QSize(41,21))

        mwEdit = QPushButton("Edit")  # type: QPushButton
        mwEdit.setStyleSheet('''background-color: rgb(255, 255, 255);color: rgb(170, 0, 255);
                                                    height : 19px; width:70px;border-color: rgb(170, 0, 255);
                                                    font : 12px "Bahnschrift Light"; ''')
        mwDelete = QPushButton("Delete")  # type: QPushButton
        mwDelete.setStyleSheet(''' background-color: rgb(255, 255, 255);color: rgb(170, 0, 255);
                                                    height : 19px; width:70px;border-color: rgb(170, 0, 255);
                                                    font : 12px "Bahnschrift Light"; ''')
        mwSaveKey = QPushButton("Save Key")  # type: QPushButton
        mwSaveKey.setStyleSheet(''' background-color: rgb(255, 255, 255);color: rgb(170, 0, 255); 
                                                    height : 19px; width:70px;border-color: rgb(170, 0, 255);
                                                    font : 12px "Bahnschrift Light"; ''')
        self.ui.multWallet.setCellWidget(1, 2, mwOpen)
        self.ui.multWallet.setCellWidget(1, 3, mwEdit)
        self.ui.multWallet.setCellWidget(1, 4, mwDelete)
        self.ui.multWallet.setCellWidget(1, 5, mwSaveKey)



        #self.show()  # show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。
class Wallet:
    password = ''
    privateKey = ''
    mnem = ''
    address = ''
    accountname = ''




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    #s = Warning_Form.SecondWindow()
    #ex.ui.cw.clicked.connect(s.handle_click)
    ex.show()
    sys.exit(app.exec_())
