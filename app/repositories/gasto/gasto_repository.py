from app.models.gasto.gasto_model import GastoCreate, GastoUpdate
from config.Connection import prisma_connection

class GastoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.gasto.find_many(include={"sucursal":True,"conceptoGasto":True,"tipoGasto":True})

    async def get_by_id(self, gasto_id: int):
        return await self.connection.prisma.gasto.find_first(where={"id": gasto_id})
    
    async def create(self, gasto: GastoCreate):
        return await self.connection.prisma.gasto.create(gasto)
    
    async def update(self, gasto_id: int, gasto: GastoUpdate):
        return await self.connection.prisma.gasto.update(where={"id": gasto_id}, data=gasto)

    async def delete(self, gasto_id: int):
        return await self.connection.prisma.gasto.delete(where={"id": gasto_id})
