# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_facture.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import resources_main_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 500)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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
        self.newFactureButton.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.newFactureButton)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Text = QWidget()
        self.Text.setObjectName(u"Text")
        self.verticalLayout = QVBoxLayout(self.Text)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fp_text_output = QTextBrowser(self.Text)
        self.fp_text_output.setObjectName(u"fp_text_output")

        self.verticalLayout.addWidget(self.fp_text_output)

        self.tabWidget.addTab(self.Text, "")
        self.Image = QWidget()
        self.Image.setObjectName(u"Image")
        self.verticalLayout_2 = QVBoxLayout(self.Image)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fp_img_output = QGraphicsView(self.Image)
        self.fp_img_output.setObjectName(u"fp_img_output")

        self.verticalLayout_2.addWidget(self.fp_img_output)

        self.tabWidget.addTab(self.Image, "")

        self.verticalLayout_6.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.numFactureField = QLineEdit(Form)
        self.numFactureField.setObjectName(u"numFactureField")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.numFactureField)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.sommeField = QLineEdit(Form)
        self.sommeField.setObjectName(u"sommeField")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sommeField)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.error_msg = QLabel(Form)
        self.error_msg.setObjectName(u"error_msg")

        self.verticalLayout_3.addWidget(self.error_msg)

        self.add_facture_info = QPushButton(Form)
        self.add_facture_info.setObjectName(u"add_facture_info")
        sizePolicy.setHeightForWidth(self.add_facture_info.sizePolicy().hasHeightForWidth())
        self.add_facture_info.setSizePolicy(sizePolicy)
        self.add_facture_info.setFont(font)
        self.add_facture_info.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.add_facture_info)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.paidButton = QPushButton(Form)
        self.paidButton.setObjectName(u"paidButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(25)
        sizePolicy1.setHeightForWidth(self.paidButton.sizePolicy().hasHeightForWidth())
        self.paidButton.setSizePolicy(sizePolicy1)
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

        self.verticalLayout_3.addWidget(self.paidButton)

        self.waitlistButton = QPushButton(Form)
        self.waitlistButton.setObjectName(u"waitlistButton")
        sizePolicy1.setHeightForWidth(self.waitlistButton.sizePolicy().hasHeightForWidth())
        self.waitlistButton.setSizePolicy(sizePolicy1)
        self.waitlistButton.setFont(font2)
        self.waitlistButton.setLayoutDirection(Qt.LeftToRight)
        self.waitlistButton.setStyleSheet(u"color:rgb(250, 250, 250); background-color:rgb(95, 95, 95);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/WHITE-time-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.waitlistButton.setIcon(icon1)
        self.waitlistButton.setFlat(False)

        self.verticalLayout_3.addWidget(self.waitlistButton)

        self.annulerButton = QPushButton(Form)
        self.annulerButton.setObjectName(u"annulerButton")
        sizePolicy1.setHeightForWidth(self.annulerButton.sizePolicy().hasHeightForWidth())
        self.annulerButton.setSizePolicy(sizePolicy1)
        self.annulerButton.setFont(font2)
        self.annulerButton.setStyleSheet(u"color:rgb(212, 212, 212); background-color:rgb(234, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/WHITE-cross-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.annulerButton.setIcon(icon2)
        self.annulerButton.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.annulerButton)

        self.go_back_button = QPushButton(Form)
        self.go_back_button.setObjectName(u"go_back_button")
        sizePolicy.setHeightForWidth(self.go_back_button.sizePolicy().hasHeightForWidth())
        self.go_back_button.setSizePolicy(sizePolicy)
        self.go_back_button.setFont(font)
        self.go_back_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/WHITE-arrow-narrow-left-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.go_back_button.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.go_back_button)

        self.verticalSpacer_2 = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)
        self.waitlistButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.newFactureButton.setText(QCoreApplication.translate("Form", u"+ ajoutee un facture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Text), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Image), QCoreApplication.translate("Form", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("Form", u"Numero de Facture:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Somme:", None))
        self.error_msg.setText("")
        self.add_facture_info.setText(QCoreApplication.translate("Form", u"+ ajoute un field", None))
        self.paidButton.setText(QCoreApplication.translate("Form", u"Paiee", None))
        self.waitlistButton.setText(QCoreApplication.translate("Form", u"en attendre", None))
        self.annulerButton.setText(QCoreApplication.translate("Form", u"Annuler", None))
        self.go_back_button.setText("")
    # retranslateUi

