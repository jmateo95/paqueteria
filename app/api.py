from fastapi import APIRouter
from app.routers import ciudad_router

api_router = APIRouter()

#RUTAS
api_router.include_router(ciudad_router.router)