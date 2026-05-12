import yaml
import os
import sys

# Esto asegura que la carpeta raíz del nodo esté en el path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

class Settings:
    def __init__(self):
        # Buscamos el yaml en la misma carpeta que este script
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, "node.yaml")
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"No se encontró node.yaml en {config_path}")
            
        with open(config_path, "r") as f:
            self._data = yaml.safe_load(f)

    def get(self, path, default=None):
        keys = path.split(".")
        val = self._data
        try:
            for key in keys:
                val = val[key]
            return val
        except (KeyError, TypeError):
            return default

settings = Settings()