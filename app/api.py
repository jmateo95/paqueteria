from fastapi import APIRouter
from app.controllers import ciudad_controller

api_router = APIRouter()

#RUTAS
api_router.include_router(ciudad_controller.router)