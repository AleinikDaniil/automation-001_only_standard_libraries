import sys
import os
import config
from src.io import receiving, assembly, report as report_module
from src.processing import grouping, check, cleaning
from src.core import calculations
from src.services import errors as errors_module


folder_path = config.DATA_FOLDER
all_errors = []

found_files = receiving.find_csv_files(folder_path)
if not found_files:
    print(f"❌ ОШИБКА: В папке '{folder_path}' не найдено CSV-файлов!")
    sys.exit(1)


print("\nПроверяю структуру файлов...")
valid_files = []

for file_name in found_files:
    full_path = os.path.join(folder_path, file_name)
    is_valid, error_msg = check.check_columns(full_path)

    if is_valid:
        valid_files.append(file_name)
    else:
        print(f"⚠ Файл '{file_name}' пропущен. Причина: {error_msg}")
        all_errors.append(f"Файл '{file_name}': {error_msg}") 

if not valid_files:
    print("❌ ОШИБКА: Ни один файл не прошел проверку структуры (колонок)!")
    errors_module.save_errors(all_errors)
    sys.exit(1)

print(f"✓ Файлов, готовых к чтению: {len(valid_files)}")


print("\nНачинаю сбор данных...")
all_data = assembly.load_all_data(folder_path, valid_files)


print(f"✓ Всего прочитано строк: {len(all_data)}")


print("\nОчищаю данные...")
clean_data, cleaning_errors = cleaning.clean_data(all_data)
for err in cleaning_errors:
    print(f"⚠ {err}")
    all_errors.append(err)

print(f"✓ Осталось строк после очистки: {len(clean_data)}")


print("\nГруппирую данные...")
grouped = grouping.group_sales_by_product(clean_data)

print(f"✓ Найдено уникальных товаров: {len(grouped)}")
print("Список товаров:", list(grouped.keys()))

# Посмотрим, что лежит в ящике "Laptop"
if "Laptop" in grouped:
    print("\nДанные по товару 'Laptop':")
    for item in grouped["Laptop"]:
        print(item)

report = calculations.calculate_totals(grouped)
print("\n")
print("ОТЧЕТ ПО ТОВАРАМ")
for product_name in report:    
    qty = report[product_name]["total_quantity"]
    rvn = report[product_name]["total_revenue"]    
    print(f"  {product_name:<15} | Кол-во: {qty:<6g} | Выручка: {rvn:>8.2f}")

company_revenue = calculations.calculate_company_revenue(report)
print(f"\nОБЩАЯ ВЫРУЧКА КОМПАНИИ\n{company_revenue}")

best_product = calculations.find_best_product(report)
print(f"\nСАМЫЙ ПРИБЫЛЬНЫЙ ПРОДУКТ\nНазвание: {best_product[0]}\nВыручка за товар: {best_product[1]}")

report_module.save_report(report, company_revenue)
errors_module.save_errors(all_errors)
print("\n✓ Отчет сохранен в reports/sales_report.csv")