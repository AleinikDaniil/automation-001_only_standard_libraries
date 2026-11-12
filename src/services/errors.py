def save_errors(errors_list):
    if not errors_list:
        return

    grouped = {
        "empty": [],
        "text": [],
        "negative": []
    }

    for err in errors_list:
        err_type = err["type"]
        if err_type in grouped:
            grouped[err_type].append(err["data"])
    
    with open("reports/errors.log", "w", encoding="utf-8")as f:
        headers = {
            "empty": "⚠ ПРОПУЩЕНЫ СТРОКИ С ПУСТЫМИ ПОЛЯМИ:",
            "text": "⚠ ПРОПУЩЕНЫ СТРОКИ С НЕКОРРЕКТНЫМИ ЧИСЛАМИ (ТЕКСТ):",
            "negative": "⚠ ПРОПУЩЕНЫ СТРОКИ С ОТРИЦАТЕЛЬНЫМИ ИЛИ НУЛЕВЫМИ ЗНАЧЕНИЯМИ:"
        }

        for err_type, items in grouped.items():
            if items:
                f.write(headers[err_type] + "\n")
                for item in items:
                    f.write(f"  {item}\n")
                f.write("\n")