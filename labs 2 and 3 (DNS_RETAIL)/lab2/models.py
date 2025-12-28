from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from db import Base


# Справочники
class ProductCategory(Base):
    __tablename__ = "ProductCategory"
    CategoryID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False)
    products = relationship("Product", back_populates="category")


class EmployeePosition(Base):
    __tablename__ = "EmployeePosition"
    PositionID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False)
    employees = relationship("Employee", back_populates="position")


# Магазины
class Store(Base):
    __tablename__ = "Store"
    StoreID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False)
    Address = Column(String(255), nullable=False)
    employees = relationship("Employee", back_populates="store")
    sales = relationship("Sale", back_populates="store")
    inventories = relationship("Inventory", back_populates="store")


# Сотрудники
class Employee(Base):
    __tablename__ = "Employee"
    EmployeeID = Column(Integer, primary_key=True, index=True)
    FullName = Column(String(150), nullable=False)
    PositionID = Column(Integer, ForeignKey("EmployeePosition.PositionID"))
    StoreID = Column(Integer, ForeignKey("Store.StoreID"))
    position = relationship("EmployeePosition", back_populates="employees")
    store = relationship("Store", back_populates="employees")
    sales = relationship("Sale", back_populates="employee")


# Клиенты
class Customer(Base):
    __tablename__ = "Customer"
    CustomerID = Column(Integer, primary_key=True, index=True)
    FullName = Column(String(150))
    Phone = Column(String(20))
    sales = relationship("Sale", back_populates="customer")


# Товары
class Product(Base):
    __tablename__ = "Product"
    ProductID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(150), nullable=False)
    Price = Column(DECIMAL(10,2), nullable=False)
    CategoryID = Column(Integer, ForeignKey("ProductCategory.CategoryID"))
    category = relationship("ProductCategory", back_populates="products")
    sale_items = relationship("SaleItem", back_populates="product")
    supplies = relationship("Supply", back_populates="product")
    inventories = relationship("Inventory", back_populates="product")


# Продажи
class Sale(Base):
    __tablename__ = "Sale"
    SaleID = Column(Integer, primary_key=True, index=True)
    SaleDate = Column(DateTime, nullable=False)
    StoreID = Column(Integer, ForeignKey("Store.StoreID"))
    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    CustomerID = Column(Integer, ForeignKey("Customer.CustomerID"))
    store = relationship("Store", back_populates="sales")
    employee = relationship("Employee", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    items = relationship("SaleItem", back_populates="sale")


# Позиции чеков
class SaleItem(Base):
    __tablename__ = "SaleItem"
    SaleItemID = Column(Integer, primary_key=True, index=True)
    SaleID = Column(Integer, ForeignKey("Sale.SaleID"))
    ProductID = Column(Integer, ForeignKey("Product.ProductID"))
    Quantity = Column(Integer, nullable=False)
    Price = Column(DECIMAL(10,2), nullable=False)
    sale = relationship("Sale", back_populates="items")
    product = relationship("Product", back_populates="sale_items")


# Поставщики
class Supplier(Base):
    __tablename__ = "Supplier"
    SupplierID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(150), nullable=False)
    supplies = relationship("Supply", back_populates="supplier")


# Поставки
class Supply(Base):
    __tablename__ = "Supply"
    SupplyID = Column(Integer, primary_key=True, index=True)
    SupplierID = Column(Integer, ForeignKey("Supplier.SupplierID"))
    ProductID = Column(Integer, ForeignKey("Product.ProductID"))
    SupplyDate = Column(Date, nullable=False)
    Quantity = Column(Integer, nullable=False)
    supplier = relationship("Supplier", back_populates="supplies")
    product = relationship("Product", back_populates="supplies")


# Остатки
class Inventory(Base):
    __tablename__ = "Inventory"
    InventoryID = Column(Integer, primary_key=True, index=True)
    StoreID = Column(Integer, ForeignKey("Store.StoreID"))
    ProductID = Column(Integer, ForeignKey("Product.ProductID"))
    Quantity = Column(Integer, nullable=False)
    store = relationship("Store", back_populates="inventories")
    product = relationship("Product", back_populates="inventories")
