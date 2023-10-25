from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate
from config.Connection import prisma_connection

class SalidaRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.salida.find_many()

    async def get_by_id(self, salida_id: int):
        return await self.connection.prisma.salida.find_first(where={"id": salida_id})
    
    async def create(self, salida: SalidaCreate):
        return await self.connection.prisma.salida.create(salida)
    
    async def update(self, salida_id: int, salida: SalidaUpdate):
        return await self.connection.prisma.salida.update(where={"id": salida_id}, data=salida)

    async def delete(self, salida_id: int):
        return await self.connection.prisma.salida.delete(where={"id": salida_id})
