import os


def load_data(filename):
    base_dir = os.path.dirname(__file__)  # директорія, де лежить data.py
    full_path = os.path.join(base_dir, filename)
    with open(full_path, "r", encoding="utf-8") as file:
        return file.readlines()


def clean_data(temperature_data: list[str]) -> list[float]:
    return [float(temp.strip()) for temp in temperature_data if temp.strip()]
