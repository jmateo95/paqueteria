from app.models.gasto.gasto_model import GastoCreate, GastoUpdate
from config.Connection import prisma_connection
from datetime import datetime
import calendar

class GastoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.gasto.find_many()

    async def get_by_id(self, gasto_id: int):
        return await self.connection.prisma.gasto.find_first(where={"id": gasto_id})
    
    async def create(self, gasto: GastoCreate):
        return await self.connection.prisma.gasto.create(gasto)
    
    async def update(self, gasto_id: int, gasto: GastoUpdate):
        return await self.connection.prisma.gasto.update(where={"id": gasto_id}, data=gasto)

    async def delete(self, gasto_id: int):
        return await self.connection.prisma.gasto.delete(where={"id": gasto_id})
    
    async def delete_by_concepto_rango(self, concepto_gasto_id: int, fecha=None):
        today = datetime.now()
        if fecha is None:
            first_day = today.replace(day=1, hour=0, minute=0, second=0)
            last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1], hour=23, minute=59, second=59)
        return await self.connection.prisma.gasto.delete_many(
            where={
                "concepto_gasto_id": concepto_gasto_id,
                "fecha": {"gte": first_day, "lte": last_day}
            }
        )
