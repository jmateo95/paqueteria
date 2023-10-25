from app.models.sucursal.tarifario_model import TarifarioCreate, TarifarioUpdate
from config.Connection import prisma_connection

class TarifarioRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.tarifario.find_many()

    async def get_by_id(self, tarifario_id: int):
        return await self.connection.prisma.tarifario.find_first(where={"id": tarifario_id})
    
    async def create(self, tarifario: TarifarioCreate):
        return await self.connection.prisma.tarifario.create(tarifario)
    
    async def update(self, tarifario_id: int, tarifario: TarifarioUpdate):
        return await self.connection.prisma.tarifario.update(where={"id": tarifario_id}, data=tarifario)

    async def delete(self, tarifario_id: int):
        return await self.connection.prisma.tarifario.delete(where={"id": tarifario_id})
