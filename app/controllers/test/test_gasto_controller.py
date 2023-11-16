from schema import ResponseSchema
from app.services.gasto.gasto_service import GastoService
from app.models.gasto.gasto_model import GastoCreate, GastoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends, Query
from datetime import datetime

class GastoController:
    def __init__(self):
        self.service = GastoService()
    
    async def get_gastos_by_filters(self, sucursal_id: int = Query(None), tipo_gasto_id: int = Query(None), fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_gastos_by_filters(sucursal_id=sucursal_id, tipo_gasto_id=tipo_gasto_id, fecha=fecha, test=True)
        return ResponseSchema(detail="", result=result)

    async def create(self, gasto: GastoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        gasto.test=True
        gasto = await self.service.create(gasto)
        return ResponseSchema(detail="Gasto creado con éxito", result=gasto)
    


    
    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        gasto = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=gasto)

    async def update(self, id: int, gasto: GastoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        gasto = await self.service.update(id, gasto)
        return ResponseSchema(detail="Gasto actualizado con éxito", result=gasto)

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Gasto eliminado con éxito")