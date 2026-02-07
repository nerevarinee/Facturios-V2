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
    QGraphicsScene
)
from PySide6.QtCore import Qt, QFile


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

        self.login = LoginWindow()
        self.main = MainWindow()
        self.facture = FactureWindow()
        self.custom_facture_window = CustomFactureWindow()
        self.browse_factures = BrowseFactures()

        self.stack.addWidget(self.login)
        self.stack.addWidget(self.main)
        self.stack.addWidget(self.facture)
        self.stack.addWidget(self.custom_facture_window)
        self.stack.addWidget(self.browse_factures)

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


    def go_to_facture(self, msg: str):
        self.facture.receive_message(msg)
        if msg == "FACTURE_PRECISEE":
            self.stack.setCurrentWidget(self.custom_facture_window)
        else:
            self.stack.setCurrentWidget(self.facture)
    def go_to_browse_factures(self, msg: str):
        self.browse_factures.receive_message(msg)
        self.stack.setCurrentWidget(self.browse_factures)

def run_app():
    app = QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec())
