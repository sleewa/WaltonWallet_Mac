import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout,
                             QLineEdit, QFrame, QAbstractItemView)
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from Mainform_QT import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def pressbtn1(self):
        self.ui.mywallet.setIcon(QIcon("pic/mywallet1.png"))
        self.ui.statistic.setIcon(QIcon("pic/statistics0.png"))
        self.ui.message.setIcon(QIcon('pic/message0.png'))
        self.ui.contact.setIcon(QIcon("pic/contact0.png"))
        self.ui.mining.setIcon(QIcon("pic/mining0.png"))
        self.ui.mw.setIcon(QIcon("pic/mw0.png"))
        self.ui.cw.setIcon(QIcon("pic/cw0.png"))
        self.ui.stackedWidget.setCurrentIndex(1)

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

    def initUI(self):
        '显示窗口'
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        stackedW = self.ui.stackedWidget

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

        stackedW.setCurrentIndex(1)

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

        self.show()  # show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
