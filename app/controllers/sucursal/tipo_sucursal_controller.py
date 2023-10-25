from schema import ResponseSchema
from app.services.sucursal.tipo_sucursal_service import TipoSucursalService
from app.models.sucursal.tipo_sucursal_model import TipoSucursalCreate, TipoSucursalUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class TipoSucursalController:
    def __init__(self):
        self.service = TipoSucursalService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_all()
        return ResponseSchema(detail="", result=result)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=result)

    async def create(self, tipo_sucursal: TipoSucursalCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(tipo_sucursal)
        return ResponseSchema(detail="")

    async def update(self, id: int, tipo_sucursal: TipoSucursalUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(id, tipo_sucursal)
        return ResponseSchema(detail="")

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="")

tipo_sucursal_controller = TipoSucursalController()