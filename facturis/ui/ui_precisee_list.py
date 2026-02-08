# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prescisee_list.ui'
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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(252, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(17, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(121, 121, 121)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(250, 250, 250)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.facturePreciseeButton_3 = QPushButton(self.frame)
        self.facturePreciseeButton_3.setObjectName(u"facturePreciseeButton_3")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.facturePreciseeButton_3.setFont(font1)
        self.facturePreciseeButton_3.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

        self.verticalLayout.addWidget(self.facturePreciseeButton_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(17, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(251, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Factures Precises:", None))
        self.facturePreciseeButton_3.setText(QCoreApplication.translate("Form", u"+ Ajouter une categorie", None))
    # retranslateUi

