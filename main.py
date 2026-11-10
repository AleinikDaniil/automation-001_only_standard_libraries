import config
import src.receiving as receiving
import src.assembly as assembly
import src.grouping as grouping


folder_path = config.DATA_FOLDER

found_files = receiving.find_csv_files(folder_path)

print("\nНачинаю сбор данных...")
all_data = assembly.load_all_data(folder_path, found_files)

print("\n" + "="*30)
print(f"✓ Всего прочитано строк: {len(all_data)}")
print("Первая строка для проверки:")
print(all_data[0])


print("\nГруппирую данные...")
grouped = grouping.group_sales_by_product(all_data)

print(f"✓ Найдено уникальных товаров: {len(grouped)}")
print("Список товаров:", list(grouped.keys()))

# Посмотрим, что лежит в ящике "Laptop"
if "Laptop" in grouped:
    print("\nДанные по товару 'Laptop':")
    for item in grouped["Laptop"]:
        print(item)

print(grouped)