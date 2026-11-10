def group_sales_by_product(data):
    grouped_data = {}

    for row in data:
        product_name = row["product"]
        dublicates = []

        if product_name not in grouped_data:
            grouped_data[product_name] = []

        grouped_data[product_name].append(row)


    return grouped_data