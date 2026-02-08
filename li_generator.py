import sys  
import json  
from datetime import datetime, timedelta  
from pathlib import Path  
from PySide6.QtWidgets import (  
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,  
    QLabel, QLineEdit, QPushButton, QSpinBox, QMessageBox, QFileDialog  
)  
from PySide6.QtCore import Qt  
  
class LicenseGeneratorWindow(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("Facturis License Generator")  
        self.setMinimumWidth(400)  
          
        layout = QVBoxLayout()  
          
        # License Key field  
        key_layout = QHBoxLayout()  
        key_layout.addWidget(QLabel("License Key:"))  
        self.license_key_field = QLineEdit()  
        self.license_key_field.setPlaceholderText("Auto-generated")  
        self.license_key_field.setReadOnly(True)  
        key_layout.addWidget(self.license_key_field)  
        layout.addLayout(key_layout)  
          
        # Days Valid field  
        days_layout = QHBoxLayout()  
        days_layout.addWidget(QLabel("Days Valid:"))  
        self.days_spinbox = QSpinBox()  
        self.days_spinbox.setMinimum(1)  
        self.days_spinbox.setMaximum(3650)  # Max 10 years  
        self.days_spinbox.setValue(365)  
        days_layout.addWidget(self.days_spinbox)  
        layout.addLayout(days_layout)  
          
        # Issued To field  
        issued_layout = QHBoxLayout()  
        issued_layout.addWidget(QLabel("Issued To:"))  
        self.issued_to_field = QLineEdit()  
        self.issued_to_field.setPlaceholderText("Company/User Name")  
        issued_layout.addWidget(self.issued_to_field)  
        layout.addLayout(issued_layout)  
          
        # Expiration Date display  
        exp_layout = QHBoxLayout()  
        exp_layout.addWidget(QLabel("Expiration Date:"))  
        self.expiration_label = QLabel("")  
        exp_layout.addWidget(self.expiration_label)  
        layout.addLayout(exp_layout)  
          
        # Output Path field  
        path_layout = QHBoxLayout()  
        path_layout.addWidget(QLabel("Output Path:"))  
        self.output_path_field = QLineEdit()  
        self.output_path_field.setText(str(Path.home() / ".facturis_license"))  
        path_layout.addWidget(self.output_path_field)  
        browse_btn = QPushButton("Browse")  
        browse_btn.clicked.connect(self.browse_output_path)  
        path_layout.addWidget(browse_btn)  
        layout.addLayout(path_layout)  
          
        # Generate button  
        self.generate_btn = QPushButton("Generate License")  
        self.generate_btn.clicked.connect(self.generate_license)  
        layout.addWidget(self.generate_btn)  
          
        self.setLayout(layout)  
          
        # Connect signals  
        self.days_spinbox.valueChanged.connect(self.update_expiration_preview)  
        self.update_expiration_preview()  
      
    def update_expiration_preview(self):  
        days = self.days_spinbox.value()  
        expiration = datetime.now() + timedelta(days=days)  
        self.expiration_label.setText(expiration.strftime("%Y-%m-%d"))  
          
        # Generate preview license key  
        issue_date = datetime.now()  
        key = f"FACTURIS-{issue_date.strftime('%Y%m%d')}-{hash(str(issue_date) + str(days)) % 10000:04d}"  
        self.license_key_field.setText(key)  
      
    def browse_output_path(self):  
        file_path, _ = QFileDialog.getSaveFileName(  
            self,  
            "Save License File",  
            str(Path.home() / ".facturis_license"),  
            "All Files (*)"  
        )  
        if file_path:  
            self.output_path_field.setText(file_path)  
      
    def generate_license(self):  
        days_valid = self.days_spinbox.value()  
        issued_to = self.issued_to_field.text() or "Licensed User"  
        output_path = Path(self.output_path_field.text())  
          
        try:  
            issue_date = datetime.now()  
            expiration_date = issue_date + timedelta(days=days_valid)  
              
            license_data = {  
                "license_key": self.license_key_field.text(),  
                "expiration_date": expiration_date.strftime("%Y-%m-%d"),  
                "issued_to": issued_to,  
                "issued_date": issue_date.strftime("%Y-%m-%d"),  
                "days_valid": days_valid  
            }  
              
            output_path.write_text(json.dumps(license_data, indent=2))  
              
            QMessageBox.information(  
                self,  
                "Success",  
                f"License generated successfully!\n\n"  
                f"Location: {output_path}\n"  
                f"Valid until: {expiration_date.strftime('%Y-%m-%d')}\n"  
                f"Days: {days_valid}"  
            )  
        except Exception as e:  
            QMessageBox.critical(  
                self,  
                "Error",  
                f"Failed to generate license:\n{str(e)}"  
            )  
  
def run_license_generator():  
    app = QApplication(sys.argv)  
    window = LicenseGeneratorWindow()  
    window.show()  
    sys.exit(app.exec())  
  
if __name__ == "__main__":  
    run_license_generator()