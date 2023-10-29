from schema import ResponseSchema
from app.services.sucursal.tarifario_service import TarifarioService
from app.models.sucursal.tarifario_model import TarifarioCreate, TarifarioUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends, Query
from datetime import datetime

class TarifarioController:
    def __init__(self):
        self.service = TarifarioService()

    async def get_tarifarios_by_filters(self, fecha: datetime = Query(None)):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_tarifarios_by_filters(fecha)
        return ResponseSchema(detail="", result=result)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tarifario = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=tarifario)

    async def create(self, tarifario: TarifarioCreate):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(tarifario)
        return ResponseSchema(detail="Tarifario creado con éxito")

    async def update(self, id: int, tarifario: TarifarioUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(id, tarifario)
        return ResponseSchema(detail="Tarifario actualizado con éxito")

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Tarifario eliminado con éxito")