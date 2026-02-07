# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facture.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 500)
        Form.setStyleSheet(u"background-color:rgb(0, 85, 255)")
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.newFactureButton = QPushButton(Form)
        self.newFactureButton.setObjectName(u"newFactureButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newFactureButton.sizePolicy().hasHeightForWidth())
        self.newFactureButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(False)
        self.newFactureButton.setFont(font)
        self.newFactureButton.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

        self.verticalLayout.addWidget(self.newFactureButton)

        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.graphicsView)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.factureTypeLabel = QLabel(Form)
        self.factureTypeLabel.setObjectName(u"factureTypeLabel")
        font1 = QFont()
        font1.setPointSize(12)
        self.factureTypeLabel.setFont(font1)
        self.factureTypeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.factureTypeLabel)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.numFactureField = QLineEdit(Form)
        self.numFactureField.setObjectName(u"numFactureField")
        self.numFactureField.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.verticalLayout_3.addWidget(self.numFactureField)

        self.sommeField = QLineEdit(Form)
        self.sommeField.setObjectName(u"sommeField")
        self.sommeField.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.verticalLayout_3.addWidget(self.sommeField)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.noteField = QPlainTextEdit(Form)
        self.noteField.setObjectName(u"noteField")
        self.noteField.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.horizontalLayout_2.addWidget(self.noteField)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.paidButton = QPushButton(Form)
        self.paidButton.setObjectName(u"paidButton")
        sizePolicy.setHeightForWidth(self.paidButton.sizePolicy().hasHeightForWidth())
        self.paidButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.paidButton.setFont(font2)
        self.paidButton.setStyleSheet(u"color:rgb(250, 250, 250); background-color:rgb(0, 132, 0);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/WHITE-correct-signal-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.paidButton.setIcon(icon)
        self.paidButton.setIconSize(QSize(15, 15))

        self.verticalLayout_6.addWidget(self.paidButton)

        self.waitlistButton = QPushButton(Form)
        self.waitlistButton.setObjectName(u"waitlistButton")
        sizePolicy.setHeightForWidth(self.waitlistButton.sizePolicy().hasHeightForWidth())
        self.waitlistButton.setSizePolicy(sizePolicy)
        self.waitlistButton.setFont(font2)
        self.waitlistButton.setLayoutDirection(Qt.LeftToRight)
        self.waitlistButton.setStyleSheet(u"color:rgb(250, 250, 250); background-color:rgb(95, 95, 95);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/WHITE-time-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.waitlistButton.setIcon(icon1)
        self.waitlistButton.setFlat(False)

        self.verticalLayout_6.addWidget(self.waitlistButton)

        self.annulerButton = QPushButton(Form)
        self.annulerButton.setObjectName(u"annulerButton")
        sizePolicy.setHeightForWidth(self.annulerButton.sizePolicy().hasHeightForWidth())
        self.annulerButton.setSizePolicy(sizePolicy)
        self.annulerButton.setFont(font2)
        self.annulerButton.setStyleSheet(u"color:rgb(212, 212, 212); background-color:rgb(234, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/WHITE-cross-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.annulerButton.setIcon(icon2)
        self.annulerButton.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.annulerButton)

        self.go_back_button = QPushButton(Form)
        self.go_back_button.setObjectName(u"go_back_button")
        sizePolicy.setHeightForWidth(self.go_back_button.sizePolicy().hasHeightForWidth())
        self.go_back_button.setSizePolicy(sizePolicy)
        self.go_back_button.setFont(font)
        self.go_back_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/arrow-narrow-left-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.go_back_button.setIcon(icon3)

        self.verticalLayout_6.addWidget(self.go_back_button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 4)
        self.verticalLayout_6.setStretch(2, 4)
        self.verticalLayout_6.setStretch(4, 2)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_7.setStretch(3, 10)

        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalLayout_4.setStretch(0, 10)

        self.retranslateUi(Form)

        self.waitlistButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.newFactureButton.setText(QCoreApplication.translate("Form", u"+ ajoutee un facture", None))
        self.factureTypeLabel.setStyleSheet(QCoreApplication.translate("Form", u"color:white", None))
        self.factureTypeLabel.setText(QCoreApplication.translate("Form", u"facture type", None))
        self.label.setStyleSheet(QCoreApplication.translate("Form", u"color:white", None))
        self.label.setText(QCoreApplication.translate("Form", u"Numero de Facture:", None))
        self.label_2.setStyleSheet(QCoreApplication.translate("Form", u"color:white", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Somme:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Note", None))
        self.paidButton.setText(QCoreApplication.translate("Form", u"Paiee", None))
        self.waitlistButton.setText(QCoreApplication.translate("Form", u"en attendre", None))
        self.annulerButton.setText(QCoreApplication.translate("Form", u"Annuler", None))
        self.go_back_button.setText("")
    # retranslateUi

