from app.models.gasto.gasto_model import GastoCreate, GastoUpdate
from config.Connection import prisma_connection
from datetime import datetime
import calendar

class GastoRepository:
    def __init__(self):
        self.connection = prisma_connection
    
    async def get_gastos_by_filters(self, sucursal_id=None, tipo_gasto_id=None, fecha:datetime=None):
        where_conditions = {}        
        if sucursal_id is not None:
            where_conditions["sucursal_id"] = sucursal_id
        if tipo_gasto_id is not None:
            where_conditions["tipo_gasto_id"] = tipo_gasto_id
        if fecha is not None:
           first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
           last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
           where_conditions["fecha"] = {"gte": first_day, "lte": last_day}
        return await self.connection.prisma.gasto.find_many(include={"sucursal":True,"conceptoGasto":True,"tipoGasto":True}, where=where_conditions)

    async def get_by_id(self, gasto_id: int):
        return await self.connection.prisma.gasto.find_first(where={"id": gasto_id})
    
    async def create(self, gasto: GastoCreate):
        return await self.connection.prisma.gasto.create(gasto)
    
    async def update(self, gasto_id: int, gasto: GastoUpdate):
        return await self.connection.prisma.gasto.update(where={"id": gasto_id}, data=gasto)

    async def delete(self, gasto_id: int):
        return await self.connection.prisma.gasto.delete(where={"id": gasto_id})
    
    async def delete_by_concepto_rango(self, concepto_gasto_id: int, fecha:datetime=None):
        if fecha is None:
            fecha = datetime.now()
        first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
        last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
        return await self.connection.prisma.gasto.delete_many(
            where={
                "concepto_gasto_id": concepto_gasto_id,
                "fecha": {"gte": first_day, "lte": last_day}
            }
        )
