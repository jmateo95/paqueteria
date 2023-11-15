from schema import ResponseSchema
from app.services.paquete.tracking_log_service import TrackingLogService
from config.auth import get_current_user_with_roles
from fastapi import Depends, Query

class TrackingLogController:
    def __init__(self):
        self.service = TrackingLogService()

    async def get_tracking_log_by_filters(self, paquete_id: int = Query(None), estado_tracking_id: int = Query(None), salida_id:int = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        trackings = await self.service.get_tracking_log_by_filters(paquete_id, estado_tracking_id, salida_id)
        return ResponseSchema(detail="", result=trackings)