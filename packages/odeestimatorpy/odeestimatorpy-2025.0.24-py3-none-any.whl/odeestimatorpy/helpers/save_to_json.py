import json
import multiprocessing
import os

lock = multiprocessing.Lock()

def save_json(data, file_path):
    with lock:
        try:
            with open(file_path, "r") as f:
                content = f.read().strip()
                existing_data = json.loads(content)
        except FileNotFoundError:
            existing_data = []

        if any(data["ID"] == item["ID"] for item in existing_data):
            return

        existing_data.append(data)

        with open(file_path, "w") as f:
            json.dump(existing_data, f, indent=2)


def save_new_json(data, file_path):
    """Save JSON data to a new file."""

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)