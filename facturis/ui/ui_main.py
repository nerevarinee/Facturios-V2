# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_main_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 500)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(117, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(17, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(40, 40, 40)")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.sonelgazeButton = QPushButton(self.frame_2)
        self.sonelgazeButton.setObjectName(u"sonelgazeButton")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.sonelgazeButton.setFont(font1)
        self.sonelgazeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sonelgazeButton.setLayoutDirection(Qt.RightToLeft)
        self.sonelgazeButton.setStyleSheet(u"color:rgb(212, 212, 212); background-color:rgb(255, 155, 3);")
        icon = QIcon()
        icon.addFile(u":/images/images/Logo_Sonelgaz.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sonelgazeButton.setIcon(icon)
        self.sonelgazeButton.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.sonelgazeButton)

        self.adeButton = QPushButton(self.frame_2)
        self.adeButton.setObjectName(u"adeButton")
        self.adeButton.setFont(font1)
        self.adeButton.setLayoutDirection(Qt.RightToLeft)
        self.adeButton.setStyleSheet(u"color:rgb(212, 212, 212); background-color:rgb(95, 95, 95);")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/222.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.adeButton.setIcon(icon1)
        self.adeButton.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.adeButton)

        self.telecomButton = QPushButton(self.frame_2)
        self.telecomButton.setObjectName(u"telecomButton")
        self.telecomButton.setFont(font1)
        self.telecomButton.setLayoutDirection(Qt.RightToLeft)
        self.telecomButton.setStyleSheet(u"color:rgb(50, 50, 50); background-color:rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/algerie-telecom-logo-png_seeklogo-210074.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.telecomButton.setIcon(icon2)
        self.telecomButton.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.telecomButton)

        self.facturePreciseeButton = QPushButton(self.frame_2)
        self.facturePreciseeButton.setObjectName(u"facturePreciseeButton")
        self.facturePreciseeButton.setFont(font1)
        self.facturePreciseeButton.setStyleSheet(u"color:rgb(212, 212, 212); background-color:rgb(95, 95, 95);")

        self.verticalLayout_2.addWidget(self.facturePreciseeButton)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(121, 121, 121)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(250, 250, 250)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.data_sonelgazeButton = QPushButton(self.frame)
        self.data_sonelgazeButton.setObjectName(u"data_sonelgazeButton")
        self.data_sonelgazeButton.setFont(font1)
        self.data_sonelgazeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.data_sonelgazeButton.setLayoutDirection(Qt.RightToLeft)
        self.data_sonelgazeButton.setStyleSheet(u"color:rgb(212, 212, 212); background-color:rgb(255, 155, 3);")
        self.data_sonelgazeButton.setIcon(icon)
        self.data_sonelgazeButton.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.data_sonelgazeButton)

        self.data_adeButton = QPushButton(self.frame)
        self.data_adeButton.setObjectName(u"data_adeButton")
        self.data_adeButton.setFont(font1)
        self.data_adeButton.setLayoutDirection(Qt.RightToLeft)
        self.data_adeButton.setStyleSheet(u"color:rgb(212, 212, 212); background-color:rgb(95, 95, 95);")
        self.data_adeButton.setIcon(icon1)
        self.data_adeButton.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.data_adeButton)

        self.data_telecomButton = QPushButton(self.frame)
        self.data_telecomButton.setObjectName(u"data_telecomButton")
        self.data_telecomButton.setFont(font1)
        self.data_telecomButton.setLayoutDirection(Qt.RightToLeft)
        self.data_telecomButton.setStyleSheet(u"color:rgb(50, 50, 50); background-color:rgb(255, 255, 255);")
        self.data_telecomButton.setIcon(icon2)
        self.data_telecomButton.setIconSize(QSize(48, 48))

        self.verticalLayout.addWidget(self.data_telecomButton)

        self.data_facturePreciseeButton = QPushButton(self.frame)
        self.data_facturePreciseeButton.setObjectName(u"data_facturePreciseeButton")
        self.data_facturePreciseeButton.setFont(font1)
        self.data_facturePreciseeButton.setStyleSheet(u"color:rgb(212, 212, 212); background-color:rgb(95, 95, 95);")

        self.verticalLayout.addWidget(self.data_facturePreciseeButton)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(17, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.parametres_button = QPushButton(Form)
        self.parametres_button.setObjectName(u"parametres_button")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.parametres_button.setFont(font2)
        self.parametres_button.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.parametres_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.storagePathLineEdit = QLineEdit(Form)
        self.storagePathLineEdit.setObjectName(u"storagePathLineEdit")

        self.verticalLayout_3.addWidget(self.storagePathLineEdit)

        self.verticalSpacer_3 = QSpacerItem(17, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(117, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nouveau Factures:", None))
        self.sonelgazeButton.setText(QCoreApplication.translate("Form", u"SONELGAZE ", None))
        self.adeButton.setText(QCoreApplication.translate("Form", u"ADE", None))
        self.telecomButton.setText(QCoreApplication.translate("Form", u"TELECOM", None))
        self.facturePreciseeButton.setText(QCoreApplication.translate("Form", u"+ Facture Precisee", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Factures deja enregestree:", None))
        self.data_sonelgazeButton.setText(QCoreApplication.translate("Form", u"SONELGAZE ", None))
        self.data_adeButton.setText(QCoreApplication.translate("Form", u"ADE", None))
        self.data_telecomButton.setText(QCoreApplication.translate("Form", u"TELECOM", None))
        self.data_facturePreciseeButton.setText(QCoreApplication.translate("Form", u"+ Facture Precisee", None))
        self.parametres_button.setText(QCoreApplication.translate("Form", u"Parametres", None))
    # retranslateUi

