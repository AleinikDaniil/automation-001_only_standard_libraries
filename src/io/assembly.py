import os
import csv

def read_one_file(file_path):
    rows = []

    with open(file_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    return rows

def load_all_data(folder_path, file_names):
    all_data = []

    for name in file_names:
        full_path = os.path.join(folder_path, name)
        print(f"Читаю файл {name}...")

        file_data = read_one_file(full_path)

        all_data.extend(file_data)

    return all_data
