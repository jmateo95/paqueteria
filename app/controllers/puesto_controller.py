from schema import ResponseSchema
from app.services.puesto_service import PuestoService
from app.models.puesto_model import PuestoCreate, PuestoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class PuestoController:
    def __init__(self):
        self.service = PuestoService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_all()
        return ResponseSchema(detail="", result=result)

    async def get_by_id(self, puesto_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_by_id(puesto_id)
        return ResponseSchema(detail="", result=result)

    async def create(self, puesto: PuestoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(puesto)
        return ResponseSchema(detail="")

    async def update(self, puesto_id: int, puesto: PuestoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(puesto_id, puesto)
        return ResponseSchema(detail="")

    async def delete(self, puesto_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(puesto_id)
        return ResponseSchema(detail="")

puesto_controller = PuestoController()