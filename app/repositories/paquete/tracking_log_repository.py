from app.models.paquete.tracking_model import TrackingCreate
from config.Connection import prisma_connection

class TrackingLogRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_tracking_log_by_filters(self, paquete_id:int=None, estado_tracking_id:int=None, salida_id:int=None):
        where_conditions = {}
        if paquete_id is not None:
            where_conditions["paquete_id"] = paquete_id
        if estado_tracking_id is not None:
            where_conditions["estado_tracking_id"] = estado_tracking_id
        if salida_id is not None:
            where_conditions["salida_id"] = salida_id
        return await self.connection.prisma.trackinglog.find_many(where=where_conditions, include={"paquete":True,"sucursal":True}, order=[ {"id": "asc"}])
    
    async def create(self, tracking: TrackingCreate):
        return await self.connection.prisma.trackinglog.create(tracking)