from datetime import datetime
from logging import NullHandler
import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QWidget,
    QMainWindow,
    QMessageBox,
    QFileDialog,
    QHeaderView,
    QTableView,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QGraphicsScene,
    QDateEdit,
    QRadioButton,
    QLineEdit,
)
from PySide6.QtCore import Qt, QFile, Signal, Slot, QObject

from facturis.ui.ui_browse_factures import Ui_Form
from facturis.utils.loadDataFromJsonFile import loadDataFromJsonFile
from facturis.models.factureTableModel import FactureTableModel
from facturis.models.fpFactureTableModel import FPFactureTableModel

from facturis.core.settings import load_settings
from facturis.utils.saveDataToJsonFile import saveDataToJsonFile

class BrowseFactures(QWidget):
    message_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.settings = load_settings()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Facturis - Browse Factures")
        self.resize(800, 600)
        self.ui.refresh_button.clicked.connect(self.load_factures)

        #self.load_factures()

        self.ui.set_paid_button.clicked.connect(self.set_facture_paid)

        self.ui.dateEdit
        self.ui.paid_radio_button
        self.ui.waitlist_radio_button
        self.ui.affiche_button.clicked.connect(self.apply_filters)

        self.ui.tableView.setSelectionBehavior(QTableView.SelectItems)
        self.ui.tableView.setSelectionMode(QTableView.ExtendedSelection)
        self.ui.tableView.setEditTriggers(QTableView.NoEditTriggers)

    def copy_selection(self):
        selection = self.ui.tableView.selectionModel().selectedIndexes()
        if not selection:
            return

        rows = {}
        for index in selection:
            rows.setdefault(index.row(), {})[index.column()] = index.data()
        text = ""
        for row in sorted(rows):
            row_data = rows[row]
            text += "\t".join(
            str(row_data[col]) for col in sorted(row_data)
            ) + "\n"

        QApplication.clipboard().setText(text)

        self.ui.tableView.keyPressEvent = lambda event: (
            self.copy_selection() if event.matches(QKeySequence.Copy)
            else QTableView.keyPressEvent(self.ui.tableView, event)
        )

    def receive_message(self, msg: str):
        self.ui.facture_type_label.setText(msg)
        return msg

    def get_data_source_path(self):
        storage_dir = self.settings.get("storage_dir")
        if not storage_dir:
            QMessageBox.warning(
                self,
                "Storage Directory Not Set",
                "Please set the storage directory in the main window settings."
            )
            return None
        self.source_path = f"{storage_dir}/{self.ui.facture_type_label.text()}_factures.json"
        print("Data source path:", self.source_path)
        return self.source_path

    def load_factures(self):
        data_source = self.get_data_source_path()
        try:
            self.all_factures = loadDataFromJsonFile(data_source)
            if self.ui.facture_type_label.text() == "FACTURE_PRECISEE":
                self.model = FPFactureTableModel(self.all_factures)
            else:
                self.model = FactureTableModel(self.all_factures)
            self.ui.tableView.setModel(self.model)
            QMessageBox.information(
                self,
                "Success",
                f"Factures loaded successfully from {data_source}.")
        except Exception as e:
            #print(f"Error loading factures from {data_source}: {e}")
            QMessageBox.critical(self, "Error", f"Failed to load factures: {e}")
            return []

    def set_facture_paid(self):
        facture_number = self.ui.modify_status_input_field.text().strip()

        if not facture_number:
            QMessageBox.warning(
                self,
                "Input Error",
                "Please enter a facture number."
            )
            return

        data_source = self.get_data_source_path()

        try:
            factures = loadDataFromJsonFile(data_source)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        facture_found = False

        for facture in factures:
            if facture.get("numero_facture") == facture_number:
                facture["status"] = "paid"
                facture_found = True
                break

        if not facture_found:
            QMessageBox.warning(
                self,
                "Not found",
                f"Facture {facture_number} not found."
            )
            return

        saveDataToJsonFile(data_source, factures)

        QMessageBox.information(
            self,
            "Success",
            f"Facture {facture_number} marked as PAID."
        )

        self.load_factures()

    def apply_filters(self):
        filtered = []

        qdate = self.ui.dateEdit.date()
        selected_date = qdate.toPython() if hasattr(qdate, 'toPython') else qdate.toDate().toPython() if hasattr(qdate, 'toDate') else qdate
        filter_paid = self.ui.paid_radio_button.isChecked()
        filter_pending = self.ui.waitlist_radio_button.isChecked()

        for facture in self.all_factures:
            # --- DATE FILTER ---
            facture_date = datetime.strptime(
            facture["date_facture"], "%Y-%m-%d"
            ).date()

            if facture_date > selected_date:
                continue

            # --- STATUS FILTER ---
            status = facture.get("status", "pending")

            if filter_paid and status != "paid":
                continue

            if filter_pending and status != "en_attente":
                continue

            filtered.append(facture)

        self.model = FactureTableModel(filtered)
        self.ui.tableView.setModel(self.model)