from schema import ResponseSchema
from app.services.sucursal.ciudad_service import CiudadService
from app.models.sucursal.ciudad_model import CiudadCreate, CiudadUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class CiudadController:
    def __init__(self):
        self.service = CiudadService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_all()
        return ResponseSchema(detail="", result=result)


    async def get_by_id(self, ciudad_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_by_id(ciudad_id)
        return ResponseSchema(detail="", result=result)


    async def create(self, ciudad: CiudadCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(ciudad)
        return ResponseSchema(detail="")


    async def update(self, ciudad_id: int, ciudad: CiudadUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(ciudad_id, ciudad)
        return ResponseSchema(detail="")


    async def delete(self, ciudad_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(ciudad_id)
        return ResponseSchema(detail="")

ciudad_controller = CiudadController()
