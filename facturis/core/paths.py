# facturis/core/paths.py

from pathlib import Path

APP_DIR = Path.home() / ".facturis"
SETTINGS_FILE = APP_DIR / "settings.json"

DEFAULT_STORAGE_DIR = Path.home() / "FacturisData"
