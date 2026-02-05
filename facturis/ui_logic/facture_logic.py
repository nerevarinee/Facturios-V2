from datetime import date
from logging import NullHandler
import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QMessageBox,
    QFileDialog,
    QHeaderView,
    QTableView,
    QStackedWidget,
    QGraphicsScene
)
from PySide6.QtCore import Qt, QFile

from facturis.ui.ui_facture import Ui_Form
#from facturis.resources import resources_rc

from facturis.core.settings import load_settings

from facturis.utils.factureImgHandler import imgHandler
from facturis.utils.fileDialog import open_file_dialog
from facturis.utils.registerFacture import register_facture

class FactureWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.settings = load_settings()
        storage_dir = self.settings.get("storage_dir")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.resize(1080, 640)

        self.setWindowTitle("Facturis - Facture Window")
        self.ui.paidButton.clicked.connect(self.on_paid)
        self.ui.waitlistButton.clicked.connect(self.on_waitlist)
        self.annulerButton = self.ui.annulerButton
        self.ui.newFactureButton.clicked.connect(self.new_facture)

    def receive_message(self, msg: str):
        self.ui.factureTypeLabel.setText(msg)
    def collect_facture_data(self):
        data = {
            "date_facture": date.today().isoformat(),
            "numero_facture": self.ui.numFactureField.text(),
            "somme": self.ui.sommeField.text(),
            "notes": self.ui.noteField.toPlainText()
        }
        return data
    def on_paid(self):
        data = self.collect_facture_data()
        data["status"] = "paid"
        save_path = f"{self.settings['storage_dir']}/{self.ui.factureTypeLabel.text()}_factures.json"
        register_facture(save_path, data, self, facture_status="paid")
        print(data)
    def on_waitlist(self):
        data = self.collect_facture_data()
        data["status"] = "en_attente"
        save_path = f"{self.settings['storage_dir']}/{self.ui.factureTypeLabel.text()}_factures.json"
        register_facture(save_path, data, self, facture_status="en_attente")
        print(data)

    def new_facture(self):
        self.ui.numFactureField.clear()
        self.ui.sommeField.clear()
        self.ui.noteField.clear()
        file_path = open_file_dialog(self)
        imgHandler(file_path, self, self.ui.graphicsView)