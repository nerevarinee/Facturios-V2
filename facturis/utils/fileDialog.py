import re
from PySide6.QtWidgets import QFileDialog, QWidget

def open_file_dialog(parent_widget: QWidget):
        file_path, _ = QFileDialog.getOpenFileName(
            parent_widget,
            "Sélectionner une facture",
            "",
            "Images / PDF (*.*)",
        )
        return file_path