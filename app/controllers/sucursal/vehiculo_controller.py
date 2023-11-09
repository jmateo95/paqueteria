from schema import ResponseSchema
from app.services.sucursal.vehiculo_service import VehiculoService
from app.models.sucursal.vehiculo_model import VehiculoCreate, VehiculoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class VehiculoController:
    def __init__(self):
        self.service = VehiculoService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        vehiculos = await self.service.get_all()
        return ResponseSchema(detail="", result=vehiculos)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        vehiculo = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=vehiculo)
    
    async def get_by_sucursal(self, sucursal_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        segmento = await self.service.get_by_sucursal(sucursal_id)
        return ResponseSchema(detail="", result=segmento)

    async def create(self, vehiculo: VehiculoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        vehiculo = await self.service.create(vehiculo)
        return ResponseSchema(detail="Vehiculo creado con éxito", result=vehiculo)

    async def update(self, id: int, vehiculo: VehiculoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        vehiculo = await self.service.update(id, vehiculo)
        return ResponseSchema(detail="Vehiculo actualizado con éxito", result=vehiculo)

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Vehiculo eliminado con éxito")
