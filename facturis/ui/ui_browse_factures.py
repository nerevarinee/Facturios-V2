# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browse_factures.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 500)
        Form.setStyleSheet(u"background-color:rgb(0, 85, 255)")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.go_back_button = QPushButton(Form)
        self.go_back_button.setObjectName(u"go_back_button")
        self.go_back_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-narrow-left-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.go_back_button.setIcon(icon)

        self.verticalLayout_7.addWidget(self.go_back_button)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.facture_type_label = QLabel(Form)
        self.facture_type_label.setObjectName(u"facture_type_label")
        font = QFont()
        font.setPointSize(12)
        self.facture_type_label.setFont(font)
        self.facture_type_label.setStyleSheet(u"color:white")
        self.facture_type_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_7.addWidget(self.facture_type_label)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white")

        self.horizontalLayout_3.addWidget(self.label)

        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet(u"background-color:white")
        self.dateEdit.setDateTime(QDateTime(QDate(2026, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setMaximumDateTime(QDateTime(QDate(2050, 1, 1), QTime(22, 59, 59)))
        self.dateEdit.setMinimumDateTime(QDateTime(QDate(2025, 12, 31), QTime(23, 0, 0)))

        self.horizontalLayout_3.addWidget(self.dateEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.paid_radio_button = QRadioButton(Form)
        self.paid_radio_button.setObjectName(u"paid_radio_button")
        self.paid_radio_button.setStyleSheet(u"color:white")

        self.verticalLayout_2.addWidget(self.paid_radio_button)

        self.waitlist_radio_button = QRadioButton(Form)
        self.waitlist_radio_button.setObjectName(u"waitlist_radio_button")
        self.waitlist_radio_button.setStyleSheet(u"color:white")

        self.verticalLayout_2.addWidget(self.waitlist_radio_button)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.affiche_button = QPushButton(Form)
        self.affiche_button.setObjectName(u"affiche_button")
        font2 = QFont()
        font2.setPointSize(11)
        self.affiche_button.setFont(font2)
        self.affiche_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

        self.verticalLayout_4.addWidget(self.affiche_button)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white")

        self.verticalLayout_5.addWidget(self.label_3)

        self.modify_status_input_field = QLineEdit(Form)
        self.modify_status_input_field.setObjectName(u"modify_status_input_field")
        self.modify_status_input_field.setStyleSheet(u"background-color:white")

        self.verticalLayout_5.addWidget(self.modify_status_input_field)

        self.set_paid_button = QPushButton(Form)
        self.set_paid_button.setObjectName(u"set_paid_button")
        self.set_paid_button.setFont(font2)
        self.set_paid_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")

        self.verticalLayout_5.addWidget(self.set_paid_button)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_bar = QLineEdit(Form)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setStyleSheet(u"background-color:white")

        self.horizontalLayout.addWidget(self.search_bar)

        self.search_button = QPushButton(Form)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/search-alt-1-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.search_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.refresh_button = QPushButton(Form)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setStyleSheet(u"color:rgb(39, 39, 39); background-color:rgb(255, 155, 3);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/refresh-cw-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.refresh_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color:white")

        self.verticalLayout.addWidget(self.tableView)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(3, 10)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.go_back_button.setText("")
        self.facture_type_label.setText(QCoreApplication.translate("Form", u"TYPE DE FACTURE", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Filtres les factures:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Avant de :", None))
        self.paid_radio_button.setText(QCoreApplication.translate("Form", u"Paye", None))
        self.waitlist_radio_button.setText(QCoreApplication.translate("Form", u"En attente", None))
        self.affiche_button.setText(QCoreApplication.translate("Form", u"Affiche", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Modifier une facture:", None))
        self.modify_status_input_field.setInputMask("")
        self.set_paid_button.setText(QCoreApplication.translate("Form", u"Paiee", None))
        self.search_bar.setInputMask("")
        self.search_button.setText("")
        self.refresh_button.setText("")
    # retranslateUi

