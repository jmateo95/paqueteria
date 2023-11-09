from schema import ResponseSchema
from app.services.paquete.tracking_service import TrackingService
from app.models.paquete.tracking_model import TrackingCreate, TrackingUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends, Query

class TrackingController:
    def __init__(self):
        self.service = TrackingService()

    async def get_tracking_by_filters(self, paquete_id: int = Query(None), estado_tracking_id: int = Query(None), salida_id:int = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        trackings = await self.service.get_tracking_by_filters(paquete_id, estado_tracking_id, salida_id)
        return ResponseSchema(detail="", result=trackings)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tracking = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=tracking)

    async def create(self, tracking: TrackingCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        tracking = await self.service.create(tracking)
        return ResponseSchema(detail="Tracking creado con éxito", result=tracking)

    async def update(self, id: int, tracking: TrackingUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        tracking = await self.service.update(id, tracking)
        return ResponseSchema(detail="Tracking actualizado con éxito", result=tracking)

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Tracking eliminado con éxito")
