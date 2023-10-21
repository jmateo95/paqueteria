from fastapi import APIRouter
from app.routers import ciudad_router, usuario_router, puesto_router, tipo_sucursal_router, sucursal_router

api_router = APIRouter()

#RUTAS
api_router.include_router(ciudad_router.router)
api_router.include_router(usuario_router.router)
api_router.include_router(puesto_router.router)
api_router.include_router(tipo_sucursal_router.router)
api_router.include_router(sucursal_router.router)