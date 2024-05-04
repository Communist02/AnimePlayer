import os
import json


class ConfigManager:
    def __init__(self, filename):
        self.filename = filename
        if os.name == 'nt':
            self.filepath = os.path.join(os.getenv('APPDATA'), 'Anime Player', filename)
        else:
            self.filepath = os.path.join(os.getenv('HOME'), '.anime_player', filename)
        self.config = {}
        self.load_config()

    def load_config(self):
        try:
            if os.path.exists(self.filepath):
                with open(self.filepath, 'r') as file:
                    self.config = json.load(file)
        except json.decoder.JSONDecodeError:
            pass

    def save_config(self):
        if not os.path.exists(os.path.dirname(self.filepath)):
            os.makedirs(os.path.dirname(self.filepath))
        with open(self.filepath, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def delete(self, key):
        if key in self.config:
            del self.config[key]
