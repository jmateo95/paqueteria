from schema import ResponseSchema
from app.services.sucursal.tipo_salida_service import TipoSalidaService
from app.models.sucursal.tipo_salida_model import TipoSalidaCreate, TipoSalidaUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class TipoSalidaController:
    def __init__(self):
        self.service = TipoSalidaService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tipos_salida = await self.service.get_all()
        return ResponseSchema(detail="", result=tipos_salida)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tipo_salida = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=tipo_salida)

    async def create(self, tipo_salida: TipoSalidaCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(tipo_salida)
        return ResponseSchema(detail="Tipo de Salida creado con éxito")

    async def update(self, id: int, tipo_salida: TipoSalidaUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(id, tipo_salida)
        return ResponseSchema(detail="Tipo de Salida actualizado con éxito")

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Tipo de Salida eliminado con éxito")
