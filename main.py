import config
import src.receiving as receiving
import src.assembly as assembly
import src.grouping as grouping
import src.calculations as calculations
import src.report as report_module


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
print("\n✓ Отчет сохранен в reports/sales_report.csv")