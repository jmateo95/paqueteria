from schema import ResponseSchema
from app.services.sucursal.segmento_service import SegmentoService
from app.models.sucursal.segmento_model import SegmentoCreate, SegmentoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class SegmentoController:
    def __init__(self):
        self.service = SegmentoService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        segmentos = await self.service.get_all()
        return ResponseSchema(detail="", result=segmentos)

    async def get_by_id(self, segmento_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        segmento = await self.service.get_by_id(segmento_id)
        return ResponseSchema(detail="", result=segmento)

    async def create(self, segmento: SegmentoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(segmento)
        return ResponseSchema(detail="Segmento creado con éxito")

    async def update(self, segmento_id: int, segmento: SegmentoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(segmento_id, segmento)
        return ResponseSchema(detail="Segmento actualizado con éxito")

    async def delete(self, segmento_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(segmento_id)
        return ResponseSchema(detail="Segmento eliminado con éxito")