from fastapi import APIRouter
from app.routers import ciudad_router, usuario_router

api_router = APIRouter()

#RUTAS
api_router.include_router(ciudad_router.router)
api_router.include_router(usuario_router.router)