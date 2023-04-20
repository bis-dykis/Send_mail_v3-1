# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1099, 802)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 40, 541, 91))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 40, 48, 21))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 40, 61, 21))
        self.id_edit = QLineEdit(self.groupBox)
        self.id_edit.setObjectName(u"id_edit")
        self.id_edit.setGeometry(QRect(80, 35, 151, 31))
        self.pass_edit = QLineEdit(self.groupBox)
        self.pass_edit.setObjectName(u"pass_edit")
        self.pass_edit.setGeometry(QRect(330, 34, 191, 31))
        self.pass_edit.setEchoMode(QLineEdit.Password)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 170, 171, 16))
        self.label_5.setFont(font)
        self.list_edit = QLineEdit(self.centralwidget)
        self.list_edit.setObjectName(u"list_edit")
        self.list_edit.setGeometry(QRect(40, 190, 430, 30))
        self.list_btn = QPushButton(self.centralwidget)
        self.list_btn.setObjectName(u"list_btn")
        self.list_btn.setGeometry(QRect(500, 190, 70, 30))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 240, 161, 16))
        self.label_6.setFont(font)
        self.attach_edit = QLineEdit(self.centralwidget)
        self.attach_edit.setObjectName(u"attach_edit")
        self.attach_edit.setGeometry(QRect(40, 260, 430, 30))
        self.attach_btn = QPushButton(self.centralwidget)
        self.attach_btn.setObjectName(u"attach_btn")
        self.attach_btn.setGeometry(QRect(500, 260, 70, 30))
        self.send_btn = QPushButton(self.centralwidget)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setEnabled(True)
        self.send_btn.setGeometry(QRect(240, 660, 141, 51))
        self.send_btn.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 330, 48, 16))
        self.label.setFont(font)
        self.subject_edit = QLineEdit(self.centralwidget)
        self.subject_edit.setObjectName(u"subject_edit")
        self.subject_edit.setGeometry(QRect(40, 350, 531, 31))
        self.subject_edit.setFont(font)
        self.body_edit = QTextEdit(self.centralwidget)
        self.body_edit.setObjectName(u"body_edit")
        self.body_edit.setGeometry(QRect(40, 430, 531, 191))
        self.body_edit.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 410, 48, 16))
        self.label_2.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(930, 730, 131, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_7.setFont(font1)
        self.list_table = QTableWidget(self.centralwidget)
        if (self.list_table.columnCount() < 3):
            self.list_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.list_table.setObjectName(u"list_table")
        self.list_table.setGeometry(QRect(610, 100, 460, 471))
        self.list_table.setFont(font)
        self.list_table.setColumnCount(3)
        self.list_table.horizontalHeader().setCascadingSectionResizes(False)
        self.list_table.horizontalHeader().setMinimumSectionSize(30)
        self.list_table.horizontalHeader().setDefaultSectionSize(100)
        self.list_table.horizontalHeader().setStretchLastSection(False)
        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(680, 580, 131, 41))
        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(850, 580, 121, 41))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1099, 22))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\uba54\uc77c \ubcf4\ub0b4\uae30", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"\ub124\uc774\ubc84", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\uc544\uc774\ub514", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\ud328\uc2a4\uc6cc\ub4dc", None))
        self.id_edit.setText("")
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\uba54\uc77c \ub9ac\uc2a4\ud2b8 (\uc5d1\uc140\ud30c\uc77c)", None))
        self.list_btn.setText(QCoreApplication.translate("mainWindow", u"\uc5f4\uae30", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\ucca8\ubd80\ud30c\uc77c (PDF) \uacbd\ub85c", None))
        self.attach_btn.setText(QCoreApplication.translate("mainWindow", u"\uc5f4\uae30", None))
        self.send_btn.setText(QCoreApplication.translate("mainWindow", u"\uba54\uc77c \uc804\uc1a1", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\uc81c\ubaa9", None))
        self.subject_edit.setText(QCoreApplication.translate("mainWindow", u"\uc81c\ubaa9\uc744 \uc785\ub825\ud558\uc138\uc694.", None))
        self.body_edit.setHtml(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub098\ub214\uace0\ub515'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ub0b4\uc6a9\uc744 \uc785\ub825\ud558\uc138\uc694.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\ub0b4\uc6a9", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"Powered by 4elife", None))
        ___qtablewidgetitem = self.list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"\uac70\ub798\ucc98\uba85", None));
        ___qtablewidgetitem1 = self.list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"\uc774\uba54\uc77c", None));
        ___qtablewidgetitem2 = self.list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"\uc804\uc1a1", None));
        self.delete_btn.setText(QCoreApplication.translate("mainWindow", u"\uc120\ud0dd \uc0ad\uc81c", None))
        self.add_btn.setText(QCoreApplication.translate("mainWindow", u"\ucd94\uac00", None))
    # retranslateUi

