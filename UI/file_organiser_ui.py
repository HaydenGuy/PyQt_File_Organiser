# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_organiser.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_file_organiser(object):
    def setupUi(self, file_organiser):
        if not file_organiser.objectName():
            file_organiser.setObjectName(u"file_organiser")
        file_organiser.resize(487, 291)
        file_organiser.setMinimumSize(QSize(487, 291))
        self.centralwidget = QWidget(file_organiser)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color:black;")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(35)
        self.gridLayout.setContentsMargins(25, -1, 20, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cb_mp3 = QCheckBox(self.frame)
        self.cb_mp3.setObjectName(u"cb_mp3")

        self.horizontalLayout_4.addWidget(self.cb_mp3)

        self.cb_wav = QCheckBox(self.frame)
        self.cb_wav.setObjectName(u"cb_wav")

        self.horizontalLayout_4.addWidget(self.cb_wav)

        self.cb_jpg = QCheckBox(self.frame)
        self.cb_jpg.setObjectName(u"cb_jpg")

        self.horizontalLayout_4.addWidget(self.cb_jpg)

        self.cb_png = QCheckBox(self.frame)
        self.cb_png.setObjectName(u"cb_png")

        self.horizontalLayout_4.addWidget(self.cb_png)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cb_pdf = QCheckBox(self.frame)
        self.cb_pdf.setObjectName(u"cb_pdf")

        self.horizontalLayout_5.addWidget(self.cb_pdf)

        self.cb_txt = QCheckBox(self.frame)
        self.cb_txt.setObjectName(u"cb_txt")

        self.horizontalLayout_5.addWidget(self.cb_txt)

        self.cb_mp4 = QCheckBox(self.frame)
        self.cb_mp4.setObjectName(u"cb_mp4")

        self.horizontalLayout_5.addWidget(self.cb_mp4)

        self.cb_mov = QCheckBox(self.frame)
        self.cb_mov.setObjectName(u"cb_mov")

        self.horizontalLayout_5.addWidget(self.cb_mov)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pb_browse = QPushButton(self.frame)
        self.pb_browse.setObjectName(u"pb_browse")

        self.horizontalLayout_6.addWidget(self.pb_browse)

        self.pb_organise = QPushButton(self.frame)
        self.pb_organise.setObjectName(u"pb_organise")

        self.horizontalLayout_6.addWidget(self.pb_organise)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        file_organiser.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(file_organiser)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 487, 20))
        file_organiser.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(file_organiser)
        self.statusbar.setObjectName(u"statusbar")
        file_organiser.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.cb_mp3, self.cb_wav)
        QWidget.setTabOrder(self.cb_wav, self.cb_jpg)
        QWidget.setTabOrder(self.cb_jpg, self.cb_png)
        QWidget.setTabOrder(self.cb_png, self.cb_pdf)
        QWidget.setTabOrder(self.cb_pdf, self.cb_txt)
        QWidget.setTabOrder(self.cb_txt, self.cb_mp4)
        QWidget.setTabOrder(self.cb_mp4, self.cb_mov)
        QWidget.setTabOrder(self.cb_mov, self.pb_browse)
        QWidget.setTabOrder(self.pb_browse, self.pb_organise)

        self.retranslateUi(file_organiser)

        QMetaObject.connectSlotsByName(file_organiser)
    # setupUi

    def retranslateUi(self, file_organiser):
        file_organiser.setWindowTitle(QCoreApplication.translate("file_organiser", u"File Organiser", None))
        self.cb_mp3.setText(QCoreApplication.translate("file_organiser", u".mp3", None))
        self.cb_wav.setText(QCoreApplication.translate("file_organiser", u".wav", None))
        self.cb_jpg.setText(QCoreApplication.translate("file_organiser", u".jpg", None))
        self.cb_png.setText(QCoreApplication.translate("file_organiser", u".png", None))
        self.cb_pdf.setText(QCoreApplication.translate("file_organiser", u".pdf", None))
        self.cb_txt.setText(QCoreApplication.translate("file_organiser", u".txt", None))
        self.cb_mp4.setText(QCoreApplication.translate("file_organiser", u".mp4", None))
        self.cb_mov.setText(QCoreApplication.translate("file_organiser", u".mov", None))
        self.pb_browse.setText(QCoreApplication.translate("file_organiser", u"Browse", None))
        self.pb_organise.setText(QCoreApplication.translate("file_organiser", u"Organise", None))
    # retranslateUi

