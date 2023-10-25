from app.models.paquete.estado_tracking_model import EstadoTrackingCreate, EstadoTrackingUpdate
from config.Connection import prisma_connection

class EstadoTrackingRepository:
    def __init(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.estadotracking.find_many()

    async def get_by_id(self, estado_tracking_id: int):
        return await self.connection.prisma.estadotracking.find_first(where={"id": estado_tracking_id})
    
    async def create(self, estado_tracking: EstadoTrackingCreate):
        return await self.connection.prisma.estadotracking.create(estado_tracking)
    
    async def update(self, estado_tracking_id: int, estado_tracking: EstadoTrackingUpdate):
        return await self.connection.prisma.estadotracking.update(where={"id": estado_tracking_id}, data=estado_tracking)

    async def delete(self, estado_tracking_id: int):
        return await self.connection.prisma.estadotracking.delete(where={"id": estado_tracking_id})
