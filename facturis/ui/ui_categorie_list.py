# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categorie_list.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 500)
        Form.setStyleSheet(u"background-color:rgb(0, 85, 255)")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(261, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.go_back_button = QPushButton(Form)
        self.go_back_button.setObjectName(u"go_back_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_back_button.sizePolicy().hasHeightForWidth())
        self.go_back_button.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(False)
        self.go_back_button.setFont(font)
        self.go_back_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-narrow-left-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.go_back_button.setIcon(icon)

        self.verticalLayout_2.addWidget(self.go_back_button)

        self.verticalSpacer_2 = QSpacerItem(17, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.categories_layout = QVBoxLayout()
        self.categories_layout.setObjectName(u"categories_layout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:rgb(250, 250, 250)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.categories_layout.addWidget(self.label_2)

        self.ajoute_categorie_button = QPushButton(Form)
        self.ajoute_categorie_button.setObjectName(u"ajoute_categorie_button")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.ajoute_categorie_button.setFont(font2)
        self.ajoute_categorie_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

        self.categories_layout.addWidget(self.ajoute_categorie_button)


        self.verticalLayout_2.addLayout(self.categories_layout)

        self.verticalSpacer = QSpacerItem(17, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(260, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.go_back_button.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Factures Precises:", None))
        self.ajoute_categorie_button.setText(QCoreApplication.translate("Form", u"+ Ajouter une categorie", None))
    # retranslateUi

