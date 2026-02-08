from ast import main
import sys
from turtle import color

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
from PySide6.QtCore import Qt, QFile
from PySide6.QtGui import QIcon

from facturis.core.settings import load_settings
from facturis.ui_logic.category_list_logic import CategoryListWindow
from facturis.ui_logic.register_logic import RegisterWindow
from facturis.ui_logic.login_logic import LoginWindow
from facturis.ui_logic.main_logic import MainWindow
from facturis.ui_logic.facture_logic import FactureWindow
from facturis.ui_logic.custom_facture_logic import CustomFactureWindow
from facturis.ui_logic.browse_factures_logic import BrowseFactures

from facturis.core.paths import SETTINGS_FILE

from facturis.resources import resources_rc


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(u"background-color:rgb(0, 85, 255)")

        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.register = RegisterWindow()
        self.login = LoginWindow()
        self.main = MainWindow()
        self.facture = FactureWindow()
        self.custom_facture_window = CustomFactureWindow()
        self.browse_factures = BrowseFactures()
        self.category_list = CategoryListWindow()

        self.stack.addWidget(self.register)
        self.stack.addWidget(self.login)
        self.stack.addWidget(self.main)
        self.stack.addWidget(self.facture)
        self.stack.addWidget(self.custom_facture_window)
        self.stack.addWidget(self.browse_factures)
        self.stack.addWidget(self.category_list)

        # In __init__:

        # Wire up signals
        self.category_list.category_selected.connect(self.go_to_custom_facture_with_category)
        self.category_list.ui.go_back_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main)
        )

        # Wire registration success to show login
        self.register.registration_success.connect(
            lambda: self.stack.setCurrentWidget(self.login)
        )

        # navigation wiring
        self.login.login_success.connect(
            lambda: self.stack.setCurrentWidget(self.main)
        )

        self.main.message_signal.connect(self.go_to_facture)
        self.main.data_message_signal.connect(self.go_to_browse_factures)
        self.facture.annulerButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main)
        )
        self.custom_facture_window.annulerButton.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main)
        )
        self.browse_factures.ui.go_back_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main)
        )
        self.facture.ui.go_back_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main)
        )
        self.custom_facture_window.ui.go_back_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main)
        )
        if self.user_exists():
            self.stack.setCurrentWidget(self.login)
        else:
            self.stack.setCurrentWidget(self.register)

    # At the end of __init__, after all signal connections:

# Check if user already exists and show appropriate screen


    def user_exists(self):
    # This depends on how your RegisterWindow stores user data
    # Common approaches
    # 1. Check if a user credentials file exists
    # 2. Check settings for a registered user flag
    # 3. Query a database

    # Example implementation (adjust based on your actual storage)
        try:
            settings = load_settings()
            return settings.get("account_registered", False)
        except:
            return False
    def go_to_facture(self, msg: str):
        if msg == "FACTURE_PRECISEE":
            # Disconnect any previous signal connections
            try:
                self.category_list.category_selected.disconnect()
            except:
                pass
        # Reconnect to facture creation handler
            self.category_list.category_selected.connect(self.go_to_custom_facture_with_category)
            self.stack.setCurrentWidget(self.category_list)
        else:
            self.facture.receive_message(msg)
            self.stack.setCurrentWidget(self.facture)

    def go_to_browse_factures(self, msg: str):
        if msg == "FACTURE_PRECISEE":
            self.stack.setCurrentWidget(self.category_list)
        # Disconnect previous signal and reconnet for browse
            try:
                self.category_list.category_selected.disconnect()
            except:
                pass
            self.category_list.category_selected.connect(self.go_to_browse_with_category)
        else:
            self.browse_factures.receive_message(msg)
            self.stack.setCurrentWidget(self.browse_factures)

    def go_to_browse_with_category(self, category_name: str):
        self.browse_factures.receive_message(category_name)
        self.stack.setCurrentWidget(self.browse_factures)

    def go_to_custom_facture_with_category(self, category_name: str):
        self.custom_facture_window.receive_message(category_name)
        self.stack.setCurrentWidget(self.custom_facture_window)

def run_app():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))

    # Apply global stylesheet for all message boxes
    app.setStyleSheet("""
        QMessageBox {
            background-color: #1e293b;
            color: #e5e7eb;
        }
        QMessageBox QLabel {
            color: #e5e7eb;
            font-size: 13px;
        }
        QMessageBox QPushButton {
            background-color: #2563eb;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
        }
        QMessageBox QPushButton:hover {
            background-color: #1d4ed8;
        }
        QMessageBox QPushButton:pressed {
            background-color: #1e40af;
        }
    """)

    w = MainApp()
    w.show()
    sys.exit(app.exec())
