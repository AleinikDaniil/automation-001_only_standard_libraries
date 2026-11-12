def calculate_totals(grouped_data):
    report = {}

    for product_name, rows in grouped_data.items():
        total_quantity = 0
        total_revenue = 0

        for row in rows:
            qty = float(row["quantity"]) 
            total_quantity += qty

            rvn = qty * float(row["price"])
            total_revenue += rvn

        report[product_name] = {"total_quantity": total_quantity, "total_revenue": total_revenue}    

    return report

def calculate_company_revenue(report):
    total_company_revenue = 0.0

    for product_name, data in report.items():
        total_company_revenue += data["total_revenue"]

    return total_company_revenue

def find_best_product(report):
    best_product_name = None
    best_product_revenue = -1.0

    for product_name, data in report.items():
        rvn = data["total_revenue"] 
        
        if rvn > best_product_revenue:
            best_product_name = product_name
            best_product_revenue = data["total_revenue"]

    return best_product_name, best_product_revenue