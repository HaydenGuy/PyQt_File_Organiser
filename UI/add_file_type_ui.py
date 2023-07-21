# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_file_type.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_add_file_type(object):
    def setupUi(self, add_file_type):
        if not add_file_type.objectName():
            add_file_type.setObjectName(u"add_file_type")
        add_file_type.resize(313, 137)
        self.verticalLayout = QVBoxLayout(add_file_type)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_file_text = QLabel(add_file_type)
        self.add_file_text.setObjectName(u"add_file_text")
        self.add_file_text.setStyleSheet(u"color:black")

        self.horizontalLayout.addWidget(self.add_file_text)

        self.lb_format = QLabel(add_file_type)
        self.lb_format.setObjectName(u"lb_format")
        self.lb_format.setStyleSheet(u"color:red;")

        self.horizontalLayout.addWidget(self.lb_format)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.le_user_input = QLineEdit(add_file_type)
        self.le_user_input.setObjectName(u"le_user_input")

        self.verticalLayout.addWidget(self.le_user_input)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_ok = QPushButton(add_file_type)
        self.pb_ok.setObjectName(u"pb_ok")

        self.horizontalLayout_2.addWidget(self.pb_ok)

        self.pb_cancel = QPushButton(add_file_type)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.horizontalLayout_2.addWidget(self.pb_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(add_file_type)

        QMetaObject.connectSlotsByName(add_file_type)
    # setupUi

    def retranslateUi(self, add_file_type):
        add_file_type.setWindowTitle(QCoreApplication.translate("add_file_type", u"Add File Type", None))
        self.add_file_text.setText(QCoreApplication.translate("add_file_type", u"Add a file type in the format: ", None))
        self.lb_format.setText(QCoreApplication.translate("add_file_type", u"*.xxx", None))
        self.pb_ok.setText(QCoreApplication.translate("add_file_type", u"OK", None))
        self.pb_cancel.setText(QCoreApplication.translate("add_file_type", u"Cancel", None))
    # retranslateUi

