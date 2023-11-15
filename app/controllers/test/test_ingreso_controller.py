from schema import ResponseSchema
from app.services.sucursal.ingreso_service import IngresoService
from app.models.sucursal.ingreso_model import IngresoCreate, IngresoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends
from fastapi import Depends, Query
from datetime import datetime

class IngresoController:
    def __init__(self):
        self.service = IngresoService()
    
    async def get_ingresos_pronosticados_by_filters(self, sucursal_id: int = Query(None), fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        result = await self.service.get_ingresos_pronosticados_by_filters(sucursal_id=sucursal_id, fecha=fecha, test=True)
        return ResponseSchema(detail="", result=result)
