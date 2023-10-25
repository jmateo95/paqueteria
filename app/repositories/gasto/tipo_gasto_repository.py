from app.models.gasto.tipo_gasto_model import TipoGastoCreate, TipoGastoUpdate
from config.Connection import prisma_connection

class TipoGastoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.tipogasto.find_many()

    async def get_by_id(self, tipo_gasto_id: int):
        return await self.connection.prisma.tipogasto.find_first(where={"id": tipo_gasto_id})
    
    async def create(self, tipo_gasto: TipoGastoCreate):
        return await self.connection.prisma.tipogasto.create(tipo_gasto)
    
    async def update(self, tipo_gasto_id: int, tipo_gasto: TipoGastoUpdate):
        return await self.connection.prisma.tipogasto.update(where={"id": tipo_gasto_id}, data=tipo_gasto)

    async def delete(self, tipo_gasto_id: int):
        return await self.connection.prisma.tipogasto.delete(where={"id": tipo_gasto_id})
