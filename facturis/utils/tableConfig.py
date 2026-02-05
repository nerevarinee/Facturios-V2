def tableConfig(tableWidget):
    # ---- TABLE CONFIG ----
        header = tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        header.setStretchLastSection(True)
        header.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        tableWidget.verticalHeader().setVisible(False)
        tableWidget.setSelectionBehavior(
            QTableView.SelectionBehavior.SelectRows
        )
        tableWidget.setSelectionMode(
            QTableView.SelectionMode.SingleSelection
        )
        tableWidget.setShowGrid(False)
        tableWidget.setStyleSheet("""
        QTableView {
         background-color: #0f172a;
         color: #e5e7eb;
         gridline-color: #334155;
         border: 1px solid #334155;
         font-size: 13px;
        }

        QTableView::item {
         padding: 6px;
        }

        QTableView::item:selected {
         background-color: #2563eb;
         color: white;
        }

        QHeaderView::section {
         background-color: #020617;
         color: #e5e7eb;
         padding: 8px;
         border: none;
         font-weight: bold;
        }

        QTableCornerButton::section {
         background-color: #020617;
         border: none;
        }
        """)

if __name__ == "__main__":
    pass