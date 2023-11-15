from app.repositories.paquete.tracking_log_repository import TrackingLogRepository

class TrackingLogService:
    def __init__(self):
        self.repository = TrackingLogRepository()

    async def get_tracking_log_by_filters(self, paquete_id:int=None, estado_tracking_id:int=None, salida_id:int=None):
        trackings = await self.repository.get_tracking_log_by_filters(paquete_id, estado_tracking_id, salida_id)
        return [] if not trackings else trackings
