from schema import ResponseSchema
from app.services.sucursal.salida_service import SalidaService
from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends, Query
from datetime import datetime

class SalidaController:
    def __init__(self):
        self.service = SalidaService()

    async def get_salidas_by_filters(self, sucursal_id: int = Query(None), tipo_salida_id: int = Query(None), fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_salidas_by_filters(sucursal_id, tipo_salida_id, fecha, test=True)
        return ResponseSchema(detail="", result=result)

    async def create(self, salida: SalidaCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        salida.test=True
        salida = await self.service.create(salida)
        return ResponseSchema(detail="Salida creada con éxito", result=salida)
