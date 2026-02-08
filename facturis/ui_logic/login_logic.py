import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QFileDialog,
    QHeaderView,
    QTableView,
    QStackedWidget,
    QGraphicsScene,
)
from PySide6.QtCore import Qt, QFile, Signal

from facturis.ui.ui_login_window import Ui_Form
from facturis.core.settings import load_settings


class LoginWindow(QWidget):
    login_success = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.error_label.setText("")
        self.ui.password_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def handle_login(self):
        username = self.ui.user_field.text()
        password = self.ui.password_field.text()

        settings = load_settings()
        stored_username = settings.get("username", "admin")
        stored_password = settings.get("password", "password")  
  
        if username == stored_username and password == stored_password:  
            self.ui.error_label.setStyleSheet("color: green;")
            self.ui.error_label.setText("le login a réussi!")
            self.login_success.emit()
        else:
            self.ui.error_label.setStyleSheet("color: red;")
            self.ui.error_label.setText("Nom d'utilisateur ou mot de passe incorrect.")
            self.ui.error_label.setStyleSheet("color: red;")
            self.ui.error_label.setText("Nom d'utilisateur ou mot de passe incorrect.")