import json
from pathlib import Path

SETTINGS_PATH = Path.home() / ".facturis_settings.json"

def load_settings():
    if SETTINGS_PATH.exists():
        return json.loads(SETTINGS_PATH.read_text())
    return {}

def save_settings(data: dict):
    SETTINGS_PATH.write_text(json.dumps(data, indent=2))
