import os
import json
from typing import Any


class ConfigManager:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        if os.name == 'nt':
            self.filepath = os.path.join(
                os.getenv('APPDATA', ''), 'Anime Player', filename)
        else:
            self.filepath = os.path.join(
                os.getenv('HOME', '~'), '.config', 'Anime Player', filename)
        self.config = {}
        self.load_config()

    def load_config(self) -> None:
        try:
            if os.path.exists(self.filepath):
                with open(self.filepath, 'r') as file:
                    self.config = json.load(file)
        except json.decoder.JSONDecodeError as error:
            print(error)

    def save_config(self):
        if not os.path.exists(os.path.dirname(self.filepath)):
            os.makedirs(os.path.dirname(self.filepath))
        with open(self.filepath, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get(self, key: str, default: Any | None = None) -> Any:
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value

    def delete(self, key: str) -> None:
        if key in self.config:
            del self.config[key]
