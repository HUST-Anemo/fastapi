from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from slowapi import Limiter
from slowapi.util import get_remote_address

import db
import schemas

# 路由定义
router = APIRouter()

# 限流配置
limiter = Limiter(key_func=get_remote_address)
limit_access = limiter.limit("3/10seconds")

# 员工管理
@router.get("/employees/", response_model=List[schemas.Employee], summary="Read：查询全部员工", tags=["员工管理"])
@limit_access
def get_all_employees(request: Request, db_session: Session = Depends(db.get_db)):
    return db_session.query(db.DB_Employee).order_by(db.DB_Employee.employee_id).all()

@router.post("/employees/", response_model=schemas.Employee, status_code=status.HTTP_201_CREATED, summary="Create：新增员工", tags=["员工管理"])
def create_employee(emp: schemas.EmployeeCreate, db_session: Session = Depends(db.get_db)):
    max_id = db_session.query(func.max(db.DB_Employee.employee_id)).scalar()
    new_emp_id = 1 if max_id is None else max_id + 1
    db_emp = db.DB_Employee(employee_id=new_emp_id,** emp.model_dump())
    db_session.add(db_emp)
    db_session.commit()
    db_session.refresh(db_emp)
    return db_emp

@router.put("/employees/{emp_id}", response_model=schemas.Employee, summary="Update：修改员工", tags=["员工管理"])
def update_employee(emp_id: int, emp: schemas.EmployeeUpdate, db_session: Session = Depends(db.get_db)):
    db_emp = db_session.query(db.DB_Employee).filter(db.DB_Employee.employee_id == emp_id).first()
    if not db_emp:
        raise HTTPException(status_code=404, detail="员工不存在")
    for key, value in emp.model_dump().items():
        setattr(db_emp, key, value)
    db_session.commit()
    db_session.refresh(db_emp)
    return db_emp

@router.delete("/employees/{emp_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete：删除员工", tags=["员工管理"])
def delete_employee(emp_id: int, db_session: Session = Depends(db.get_db)):
    db_emp = db_session.query(db.DB_Employee).filter(db.DB_Employee.employee_id == emp_id).first()
    if not db_emp:
        raise HTTPException(status_code=404, detail="员工不存在")
    db_session.delete(db_emp)
    db_session.commit()
    return

# 顾客管理
@router.get("/customers/", response_model=List[schemas.Customer], summary="Read：查询全部顾客", tags=["顾客管理"])
@limit_access
def get_all_customers(request: Request, db_session: Session = Depends(db.get_db)):
    return db_session.query(db.DB_Customer).order_by(db.DB_Customer.customer_id).all()

@router.post("/customers/", response_model=schemas.Customer, status_code=status.HTTP_201_CREATED, summary="Create：新增顾客", tags=["顾客管理"])
def create_customer(cus: schemas.CustomerCreate, db_session: Session = Depends(db.get_db)):
    max_id = db_session.query(func.max(db.DB_Customer.customer_id)).scalar()
    new_cus_id = 1 if max_id is None else max_id + 1
    db_cus = db.DB_Customer(customer_id=new_cus_id, **cus.model_dump())
    db_session.add(db_cus)
    db_session.commit()
    db_session.refresh(db_cus)
    return db_cus

@router.put("/customers/{cus_id}", response_model=schemas.Customer, summary="Update：修改顾客", tags=["顾客管理"])
def update_customer(cus_id: int, cus: schemas.CustomerUpdate, db_session: Session = Depends(db.get_db)):
    db_cus = db_session.query(db.DB_Customer).filter(db.DB_Customer.customer_id == cus_id).first()
    if not db_cus:
        raise HTTPException(status_code=404, detail="顾客不存在")
    for key, value in cus.model_dump().items():
        setattr(db_cus, key, value)
    db_session.commit()
    db_session.refresh(db_cus)
    return db_cus

@router.delete("/customers/{cus_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete：删除顾客", tags=["顾客管理"])
def delete_customer(cus_id: int, db_session: Session = Depends(db.get_db)):
    db_cus = db_session.query(db.DB_Customer).filter(db.DB_Customer.customer_id == cus_id).first()
    if not db_cus:
        raise HTTPException(status_code=404, detail="顾客不存在")
    db_session.delete(db_cus)
    db_session.commit()
    return