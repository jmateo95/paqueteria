from app.models.sucursal.ingreso_model import IngresoCreate, IngresoUpdate
from config.Connection import prisma_connection
from datetime import datetime
import calendar

class IngresoRepository:
    def __init__(self):
        self.connection = prisma_connection
        
    async def get_ingresos_by_filters(self, sucursal_id=None, fecha:datetime=None):
        where_conditions = {}        
        if sucursal_id is not None:
            where_conditions["sucursal_id"] = sucursal_id
        if fecha is not None:
           first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
           last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
           where_conditions["fecha"] = {"gte": first_day, "lte": last_day}
        return await self.connection.prisma.ingreso.find_many(include={"sucursal":True}, where=where_conditions)
    
    async def get_ingresos_pronosticados_by_filters(self, sucursal_id=None, fecha:datetime=None, test:bool=False):
        query = """
            SELECT
            se.sucursal_origen_id as sucursal_id,
            ROUND((s.capacidad_lb * (s.costo_lb + t.costo_lb) * (1 + (t.ganancia_envio / 100)))::numeric, 2) as monto,
            t.fecha as fecha
            FROM "Salida" s
            JOIN "Segmento" se on se.id = s.segmento_id
            JOIN "Tarifario" t ON EXTRACT(YEAR FROM s.fecha_programada) = EXTRACT(YEAR FROM t.fecha)
                            AND EXTRACT(MONTH FROM s.fecha_programada) = EXTRACT(MONTH FROM t.fecha)
            WHERE se.test = :test
            AND s.test = :test
            AND t.test = :test
        """
        if sucursal_id is not None:
            query += f"AND se.sucursal_origen_id = {sucursal_id}\n"
        if fecha is not None:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND t.fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        return await self.connection.prisma.query_raw(query=query, parameters={"test": test})

    async def get_by_id(self, ingreso_id: int):
        return await self.connection.prisma.ingreso.find_first(where={"id": ingreso_id})
    
    async def create(self, ingreso: IngresoCreate):
        return await self.connection.prisma.ingreso.create(ingreso)
    
    async def update(self, ingreso_id: int, ingreso: IngresoUpdate):
        return await self.connection.prisma.ingreso.update(where={"id": ingreso_id}, data=ingreso)

    async def delete(self, ingreso_id: int):
        return await self.connection.prisma.ingreso.delete(where={"id": ingreso_id})
