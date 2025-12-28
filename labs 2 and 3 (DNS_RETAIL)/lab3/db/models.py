from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProductCategory(Base):
    __tablename__ = "ProductCategory"
    CategoryID = Column(Integer, primary_key=True)
    Name = Column(String(100), unique=True)

class Product(Base):
    __tablename__ = "Product"
    ProductID = Column(Integer, primary_key=True)
    Name = Column(String(150))
    Price = Column(DECIMAL(10,2))
    CategoryID = Column(Integer, ForeignKey("ProductCategory.CategoryID"))

class Store(Base):
    __tablename__ = "Store"
    StoreID = Column(Integer, primary_key=True)
    Name = Column(String(100), unique=True)
    Address = Column(String(255))


class Supplier(Base):
    __tablename__ = "Supplier"
    SupplierID = Column(Integer, primary_key=True)
    Name = Column(String(150), unique=True)


class Inventory(Base):
    __tablename__ = "Inventory"
    InventoryID = Column(Integer, primary_key=True)
    StoreID = Column(Integer, ForeignKey("Store.StoreID"))
    ProductID = Column(Integer, ForeignKey("Product.ProductID"))
    Quantity = Column(Integer)


class Supply(Base):
    __tablename__ = "Supply"
    SupplyID = Column(Integer, primary_key=True)
    SupplierID = Column(Integer, ForeignKey("Supplier.SupplierID"))
    ProductID = Column(Integer, ForeignKey("Product.ProductID"))
    SupplyDate = Column(Date)
    Quantity = Column(Integer)
