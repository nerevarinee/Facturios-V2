# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
        Form.resize(500, 349)
        Form.setStyleSheet(u"background-color:rgb(0, 85, 255)")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

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

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color:white;font-size:12pt")
        self.label_11.setTextFormat(Qt.PlainText)

        self.verticalLayout_2.addWidget(self.label_11)

        self.password_field_2 = QLineEdit(Form)
        self.password_field_2.setObjectName(u"password_field_2")
        self.password_field_2.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.verticalLayout_2.addWidget(self.password_field_2)

        self.enrigstre_button = QPushButton(Form)
        self.enrigstre_button.setObjectName(u"enrigstre_button")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.enrigstre_button.setFont(font1)
        self.enrigstre_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

        self.verticalLayout_2.addWidget(self.enrigstre_button)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:red; background-color:white")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Nom d'utilizateur:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Mot de pass:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Confirme le mote de pass", None))
        self.enrigstre_button.setText(QCoreApplication.translate("Form", u"Enregistrer", None))
        self.label.setText(QCoreApplication.translate("Form", u"Assurez-vous de noter vos qualifications", None))
    # retranslateUi

