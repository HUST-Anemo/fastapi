from pydantic import BaseModel, Field, field_validator
from typing import Optional
import datetime

# 员工模型
class EmployeeCreate(BaseModel):
    last_name: str = Field(default="张")
    first_name: str = Field(default="三")
    title: str = Field(default="经理")
    reports_to: int = Field(default=1)
    birth_date: str = Field(default="2000-01-01")
    hire_date: str = Field(default="2020-02-02")
    address: str = Field(default="江夏区")
    city: str = Field(default="武汉市")
    state: str = Field(default="华中")
    country: str = Field(default="中国")
    postal_code: str = Field(default="8888")
    phone: str = Field(default="12345678")
    fax: str = Field(default="0713-9999999")
    email: str = Field(default="zhangsan@company.com")

    @field_validator("birth_date", "hire_date", mode="after")
    def format_date_with_native(cls, v: Optional[str]):
        if v is None:
            return None
        date_formats = ["%Y-%m-%d", "%Y/%m/%d", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S"]
        for fmt in date_formats:
            try:
                return datetime.datetime.strptime(v, fmt)
            except ValueError:
                continue
        return None

class EmployeeUpdate(BaseModel):
    last_name: str = Field(default="张")
    first_name: str = Field(default="三")
    title: str = Field(default="经理")
    reports_to: int = Field(default=1)
    birth_date: str = Field(default="2000-01-01")
    hire_date: str = Field(default="2020-02-02")
    address: str = Field(default="江夏区")
    city: str = Field(default="武汉市")
    state: str = Field(default="华中")
    country: str = Field(default="中国")
    postal_code: str = Field(default="8888")
    phone: str = Field(default="12345678")
    fax: str = Field(default="0713-9999999")
    email: str = Field(default="zhangsan@company.com")

    @field_validator("birth_date", "hire_date", mode="after")
    def format_date_with_native(cls, v: Optional[str]):
        if v is None:
            return None
        date_formats = ["%Y-%m-%d", "%Y/%m/%d", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S"]
        for fmt in date_formats:
            try:
                return datetime.datetime.strptime(v, fmt)
            except ValueError:
                continue
        return None

class Employee(BaseModel):
    employee_id: int
    last_name: str
    first_name: str
    title: Optional[str] = None
    reports_to: Optional[int] = None
    birth_date: Optional[datetime.datetime] = None
    hire_date: Optional[datetime.datetime] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

# 客户模型
class CustomerCreate(BaseModel):
    first_name: str = Field(default="李")
    last_name: str = Field(default="四")
    email: str = Field(default="lisi@email.com")
    company: str = Field(default="公司")
    address: str = Field(default="朝阳区")
    city: str = Field(default="北京市")
    state: str = Field(default="华北")
    country: str = Field(default="中国")
    postal_code: str = Field(default="6666")
    phone: str = Field(default="987654321")
    fax: str = Field(default="010-666666")
    support_rep_id: int = Field(default=1)

class CustomerUpdate(BaseModel):
    first_name: str = Field(default="李")
    last_name: str = Field(default="四")
    email: str = Field(default="lisi@email.com")
    company: str = Field(default="公司")
    address: str = Field(default="朝阳区")
    city: str = Field(default="北京市")
    state: str = Field(default="华北")
    country: str = Field(default="中国")
    postal_code: str = Field(default="6666")
    phone: str = Field(default="987654321")
    fax: str = Field(default="010-666666")
    support_rep_id: int = Field(default=1)

class Customer(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    company: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    email: str
    support_rep_id: Optional[int] = None
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True