from app.models.paquete.tracking_model import TrackingCreate, TrackingUpdate
from config.Connection import prisma_connection

class TrackingRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_tracking_by_filters(self, paquete_id:int=None, estado_tracking_id:int=None, salida_id:int=None):
        where_conditions = {}
        if paquete_id is not None:
            where_conditions["paquete_id"] = paquete_id
        if estado_tracking_id is not None:
            where_conditions["estado_tracking_id"] = estado_tracking_id
        if salida_id is not None:
            where_conditions["salida_id"] = salida_id
        return await self.connection.prisma.tracking.find_many(where=where_conditions, order=[{"id": "asc"}])

    async def get_by_id(self, tracking_id: int):
        return await self.connection.prisma.tracking.find_first(where={"id": tracking_id})
    
    async def create(self, tracking: TrackingCreate):
        return await self.connection.prisma.tracking.create(tracking)
    
    async def update(self, tracking_id: int, tracking: TrackingUpdate):
        return await self.connection.prisma.tracking.update(where={"id": tracking_id}, data=tracking)

    async def delete(self, tracking_id: int):
        return await self.connection.prisma.tracking.delete(where={"id": tracking_id})
    
    async def get_by_paquete_and_status(self, paquete_id: int, estado_tracking_id: int):
        return await self.connection.prisma.tracking.find_first(where={"paquete_id": paquete_id, "estado_tracking_id": estado_tracking_id}, order=[{"id": "desc"}])
    
    async def update_trackings_salida(self, salida_id: int, estado_tracking_id:int):
        total_actualizados = await self.connection.prisma.tracking.update_many(
            data={"estado_tracking_id": estado_tracking_id},
            where={"salida_id": salida_id}
        )
        return total_actualizados
