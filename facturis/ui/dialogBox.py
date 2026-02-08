from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel, QFileDialog
)

class StorageFolderDialog(QDialog):
    def __init__(self, parent=None, initial_path=""):
        super().__init__(parent)

        self.setWindowTitle("Choisir le dossier de stockage")
        self.resize(500, 120)

        self.path = initial_path

        layout = QVBoxLayout(self)

        label = QLabel("Dossier de stockage sélectionné :")
        layout.addWidget(label)

        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)
        self.line_edit.setText(initial_path)
        layout.addWidget(self.line_edit)

        button_layout = QHBoxLayout()

        browse_btn = QPushButton("Parcourir…")
        browse_btn.clicked.connect(self.choose_folder)
        button_layout.addWidget(browse_btn)

        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.accept)
        button_layout.addWidget(ok_btn)

        cancel_btn = QPushButton("Annuler")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Choisir le dossier",
            self.path
        )
        if folder:
            self.path = folder
            self.line_edit.setText(folder)
