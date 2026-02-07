import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QHeaderView,
    QTableView,
    QStackedWidget,
    QGraphicsScene
)

from facturis.core.settings import load_settings
from facturis.core.settings import save_settings
from facturis.core.paths import SETTINGS_FILE

from facturis.ui.ui_main import Ui_Form

class MainWindow(QWidget):
    message_signal = Signal(str)
    data_message_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.settings = load_settings()
        storage_dir = self.settings.get("storage_dir")
        if storage_dir:
            self.ui.storagePathLineEdit.setText(storage_dir)

        self.setWindowTitle("Facturis")
        self.resize(800, 600)

        self.ui.sonelgazeButton.clicked.connect(lambda: self.navigate_to_facture("SONELGAZE"))
        self.ui.adeButton.clicked.connect(lambda: self.navigate_to_facture("ADE"))
        self.ui.telecomButton.clicked.connect(lambda: self.navigate_to_facture("TELECOM"))
        self.ui.facturePreciseeButton.clicked.connect(lambda: self.navigate_to_facture("FACTURE_PRECISEE"))

        self.ui.data_sonelgazeButton.clicked.connect(lambda: self.navigate_to_browse_factures("SONELGAZE"))
        self.ui.data_adeButton.clicked.connect(lambda: self.navigate_to_browse_factures("ADE"))
        self.ui.data_telecomButton.clicked.connect(lambda: self.navigate_to_browse_factures("TELECOM"))
        self.ui.data_facturePreciseeButton.clicked.connect(lambda: self.navigate_to_browse_factures("FACTURE_PRECISEE"))

        self.ui.parametres_button.clicked.connect(self.choose_save_folder)

    def navigate_to_facture(self, nav_msg: str):
        self.message_signal.emit(nav_msg)
    def navigate_to_browse_factures(self, nav_msg: str):
        self.data_message_signal.emit(nav_msg)

    def choose_save_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Choose where files will be saved"
        )

        if folder:
            self.settings["storage_dir"] = folder
            QMessageBox.information(
                self,
                "Storage Directory Set",
                f"Storage directory set to: {folder}"
            )
            self.ui.storagePathLineEdit.setText(folder)
            save_settings(self.settings)
