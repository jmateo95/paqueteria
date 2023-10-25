from schema import ResponseSchema
from app.services.paquete.tracking_service import TrackingService
from app.models.paquete.tracking_model import TrackingCreate, TrackingUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class TrackingController:
    def __init(self):
        self.service = TrackingService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        trackings = await self.service.get_all()
        return ResponseSchema(detail="", result=trackings)

    async def get_by_id(self, tracking_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        tracking = await self.service.get_by_id(tracking_id)
        return ResponseSchema(detail="", result=tracking)

    async def create(self, tracking: TrackingCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(tracking)
        return ResponseSchema(detail="Tracking creado con éxito")

    async def update(self, tracking_id: int, tracking: TrackingUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(tracking_id, tracking)
        return ResponseSchema(detail="Tracking actualizado con éxito")

    async def delete(self, tracking_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(tracking_id)
        return ResponseSchema(detail="Tracking eliminado con éxito")
