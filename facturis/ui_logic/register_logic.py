import configparser
from logging import config
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit
from facturis.ui.ui_register import Ui_Form
from facturis.core.settings import load_settings, save_settings

class RegisterWindow(QWidget):
    registration_success = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect your register button (adjust button name as needed)
        self.ui.enrigstre_button.clicked.connect(self.handle_registration)
        self.ui.password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.password_field_2.setEchoMode(QLineEdit.EchoMode.Password)

    def handle_registration(self):
        username = self.ui.user_field.text()
        password = self.ui.password_field.text()
        confirm_password = self.ui.password_field_2.text()

        # Validate inputs
        if not username or not password:
            QMessageBox.warning(self, "Error", "Veulliez remplir tous les champs")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Mot de passe de confirmation ne correspond pas")
            return

        # Save credentials to settings
        settings = load_settings()
        settings["account_registered"] = True
        settings["username"] = username
        settings["password"] = password
        save_settings(settings)

        QMessageBox.information(self, "Success", "Compte enregistré avec succès!")
        self.registration_success.emit()