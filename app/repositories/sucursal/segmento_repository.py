from app.models.sucursal.segmento_model import SegmentoCreate, SegmentoUpdate
from config.Connection import prisma_connection

class SegmentoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.segmento.find_many()

    async def get_by_id(self, segmento_id: int):
        return await self.connection.prisma.segmento.find_first(where={"id": segmento_id})
    
    async def create(self, segmento: SegmentoCreate):
        return await self.connection.prisma.segmento.create(segmento)
    
    async def update(self, segmento_id: int, segmento: SegmentoUpdate):
        return await self.connection.prisma.segmento.update(where={"id": segmento_id}, data=segmento)

    async def delete(self, segmento_id: int):
        return await self.connection.prisma.segmento.delete(where={"id": segmento_id})
