import os

def find_csv_files(folder_path):
    items = os.listdir(folder_path)
    csv_files = []

    for item in items:
        if item.lower().endswith(".csv"):
            full_pass = os.path.join(folder_path, item)
            if os.path.isfile(full_pass):
                csv_files.append(item)

    print(f"Найдено файлов: {len(csv_files)}")
    print(csv_files)

    return csv_files