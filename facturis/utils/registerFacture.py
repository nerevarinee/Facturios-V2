import json
import os
from PySide6.QtWidgets import QMessageBox


def register_facture(save_location, facture_data, parent_widget, facture_status="en_attente"):
    try:
        # ensure file exists
        if not os.path.exists(save_location):
            with open(save_location, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False)

        with open(save_location, "r+", encoding="utf-8") as file:
            try:
                file_data = json.load(file)
                if not isinstance(file_data, list):
                    file_data = []
            except json.JSONDecodeError:
                # empty or invalid JSON -> start fresh
                file_data = []
            if facture_status == "paid":
                message = "est-tu sure de vouloir enregistrer cette facture? cette action est irreversible"
            else:
                message = "est-tu sure de vouloir mettre cette facture en attente? tu pourras la modifier plus tard"
            response = QMessageBox.question(
                parent_widget,
                "est-tu sure?",
                message,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if response == QMessageBox.StandardButton.No:
                return  # Do not save if user cancels
            else:
                file_data.append(facture_data)
                file.seek(0)
                file.truncate()
                json.dump(file_data, file, ensure_ascii=False, indent=4)
                QMessageBox.information(parent_widget, "Succes", "Facture traitee avec succes!")

    except Exception as e:
        QMessageBox.warning(parent_widget, "Erreur", f"Erreur lors de l'enregistrement de la facture: {e}")
        print("ERREUR register_facture:", e)