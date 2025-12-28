from datetime import date
from sqlalchemy.exc import IntegrityError
from db.session import SessionLocal
from db.models import (
    ProductCategory, Product, Store,
    Inventory, Supplier, Supply
)

def get_or_create(db, model, **kwargs):
    with db.no_autoflush:
        obj = db.query(model).filter_by(**kwargs).first()
        if obj:
            return obj

        obj = model(**kwargs)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj


def load(data):
    db = SessionLocal()

    for row in data:
        category = db.query(ProductCategory) \
            .filter_by(Name=row["category"]) \
            .first()

        if not category:
            category = ProductCategory(Name=row["category"])
            db.add(category)
            db.commit()
            db.refresh(category)

        product = Product(
            Name=row["product_name"],
            Price=row["price"],
            CategoryID=category.CategoryID
        )
        db.add(product)




        # --- Store ---
        store = get_or_create(
            db,
            Store,
            Name=row["store_name"],
            Address="Адрес не указан"
        )

        # --- Category ---
        category = get_or_create(
            db,
            ProductCategory,
            Name=row["category"]
        )

        # --- Supplier ---
        supplier = get_or_create(
            db,
            Supplier,
            Name=row["supplier"]
        )

        # --- Product ---
        product = Product(
            Name=row["product_name"],
            Price=row["price"],
            CategoryID=category.CategoryID
        )
        db.add(product)
        db.commit()
        db.refresh(product)

        # --- Inventory (UPSERT) ---
        inventory = db.query(Inventory).filter_by(
            StoreID=store.StoreID,
            ProductID=product.ProductID
        ).first()

        if inventory:
            inventory.Quantity += row["quantity"]
        else:
            inventory = Inventory(
                StoreID=store.StoreID,
                ProductID=product.ProductID,
                Quantity=row["quantity"]
            )
            db.add(inventory)

        # --- Supply ---
        supply = Supply(
            SupplierID=supplier.SupplierID,
            ProductID=product.ProductID,
            SupplyDate=date.today(),
            Quantity=row["quantity"]
        )
        db.add(supply)

        db.commit()

    db.close()
