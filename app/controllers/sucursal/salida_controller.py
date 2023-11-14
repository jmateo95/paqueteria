from schema import ResponseSchema
from app.services.sucursal.salida_service import SalidaService
from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends, Query
from datetime import datetime

class SalidaController:
    def __init__(self):
        self.service = SalidaService()

    async def get_salidas_by_filters(self, sucursal_id: int = Query(None), tipo_salida_id: int = Query(None), fecha: datetime = Query(None)):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_salidas_by_filters(sucursal_id, tipo_salida_id, fecha)
        return ResponseSchema(detail="", result=result)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        salida = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=salida)

    async def create(self, salida: SalidaCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        salida = await self.service.create(salida)
        return ResponseSchema(detail="Salida creada con éxito", result=salida)

    async def update(self, id: int, salida: SalidaUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        salida = await self.service.update(id, salida)
        return ResponseSchema(detail="Salida actualizada con éxito", result=salida)

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Salida eliminada con éxito")
    
    async def dar_salida(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.dar_salida(id)
        return ResponseSchema(detail="Salida actualizada con éxito")
    
    async def ingresar(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.ingresar(id)
        return ResponseSchema(detail="Salida actualizada con éxito")
