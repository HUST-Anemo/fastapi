from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接配置
SQLALCHEMY_DATABASE_URL = "postgresql://neo:chinook@localhost:5432/chinook"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 数据库会话依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 员工表
class DB_Employee(Base):
    __tablename__ = "employee"
    employee_id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    title = Column(String(30), nullable=True)
    reports_to = Column(Integer, nullable=True)
    birth_date = Column(DateTime, nullable=True)
    hire_date = Column(DateTime, nullable=True)
    address = Column(String(70), nullable=True)
    city = Column(String(40), nullable=True)
    state = Column(String(40), nullable=True)
    country = Column(String(40), nullable=True)
    postal_code = Column(String(10), nullable=True)
    phone = Column(String(24), nullable=True)
    fax = Column(String(24), nullable=True)
    email = Column(String(60), nullable=True)

# 顾客表
class DB_Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(20), nullable=False)
    company = Column(String(80), nullable=True)
    address = Column(String(70), nullable=True)
    city = Column(String(40), nullable=True)
    state = Column(String(40), nullable=True)
    country = Column(String(40), nullable=True)
    postal_code = Column(String(10), nullable=True)
    phone = Column(String(24), nullable=True)
    fax = Column(String(24), nullable=True)
    email = Column(String(60), nullable=False)
    support_rep_id = Column(Integer, nullable=True)

# 创建表
Base.metadata.create_all(bind=engine)