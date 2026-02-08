from PySide6.QtWidgets import QWidget, QInputDialog, QPushButton, QMessageBox
from PySide6.QtCore import Signal
from facturis.ui.ui_categorie_list import Ui_Form
from facturis.core.settings import load_settings, save_settings
import json
import os

class CategoryListWindow(QWidget):
    category_selected = Signal(str)  # Emits category name

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.settings = load_settings()

        self.ui.ajoute_categorie_button.clicked.connect(self.add_category)
        self.load_categories()

    def get_categories_file(self):
        storage_dir = self.settings.get("storage_dir")
        return f"{storage_dir}/facture_precisee_categories.json"

    def load_categories(self):
        # Clear existing buttons
        layout = self.ui.categories_layout
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Load from JSON
        categories_file = self.get_categories_file()

        # Handle case where storage_dir is not set
        if not categories_file:
            return

        if os.path.exists(categories_file):
            with open(categories_file, 'r') as f:
                categories = json.load(f)
        else:
            categories = []

        # Create button for each category
        for category in categories:
            btn = QPushButton(category)
            btn.clicked.connect(lambda checked, c=category: self.category_selected.emit(c))
            layout.addWidget(btn)
            btn.setStyleSheet("color: rgb(39, 39, 39); background-color:rgb(255, 155, 3)") # Set button text color to blue

    def add_category(self):
        text, ok = QInputDialog.getText(self, "New Category", "Enter category name:")
        if ok and text:
            categories_file = self.get_categories_file()
            if os.path.exists(categories_file):
                with open(categories_file, 'r') as f:
                    categories = json.load(f)
            else:
                categories = []

            if text in categories:
                QMessageBox.warning(self, "Duplicate", "Category already exists")
                return

            categories.append(text)
            with open(categories_file, 'w') as f:
                json.dump(categories, f, indent=4)

            self.load_categories()