from app.models.paquete.estado_paquete_model import EstadoPaqueteCreate, EstadoPaqueteUpdate
from config.Connection import prisma_connection

class EstadoPaqueteRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.estadopaquete.find_many()

    async def get_by_id(self, estado_paquete_id: int):
        return await self.connection.prisma.estadopaquete.find_first(where={"id": estado_paquete_id})
    
    async def create(self, estado_paquete: EstadoPaqueteCreate):
        return await self.connection.prisma.estadopaquete.create(estado_paquete)
    
    async def update(self, estado_paquete_id: int, estado_paquete: EstadoPaqueteUpdate):
        return await self.connection.prisma.estadopaquete.update(where={"id": estado_paquete_id}, data=estado_paquete)

    async def delete(self, estado_paquete_id: int):
        return await self.connection.prisma.estadopaquete.delete(where={"id": estado_paquete_id})
