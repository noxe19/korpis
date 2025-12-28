from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date


# --- ProductCategory ---
class ProductCategoryBase(BaseModel):
    Name: str = Field(..., max_length=100)


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryRead(ProductCategoryBase):
    CategoryID: int

    class Config:
        orm_mode = True


# --- EmployeePosition ---
class EmployeePositionBase(BaseModel):
    Name: str = Field(..., max_length=100)


class EmployeePositionCreate(EmployeePositionBase):
    pass


class EmployeePositionRead(EmployeePositionBase):
    PositionID: int

    class Config:
        orm_mode = True


# --- Store ---
class StoreBase(BaseModel):
    Name: str
    Address: str


class StoreCreate(StoreBase):
    pass


class StoreRead(StoreBase):
    StoreID: int

    class Config:
        orm_mode = True


# --- Employee ---
class EmployeeBase(BaseModel):
    FullName: str
    PositionID: int
    StoreID: int


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeRead(EmployeeBase):
    EmployeeID: int

    class Config:
        orm_mode = True


# --- Customer ---
class CustomerBase(BaseModel):
    FullName: Optional[str]
    Phone: Optional[str]


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    CustomerID: int

    class Config:
        orm_mode = True


# --- Product ---
class ProductBase(BaseModel):
    Name: str
    Price: float
    CategoryID: int


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    ProductID: int

    class Config:
        orm_mode = True


# --- Sale ---
class SaleBase(BaseModel):
    SaleDate: datetime
    StoreID: int
    EmployeeID: int
    CustomerID: Optional[int]


class SaleCreate(SaleBase):
    pass


class SaleRead(SaleBase):
    SaleID: int

    class Config:
        orm_mode = True


# --- SaleItem ---
class SaleItemBase(BaseModel):
    SaleID: int
    ProductID: int
    Quantity: int
    Price: float


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemRead(SaleItemBase):
    SaleItemID: int

    class Config:
        orm_mode = True


# --- Supplier ---
class SupplierBase(BaseModel):
    Name: str


class SupplierCreate(SupplierBase):
    pass


class SupplierRead(SupplierBase):
    SupplierID: int

    class Config:
        orm_mode = True


# --- Supply ---
class SupplyBase(BaseModel):
    SupplierID: int
    ProductID: int
    SupplyDate: date
    Quantity: int


class SupplyCreate(SupplyBase):
    pass


class SupplyRead(SupplyBase):
    SupplyID: int

    class Config:
        orm_mode = True


# --- Inventory ---
class InventoryBase(BaseModel):
    StoreID: int
    ProductID: int
    Quantity: int


class InventoryCreate(InventoryBase):
    pass


class InventoryRead(InventoryBase):
    InventoryID: int

    class Config:
        orm_mode = True
