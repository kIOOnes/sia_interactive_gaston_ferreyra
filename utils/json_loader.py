import json
import os

def load_json(path):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, path)

    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)