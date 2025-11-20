import json
import os


def load_json(file_path):
    """Load JSON data from file. Return empty list if file missing."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_json(file_path, data):
    """Save Python data (list/dict) into JSON file."""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
