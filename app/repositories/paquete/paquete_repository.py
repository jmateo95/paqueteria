from app.models.paquete.paquete_model import PaqueteCreate, PaqueteUpdate, PaqueteCotizar
from config.Connection import prisma_connection

class PaqueteRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.paquete.find_many()

    async def get_by_id(self, paquete_id: int):
        return await self.connection.prisma.paquete.find_first(where={"id": paquete_id})
    
    async def create(self, paquete: PaqueteCreate):
        return await self.connection.prisma.paquete.create(paquete)
    
    async def update(self, paquete_id: int, paquete: PaqueteUpdate):
        return await self.connection.prisma.paquete.update(where={"id": paquete_id}, data=paquete)

    async def delete(self, paquete_id: int):
        return await self.connection.prisma.paquete.delete(where={"id": paquete_id})
