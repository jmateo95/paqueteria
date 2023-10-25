from app.models.paquete.tracking_model import TrackingCreate, TrackingUpdate
from config.Connection import prisma_connection

class TrackingRepository:
    def __init(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.tracking.find_many()

    async def get_by_id(self, tracking_id: int):
        return await self.connection.prisma.tracking.find_first(where={"id": tracking_id})
    
    async def create(self, tracking: TrackingCreate):
        return await self.connection.prisma.tracking.create(tracking)
    
    async def update(self, tracking_id: int, tracking: TrackingUpdate):
        return await self.connection.prisma.tracking.update(where={"id": tracking_id}, data=tracking)

    async def delete(self, tracking_id: int):
        return await self.connection.prisma.tracking.delete(where={"id": tracking_id})
