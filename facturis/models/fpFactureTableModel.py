from PySide6.QtCore import Qt, QAbstractTableModel  
  
class FPFactureTableModel(QAbstractTableModel):  
    headers = ["Date", "Nomero Facture", "Somme", "Information Additionnel", "Status"]  
      
    # Standard fields that get their own columns  
    standard_fields = {"date_facture", "numero_facture", "somme", "status"}  
      
    def __init__(self, factures):  
        super().__init__()  
        self.factures = factures  
      
    def rowCount(self, parent=None):  
        return len(self.factures)  
      
    def columnCount(self, parent=None):  
        return len(self.headers)  
      
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):  
        if not index.isValid():  
            return None  
          
        facture = self.factures[index.row()]  
        col = index.column()  
          
        if role == Qt.ItemDataRole.DisplayRole:  
            if col == 0:  
                return facture.get("date_facture", "")  
            elif col == 1:  
                return facture.get("numero_facture", "")  
            elif col == 2:  
                return facture.get("somme", "")  
            elif col == 3:  
                # Aggregate all dynamic fields  
                dynamic_fields = {k: v for k, v in facture.items()   
                                if k not in self.standard_fields}  
                if dynamic_fields:  
                    # Format as "key1: value1, key2: value2"  
                    return ", ".join(f"{k}: {v}" for k, v in dynamic_fields.items())  
                return ""  
            elif col == 4:  
                return facture.get("status", "")  
          
        if role == Qt.ItemDataRole.TextAlignmentRole:  
            if col in (2, 3):  
                return Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter  
            if col == 4:  
                return Qt.AlignmentFlag.AlignCenter  
          
        return None  
      
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):  
        if role != Qt.ItemDataRole.DisplayRole:  
            return None  
          
        if orientation == Qt.Orientation.Horizontal:  
            return self.headers[section]  
          
        return section + 1