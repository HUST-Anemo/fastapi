from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

import crud
import db

app = FastAPI(
    title="后端作业一：Chinook数据库 员工+顾客 增删改查接口",
    swagger_ui_default_models_expand_depth=-1,
    swagger_ui_parameters_expand_depth=-1
)

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 限流异常处理
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(crud.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)