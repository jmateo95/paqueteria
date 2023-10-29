from schema import ResponseSchema
from app.services.gasto.tipo_gasto_service import TipoGastoService
from app.models.gasto.tipo_gasto_model import TipoGastoCreate, TipoGastoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class TipoGastoController:
    def __init__(self):
        self.service = TipoGastoService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tipo_gastos = await self.service.get_all()
        return ResponseSchema(detail="", result=tipo_gastos)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tipo_gasto = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=tipo_gasto)

    async def create(self, tipo_gasto: TipoGastoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        tipo_gasto = await self.service.create(tipo_gasto)
        return ResponseSchema(detail="Tipo de gasto creado con éxito", result=tipo_gasto)

    async def update(self, id: int, tipo_gasto: TipoGastoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        tipo_gasto = await self.service.update(id, tipo_gasto)
        return ResponseSchema(detail="Tipo de gasto actualizado con éxito", result=tipo_gasto)

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Tipo de gasto eliminado con éxito")
