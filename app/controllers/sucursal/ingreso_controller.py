from schema import ResponseSchema
from app.services.sucursal.ingreso_service import IngresoService
from app.models.sucursal.ingreso_model import IngresoCreate, IngresoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class IngresoController:
    def __init__(self):
        self.service = IngresoService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        ingresos = await self.service.get_all()
        return ResponseSchema(detail="", result=ingresos)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        ingreso = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=ingreso)

    async def create(self, ingreso: IngresoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(ingreso)
        return ResponseSchema(detail="Ingreso creado con éxito")

    async def update(self, id: int, ingreso: IngresoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(id, ingreso)
        return ResponseSchema(detail="Ingreso actualizado con éxito")

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Ingreso eliminado con éxito")
