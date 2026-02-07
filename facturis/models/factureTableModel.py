from PySide6.QtCore import Qt, QAbstractTableModel

class FactureTableModel(QAbstractTableModel):
    headers = ["Date", "Nomero Facture", "Somme", "Note", "Status"]

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
            mapping = {
                0: facture["date_facture"],
                1: facture["numero_facture"],
                2: facture["somme"],
                3: facture["notes"],
                4: facture["status"]
            }
            return mapping.get(col)

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
