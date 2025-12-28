import math
from utils.logger import logger

def transform(df):
    valid_data = []
    errors = []

    df["category"] = df["category"].astype(str).str.strip().str.capitalize()
    df["store_name"] = df["store_name"].astype(str).str.strip()
    df["product_name"] = df["product_name"].astype(str).str.strip()
    df["supplier"] = df["supplier"].astype(str).str.strip()

    for idx, row in df.iterrows():
        try:
            # --- обязательные поля ---
            if not row["store_name"] or row["store_name"] == "nan":
                raise ValueError("store_name пустой")

            if not row["product_name"] or row["product_name"] == "nan":
                raise ValueError("product_name пустой")

            if not row["category"] or row["category"] == "nan":
                raise ValueError("category пустая")

            if not row["supplier"] or row["supplier"] == "nan":
                raise ValueError("supplier пустой")

            # --- числовые поля ---
            price = float(row["price"])
            quantity = int(row["quantity"])

            if math.isnan(price) or price <= 0:
                raise ValueError("Цена некорректна")

            if quantity < 0:
                raise ValueError("Количество отрицательное")

            valid_data.append({
                "store_name": row["store_name"],
                "product_name": row["product_name"],
                "category": row["category"],
                "price": price,
                "quantity": quantity,
                "supplier": row["supplier"]
            })

        except Exception as e:
            logger.error(f"Transform error (row {idx}): {e}")
            errors.append({
                "row": idx,
                "error": str(e)
            })

    return valid_data, errors
