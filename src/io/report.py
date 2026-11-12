import csv
import os

def save_report(report_data, company_revenue):
    os.makedirs("reports", exist_ok=True)
    with open("reports/sales_report.csv", "w", newline='', encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["product", "total_quantity", "total_revenue"])

        for product_name, data in report_data.items():
            qty = data["total_quantity"]
            rvn = round(data["total_revenue"], 2)

            writer.writerow([product_name, qty, rvn])

        total_qty = 0.0
        for data in report_data.values():
            total_qty += data["total_quantity"]

        writer.writerow(["ИТОГО", total_qty, round(company_revenue, 2)])