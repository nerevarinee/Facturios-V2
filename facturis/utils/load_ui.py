def load_ui(path: str):
    loader = QUiLoader()
    ui_file = QFile(path)

    if not ui_file.open(QFile.ReadOnly):
        raise RuntimeError(f"Cannot open UI file: {path}")

    ui = loader.load(ui_file)
    ui_file.close()

    if ui is None:
        raise RuntimeError(f"Failed to load UI file: {path}")

    return ui

if __name__ == "__main__":
    pass