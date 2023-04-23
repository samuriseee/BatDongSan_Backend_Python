from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from routes.user import user
from routes.bat_dong_san import BatDongSanRouter,LoaiNhaDatBanRouter, LoaiNhaDatChoThueRouter
from config.openapi import tags_metadata
import uvicorn 

app = FastAPI(
    title="Real Estate API",
    description="Real Estate API for python crawler",
    version="0.0.1",
    openapi_tags=tags_metadata,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(BatDongSanRouter)
app.include_router(LoaiNhaDatBanRouter)
app.include_router(LoaiNhaDatChoThueRouter)
