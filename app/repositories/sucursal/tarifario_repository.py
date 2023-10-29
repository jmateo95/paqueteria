from app.enums.enums import ConceptoGasto, TipoGasto
from app.models.sucursal.tarifario_model import TarifarioCreate, TarifarioUpdate
from config.Connection import prisma_connection
from datetime import datetime
import calendar

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

    async def delete_by_fecha(self, fecha=None):
        today = datetime.now()
        if fecha is None:
            first_day = today.replace(day=1, hour=0, minute=0, second=0)
            last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1], hour=23, minute=59, second=59)
        return await self.connection.prisma.tarifario.delete_many(
            where={
                "fecha": {"gte": first_day, "lte": last_day}
            }
        )
    
    async def calculate_total_gasto(self, fecha=None):
        today = datetime.now()
        if fecha is None:
            first_day = today.replace(day=1, hour=0, minute=0, second=0).isoformat()
            last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1], hour=23, minute=59, second=59).isoformat()
        
        query = """
            SELECT SUM(monto) AS total_gasto
            FROM public."Gasto"
            WHERE fecha >= TO_TIMESTAMP($1, 'YYYY-MM-DD"T"HH24:MI:SS') 
                AND fecha <= TO_TIMESTAMP($2, 'YYYY-MM-DD"T"HH24:MI:SS')
                AND tipo_gasto_id <> $3
                AND concepto_gasto_id <> $4
        """
        result = await self.connection.prisma.query_raw(query, first_day, last_day, TipoGasto.TRANSPORTE, ConceptoGasto.GASOLINA)
        return result[0]['total_gasto'] if result else 0

    async def calculate_total_libras(self, fecha=None):
        today = datetime.now()
        if fecha is None:
            first_day = today.replace(day=1, hour=0, minute=0, second=0).isoformat()
            last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1], hour=23, minute=59, second=59).isoformat()
        query = """
            SELECT SUM(capacidad_lb) AS total_capacidad_lb
            FROM public."Salida"
            WHERE fecha_programada >= TO_TIMESTAMP($1, 'YYYY-MM-DD"T"HH24:MI:SS') 
                AND fecha_programada <= TO_TIMESTAMP($2, 'YYYY-MM-DD"T"HH24:MI:SS')
        """
        result = await self.connection.prisma.query_raw(query, first_day, last_day)
        return result[0]['total_capacidad_lb'] if result else 0