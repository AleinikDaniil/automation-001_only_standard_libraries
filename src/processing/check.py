import csv

def check_columns(file_path):
    with open(file_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        if columns == None:
            return (False, "Файл пуст")
        
        required = ["product", "quantity", "price"]

        for column_name in required:
            if column_name not in columns:
                return (False, f"Нет колонки {column_name}")

    return (True, "")
