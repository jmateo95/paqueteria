from schema import ResponseSchema
from app.services.usuario.puesto_service import PuestoService
from app.models.usuario.puesto_model import PuestoCreate, PuestoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class PuestoController:
    def __init__(self):
        self.service = PuestoService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_all()
        return ResponseSchema(detail="", result=result)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=result)

    async def create(self, puesto: PuestoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        result = await self.service.create(puesto)
        return ResponseSchema(detail="Puesto creado con éxito", result=result)

    async def update(self, id: int, puesto: PuestoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        result = await self.service.update(id, puesto)
        return ResponseSchema(detail="Puesto actualizado con éxito", result=result)

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="")

puesto_controller = PuestoController()