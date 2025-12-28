from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas
from db import SessionLocal, engine
import logging

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="DNS_RETAIL API")

logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s %(message)s")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/categories/", response_model=schemas.ProductCategoryRead)
def create_category(category: schemas.ProductCategoryCreate, db: Session = Depends(get_db)):
    logging.info(f"POST /categories/ {category}")
    db_category = models.ProductCategory(Name=category.Name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.get("/categories/{category_id}", response_model=schemas.ProductCategoryRead)
def read_category(category_id: int, db: Session = Depends(get_db)):
    logging.info(f"GET /categories/{category_id}")
    db_category = db.query(models.ProductCategory).filter(models.ProductCategory.CategoryID == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@app.get("/categories/", response_model=list[schemas.ProductCategoryRead])
def list_categories(db: Session = Depends(get_db)):
    logging.info("GET /categories/")
    return db.query(models.ProductCategory).all()


@app.put("/categories/{category_id}", response_model=schemas.ProductCategoryRead)
def update_category(category_id: int, category: schemas.ProductCategoryCreate, db: Session = Depends(get_db)):
    logging.info(f"PUT /categories/{category_id} {category}")
    db_category = db.query(models.ProductCategory).filter(models.ProductCategory.CategoryID == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db_category.Name = category.Name
    db.commit()
    db.refresh(db_category)
    return db_category


@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    logging.info(f"DELETE /categories/{category_id}")
    db_category = db.query(models.ProductCategory).filter(models.ProductCategory.CategoryID == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return {"detail": "Category deleted"}


@app.post("/positions/", response_model=schemas.EmployeePositionRead)
def create_position(position: schemas.EmployeePositionCreate, db: Session = Depends(get_db)):
    logging.info(f"POST /positions/ {position}")
    obj = models.EmployeePosition(**position.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/positions/", response_model=list[schemas.EmployeePositionRead])
def list_positions(db: Session = Depends(get_db)):
    return db.query(models.EmployeePosition).all()


@app.get("/positions/{id}", response_model=schemas.EmployeePositionRead)
def get_position(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.EmployeePosition).get(id)
    if not obj:
        raise HTTPException(404, "Position not found")
    return obj


@app.put("/positions/{id}", response_model=schemas.EmployeePositionRead)
def update_position(id: int, position: schemas.EmployeePositionCreate, db: Session = Depends(get_db)):
    obj = db.query(models.EmployeePosition).get(id)
    if not obj:
        raise HTTPException(404, "Position not found")
    obj.Name = position.Name
    db.commit()
    return obj


@app.delete("/positions/{id}")
def delete_position(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.EmployeePosition).get(id)
    if not obj:
        raise HTTPException(404, "Position not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


@app.post("/stores/", response_model=schemas.StoreRead)
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    obj = models.Store(**store.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/stores/", response_model=list[schemas.StoreRead])
def list_stores(db: Session = Depends(get_db)):
    return db.query(models.Store).all()


@app.get("/stores/{id}", response_model=schemas.StoreRead)
def get_store(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Store).get(id)
    if not obj:
        raise HTTPException(404, "Store not found")
    return obj


@app.put("/stores/{id}", response_model=schemas.StoreRead)
def update_store(id: int, store: schemas.StoreCreate, db: Session = Depends(get_db)):
    obj = db.query(models.Store).get(id)
    if not obj:
        raise HTTPException(404, "Store not found")
    obj.Name = store.Name
    obj.Address = store.Address
    db.commit()
    return obj


@app.delete("/stores/{id}")
def delete_store(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Store).get(id)
    if not obj:
        raise HTTPException(404, "Store not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


@app.post("/employees/", response_model=schemas.EmployeeRead)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    obj = models.Employee(**emp.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/employees/", response_model=list[schemas.EmployeeRead])
def list_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()


@app.get("/employees/{id}", response_model=schemas.EmployeeRead)
def get_employee(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Employee).get(id)
    if not obj:
        raise HTTPException(404, "Employee not found")
    return obj


@app.put("/employees/{id}", response_model=schemas.EmployeeRead)
def update_employee(id: int, emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    obj = db.query(models.Employee).get(id)
    if not obj:
        raise HTTPException(404, "Employee not found")
    for k, v in emp.dict().items():
        setattr(obj, k, v)
    db.commit()
    return obj


@app.delete("/employees/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Employee).get(id)
    if not obj:
        raise HTTPException(404, "Employee not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


@app.post("/customers/", response_model=schemas.CustomerRead)
def create_customer(c: schemas.CustomerCreate, db: Session = Depends(get_db)):
    obj = models.Customer(**c.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/customers/", response_model=list[schemas.CustomerRead])
def list_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()


@app.get("/customers/{id}", response_model=schemas.CustomerRead)
def get_customer(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Customer).get(id)
    if not obj:
        raise HTTPException(404, "Customer not found")
    return obj


@app.put("/customers/{id}", response_model=schemas.CustomerRead)
def update_customer(id: int, c: schemas.CustomerCreate, db: Session = Depends(get_db)):
    obj = db.query(models.Customer).get(id)
    if not obj:
        raise HTTPException(404, "Customer not found")
    for k, v in c.dict().items():
        setattr(obj, k, v)
    db.commit()
    return obj


@app.delete("/customers/{id}")
def delete_customer(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Customer).get(id)
    if not obj:
        raise HTTPException(404, "Customer not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


@app.post("/products/", response_model=schemas.ProductRead)
def create_product(p: schemas.ProductCreate, db: Session = Depends(get_db)):
    obj = models.Product(**p.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/products/", response_model=list[schemas.ProductRead])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


@app.get("/products/{id}", response_model=schemas.ProductRead)
def get_product(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Product).get(id)
    if not obj:
        raise HTTPException(404, "Product not found")
    return obj


@app.put("/products/{id}", response_model=schemas.ProductRead)
def update_product(id: int, p: schemas.ProductCreate, db: Session = Depends(get_db)):
    obj = db.query(models.Product).get(id)
    if not obj:
        raise HTTPException(404, "Product not found")
    for k, v in p.dict().items():
        setattr(obj, k, v)
    db.commit()
    return obj


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Product).get(id)
    if not obj:
        raise HTTPException(404, "Product not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


@app.post("/sales/", response_model=schemas.SaleRead)
def create_sale(s: schemas.SaleCreate, db: Session = Depends(get_db)):
    obj = models.Sale(**s.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.post("/sales/", response_model=schemas.SaleRead)
def create_sale(s: schemas.SaleCreate, db: Session = Depends(get_db)):
    obj = models.Sale(**s.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/sales/", response_model=list[schemas.SaleRead])
def list_sales(db: Session = Depends(get_db)):
    return db.query(models.Sale).all()


@app.get("/sales/{id}", response_model=schemas.SaleRead)
def get_sale(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Sale).get(id)
    if not obj:
        raise HTTPException(404, "Sale not found")
    return obj


@app.put("/sales/{id}", response_model=schemas.SaleRead)
def update_sale(id: int, s: schemas.SaleCreate, db: Session = Depends(get_db)):
    obj = db.query(models.Sale).get(id)
    if not obj:
        raise HTTPException(404, "Sale not found")
    for k, v in s.dict().items():
        setattr(obj, k, v)
    db.commit()
    return obj


@app.delete("/sales/{id}")
def delete_sale(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Sale).get(id)
    if not obj:
        raise HTTPException(404, "Sale not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


@app.post("/sale-items/", response_model=schemas.SaleItemRead)
def create_sale_item(si: schemas.SaleItemCreate, db: Session = Depends(get_db)):
    obj = models.SaleItem(**si.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/sale-items/", response_model=list[schemas.SaleItemRead])
def list_sale_items(db: Session = Depends(get_db)):
    return db.query(models.SaleItem).all()


@app.get("/sale-items/{id}", response_model=schemas.SaleItemRead)
def get_sale_item(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.SaleItem).get(id)
    if not obj:
        raise HTTPException(404, "Sale item not found")
    return obj


@app.put("/sale-items/{id}", response_model=schemas.SaleItemRead)
def update_sale_item(id: int, si: schemas.SaleItemCreate, db: Session = Depends(get_db)):
    obj = db.query(models.SaleItem).get(id)
    if not obj:
        raise HTTPException(404, "Sale item not found")
    for k, v in si.dict().items():
        setattr(obj, k, v)
    db.commit()
    return obj


@app.delete("/sale-items/{id}")
def delete_sale_item(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.SaleItem).get(id)
    if not obj:
        raise HTTPException(404, "Sale item not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


@app.post("/supplies/", response_model=schemas.SupplyRead)
def create_supply(s: schemas.SupplyCreate, db: Session = Depends(get_db)):
    obj = models.Supply(**s.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/supplies/", response_model=list[schemas.SupplyRead])
def list_supplies(db: Session = Depends(get_db)):
    return db.query(models.Supply).all()


@app.get("/supplies/{id}", response_model=schemas.SupplyRead)
def get_supply(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Supply).get(id)
    if not obj:
        raise HTTPException(404, "Supply not found")
    return obj


@app.put("/supplies/{id}", response_model=schemas.SupplyRead)
def update_supply(id: int, s: schemas.SupplyCreate, db: Session = Depends(get_db)):
    obj = db.query(models.Supply).get(id)
    if not obj:
        raise HTTPException(404, "Supply not found")
    for k, v in s.dict().items():
        setattr(obj, k, v)
    db.commit()
    return obj


@app.delete("/supplies/{id}")
def delete_supply(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Supply).get(id)
    if not obj:
        raise HTTPException(404, "Supply not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


@app.post("/inventory/", response_model=schemas.InventoryRead)
def create_inventory(i: schemas.InventoryCreate, db: Session = Depends(get_db)):
    obj = models.Inventory(**i.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/inventory/", response_model=list[schemas.InventoryRead])
def list_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()


@app.get("/inventory/{id}", response_model=schemas.InventoryRead)
def get_inventory(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Inventory).get(id)
    if not obj:
        raise HTTPException(404, "Inventory not found")
    return obj


@app.put("/inventory/{id}", response_model=schemas.InventoryRead)
def update_inventory(id: int, i: schemas.InventoryCreate, db: Session = Depends(get_db)):
    obj = db.query(models.Inventory).get(id)
    if not obj:
        raise HTTPException(404, "Inventory not found")
    for k, v in i.dict().items():
        setattr(obj, k, v)
    db.commit()
    return obj


@app.delete("/inventory/{id}")
def delete_inventory(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Inventory).get(id)
    if not obj:
        raise HTTPException(404, "Inventory not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}

