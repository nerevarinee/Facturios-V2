from datetime import date

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
    QGraphicsScene,
    QLineEdit,
    QLabel,

)
from PySide6.QtCore import Qt, QFile, Signal

from facturis.ui.ui_custom_facture import Ui_Form
#from facturis.resources import resources_rc
from facturis.utils.registerFacture import register_facture
from facturis.utils.factureReader import fileDataReader
from facturis.utils.fileDialog import open_file_dialog
from facturis.utils.factureImgHandler import imgHandler

from facturis.core.settings import load_settings
from facturis.core.settings import save_settings

from facturis.core.settings import load_settings


class CustomFactureWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.settings = load_settings()
        storage_dir = self.settings.get("storage_dir")
        # Load UI (DO NOT TOUCH UI FILE)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Store dynamic rows (QLabel, QLineEdit)
        self.dynamic_rows = []

        # Connect signals
        self.ui.add_facture_info.clicked.connect(self.add_form_row)
        self.ui.paidButton.clicked.connect(self.on_paid)
        self.ui.waitlistButton.clicked.connect(self.on_waitlist)
        self.annulerButton = self.ui.annulerButton
        self.ui.newFactureButton.clicked.connect(self.new_facture)
        self.ui.reglages_button.clicked.connect(self.choose_tesseract_bin)

        self.ui.fp_text_output.setText("Aucun fichier sélectionné.")

    def receive_message(self, category_name: str):
        self.category_name = category_name
        # Update any UI labels if needed
        self.ui.factureTypeLabel.setText(category_name)

    def new_facture(self):
        self.ui.numFactureField.clear()
        self.ui.sommeField.clear()
        for key_input, value_input in self.dynamic_rows:
            key_input.clear()
            value_input.clear()
        self.dynamic_rows.clear()
        file_path = open_file_dialog(self)
        tess_path = self.settings.get("tesseract_bin")
        text = fileDataReader(file_path, tess_path)
        self.ui.fp_text_output.setPlainText(text)
        imgHandler(file_path, self, self.ui.fp_img_output)

    # -------------------------------------------------
    # Dynamic QFormLayout logic
    # -------------------------------------------------

    def add_form_row(self):
      key_input = QLineEdit()
      key_input.setPlaceholderText("Field name")

      value_input = QLineEdit()
      value_input.setPlaceholderText("Value")

      self.ui.formLayout.addRow(key_input, value_input)
      self.dynamic_rows.append((key_input, value_input))

    # -------------------------------------------------
    # Data collection
    # -------------------------------------------------

    def collect_facture_data(self):
        data = {
            "date_facture": date.today().isoformat(),
            "numero_facture": self.ui.numFactureField.text(),
            "somme": self.ui.sommeField.text()
        }

        for key_input, value_input in self.dynamic_rows:
            key = key_input.text().strip()
            value = value_input.text()

            if not key:
                continue

            if key in data:
                QMessageBox.warning(
                    self,
                    "Duplicate Field",
                    f"Le champ '{key}' est dupliqué. Veuillez utiliser des noms de champs uniques."
                )
                return None

            data[key] = value

        return data

    # -------------------------------------------------
    # Button handlers
    # -------------------------------------------------

    def on_paid(self):
        data = self.collect_facture_data()
        if not data:
            QMessageBox.warning(
                self,
                "Input Error",
                "Please fill in all required fields and ensure there are no duplicate field names."
            )
        data["status"] = "paid"
        save_path = f"{self.settings['storage_dir']}/{self.category_name}_factures.json"
        QMessageBox.information(
            self,
            "Data Collected",
            f"Data saved in {save_path}"
        )
        register_facture(save_path, data, self, facture_status="paid")

    def on_waitlist(self):
        data = self.collect_facture_data()
        if not data:
            QMessageBox.warning(
                self,
                "Input Error",
                "Please fill in all required fields and ensure there are no duplicate field names."
            )
        data["status"] = "en_attente"
        save_path = f"{self.settings['storage_dir']}/{self.category_name}_factures.json"
        QMessageBox.information(
            self,
            "Data Collected",
            f"Data saved in {save_path}"
        )
        register_facture(save_path, data, self, facture_status="en_attente")

    def choose_tesseract_bin(self):
        bin, _ = QFileDialog.getOpenFileName(
            self,
            "Choisir le binaire de Tesseract",
        )

        if bin:
            self.settings["tesseract_bin"] = bin
            QMessageBox.information(
                self,
                "Tesseract Path Set",
                f"Tesseract binary path set to: {bin}"
            )
            save_settings(self.settings)
