from schema import ResponseSchema
from app.services.sucursal.tipo_vehiculo_service import TipoVehiculoService
from app.models.sucursal.tipo_vehiculo_model import TipoVehiculoCreate, TipoVehiculoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class TipoVehiculoController:
    def __init__(self):
        self.service = TipoVehiculoService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tipo_vehiculos = await self.service.get_all()
        return ResponseSchema(detail="", result=tipo_vehiculos)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tipo_vehiculo = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=tipo_vehiculo)

    async def create(self, tipo_vehiculo: TipoVehiculoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(tipo_vehiculo)
        return ResponseSchema(detail="Tipo de vehículo creado con éxito")

    async def update(self, id: int, tipo_vehiculo: TipoVehiculoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(id, tipo_vehiculo)
        return ResponseSchema(detail="Tipo de vehículo actualizado con éxito")

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Tipo de vehículo eliminado con éxito")
