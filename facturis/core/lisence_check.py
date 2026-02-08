import sys  
import json  
from datetime import datetime  
from pathlib import Path  
from PySide6.QtWidgets import QMessageBox, QApplication  
  
def check_license_file():  
    """  
    Check if license file exists and is still valid (not expired).  
    Returns True if valid and not expired, False otherwise.  
    """  
    license_locations = [  
        Path.home() / ".facturis_license",  
        Path("C:/ProgramData/Facturis/.license"),  
        Path("/etc/facturis/.license"),  
    ]  
      
    for location in license_locations:  
        if location.exists():  
            try:  
                # Read and parse license file  
                license_data = json.loads(location.read_text())  
                  
                # Extract expiration date  
                expiration_str = license_data.get("expiration_date")  
                if not expiration_str:  
                    return False  
                  
                # Parse expiration date (format: YYYY-MM-DD)  
                expiration_date = datetime.strptime(expiration_str, "%Y-%m-%d").date()  
                  
                # Compare with current date  
                current_date = datetime.now().date()  
                  
                if current_date <= expiration_date:  
                    return True  
                else:  
                    # License expired  
                    return False  
                      
            except (json.JSONDecodeError, ValueError, KeyError):  
                # Invalid license file format  
                return False  
      
    return False  
  
def show_license_error_and_exit():  
    """Display error message and exit application."""  
    app = QApplication.instance()  
    if app is None:  
        app = QApplication(sys.argv)  
      
    QMessageBox.critical(  
        None,  
        "License Error",  
        "No valid license found or license has expired.\n"  
        "Please contact support for assistance."  
    )  
    sys.exit(1)