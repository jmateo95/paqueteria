from schema import ResponseSchema
from app.services.sucursal.sucursal_service import SucursalService
from app.models.sucursal.sucursal_model import SucursalCreate, SucursalUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class SucursalController:
    def __init__(self):
        self.service = SucursalService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_all(test=True)
        return ResponseSchema(detail="", result=result)

    async def create(self, sucursal: SucursalCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        sucursal.test=True
        result = await self.service.create(sucursal)
        return ResponseSchema(detail="", result=result)

sucursal_controller = SucursalController()
