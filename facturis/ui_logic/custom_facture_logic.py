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
                    f"The field name '{key}' is duplicated. Please use unique field names."
                )
                return None

            data[key] = value

        return data

    # -------------------------------------------------
    # Button handlers
    # -------------------------------------------------

    def on_paid(self):
        data = self.collect_facture_data()
        data["status"] = "paid"
        register_facture(f"{self.settings['storage_dir']}/FACTURE_PRECISEE_factures.json", data, self, facture_status="paid")
        print(data)

    def on_waitlist(self):
        data = self.collect_facture_data()
        data["status"] = "en_attente"
        register_facture(f"{self.settings['storage_dir']}/FACTURE_PRECISEE_factures.json", data, self, facture_status="en_attente")
        print(data)

    def choose_tesseract_bin(self):
        bin, _ = QFileDialog.getOpenFileName(
            self,
            "Choose where tesseract binary is located"
        )

        if bin:
            self.settings["tesseract_bin"] = bin
            QMessageBox.information(
                self,
                "Tesseract Path Set",
                f"Tesseract binary path set to: {bin}"
            )
            save_settings(self.settings)
