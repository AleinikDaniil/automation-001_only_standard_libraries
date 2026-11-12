def clean_data(data):
    clean_rows = []
    errors = []

    for row in data:
        pdt = row["product"].strip()
        qty = row["quantity"].strip()
        prc = row["price"].strip()

        if not pdt or not qty or not prc:
            errors.append({
                "type": "empty",
                "data": f"Товар='{pdt}', Кол-во='{qty}', Цена='{prc}'"
            })
            continue

        try:
            qty_float = float(qty)
            prc_float = float(prc)

            if qty_float <= 0 or prc_float <= 0:
                errors.append({
                    "type": "negative",
                    "data": f"Товар='{pdt}', Кол-во={qty_float}, Цена={prc_float}"
                })
                continue
        except ValueError:
            errors.append({
                "type": "text",
                "data": f"Товар='{pdt}', Кол-во='{qty}', Цена='{prc}'"
            })
            continue

        clean_rows.append(row)

    return clean_rows, errors

