# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(501, 323)
        Form.setStyleSheet(u"background-color:rgb(0, 85, 255)")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(101, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color:white;font-size:12pt")
        self.label_9.setTextFormat(Qt.PlainText)

        self.verticalLayout_2.addWidget(self.label_9)

        self.user_field = QLineEdit(Form)
        self.user_field.setObjectName(u"user_field")
        self.user_field.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.verticalLayout_2.addWidget(self.user_field)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color:white;font-size:12pt")
        self.label_10.setTextFormat(Qt.PlainText)

        self.verticalLayout_2.addWidget(self.label_10)

        self.password_field = QLineEdit(Form)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.verticalLayout_2.addWidget(self.password_field)

        self.login_button = QPushButton(Form)
        self.login_button.setObjectName(u"login_button")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.login_button.setFont(font1)
        self.login_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

        self.verticalLayout_2.addWidget(self.login_button)

        self.error_label = QLabel(Form)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setStyleSheet(u"color:rgb(255, 0, 0); font-size:15pt;")

        self.verticalLayout_2.addWidget(self.error_label)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color:rgb(220, 220, 220);")
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(101, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Nom d'utilizateur:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Mot de pass:", None))
        self.login_button.setText(QCoreApplication.translate("Form", u"Login", None))
        self.error_label.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"If you forgot your password, contact your admin.", None))
    # retranslateUi

