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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 500)
        Form.setStyleSheet(u"background-color:rgb(0, 85, 255)")
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.parametres_button = QPushButton(Form)
        self.parametres_button.setObjectName(u"parametres_button")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(False)
        self.parametres_button.setFont(font)
        self.parametres_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/setting-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.parametres_button.setIcon(icon)

        self.verticalLayout_4.addWidget(self.parametres_button)

        self.verticalSpacer_3 = QSpacerItem(17, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(117, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(17, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(217, 217, 217)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:rgb(40, 40, 40)")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.sonelgazeButton = QPushButton(self.frame_2)
        self.sonelgazeButton.setObjectName(u"sonelgazeButton")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.sonelgazeButton.setFont(font2)
        self.sonelgazeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sonelgazeButton.setLayoutDirection(Qt.RightToLeft)
        self.sonelgazeButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/Logo_Sonelgaz.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sonelgazeButton.setIcon(icon1)
        self.sonelgazeButton.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.sonelgazeButton)

        self.adeButton = QPushButton(self.frame_2)
        self.adeButton.setObjectName(u"adeButton")
        self.adeButton.setFont(font2)
        self.adeButton.setLayoutDirection(Qt.RightToLeft)
        self.adeButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/222.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.adeButton.setIcon(icon2)
        self.adeButton.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.adeButton)

        self.telecomButton = QPushButton(self.frame_2)
        self.telecomButton.setObjectName(u"telecomButton")
        self.telecomButton.setFont(font2)
        self.telecomButton.setLayoutDirection(Qt.RightToLeft)
        self.telecomButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/algerie-telecom-logo-png_seeklogo-210074.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.telecomButton.setIcon(icon3)
        self.telecomButton.setIconSize(QSize(48, 48))

        self.verticalLayout_2.addWidget(self.telecomButton)

        self.facturePreciseeButton = QPushButton(self.frame_2)
        self.facturePreciseeButton.setObjectName(u"facturePreciseeButton")
        self.facturePreciseeButton.setFont(font2)
        self.facturePreciseeButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

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
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:rgb(250, 250, 250)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.data_sonelgazeButton = QPushButton(self.frame)
        self.data_sonelgazeButton.setObjectName(u"data_sonelgazeButton")
        self.data_sonelgazeButton.setFont(font2)
        self.data_sonelgazeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.data_sonelgazeButton.setLayoutDirection(Qt.RightToLeft)
        self.data_sonelgazeButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        self.data_sonelgazeButton.setIcon(icon1)
        self.data_sonelgazeButton.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.data_sonelgazeButton)

        self.data_adeButton = QPushButton(self.frame)
        self.data_adeButton.setObjectName(u"data_adeButton")
        self.data_adeButton.setFont(font2)
        self.data_adeButton.setLayoutDirection(Qt.RightToLeft)
        self.data_adeButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        self.data_adeButton.setIcon(icon2)
        self.data_adeButton.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.data_adeButton)

        self.data_telecomButton = QPushButton(self.frame)
        self.data_telecomButton.setObjectName(u"data_telecomButton")
        self.data_telecomButton.setFont(font2)
        self.data_telecomButton.setLayoutDirection(Qt.RightToLeft)
        self.data_telecomButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        self.data_telecomButton.setIcon(icon3)
        self.data_telecomButton.setIconSize(QSize(48, 48))

        self.verticalLayout.addWidget(self.data_telecomButton)

        self.data_facturePreciseeButton = QPushButton(self.frame)
        self.data_facturePreciseeButton.setObjectName(u"data_facturePreciseeButton")
        self.data_facturePreciseeButton.setFont(font2)
        self.data_facturePreciseeButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

        self.verticalLayout.addWidget(self.data_facturePreciseeButton)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(17, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(174, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.parametres_button.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Nouveau Factures", None))
        self.sonelgazeButton.setText(QCoreApplication.translate("Form", u"SONELGAZE ", None))
        self.adeButton.setText(QCoreApplication.translate("Form", u"ADE", None))
        self.telecomButton.setText(QCoreApplication.translate("Form", u"TELECOM", None))
        self.facturePreciseeButton.setText(QCoreApplication.translate("Form", u"Facture Precises", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Archive", None))
        self.data_sonelgazeButton.setText(QCoreApplication.translate("Form", u"SONELGAZE ", None))
        self.data_adeButton.setText(QCoreApplication.translate("Form", u"ADE", None))
        self.data_telecomButton.setText(QCoreApplication.translate("Form", u"TELECOM", None))
        self.data_facturePreciseeButton.setText(QCoreApplication.translate("Form", u" Factures Precises", None))
    # retranslateUi

