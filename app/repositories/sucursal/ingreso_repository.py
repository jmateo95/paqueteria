from app.enums.enums import TipoSalida
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
            WHERE se.test = $1
            AND s.test = $1
            AND t.test = $1
        """
        if sucursal_id is not None:
            query += f"AND se.sucursal_origen_id = {sucursal_id}\n"
        if fecha is not None:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND t.fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        return await self.connection.prisma.query_raw(query, test)

    async def get_by_id(self, ingreso_id: int):
        return await self.connection.prisma.ingreso.find_first(where={"id": ingreso_id})
    
    async def create(self, ingreso: IngresoCreate):
        return await self.connection.prisma.ingreso.create(ingreso)
    
    async def update(self, ingreso_id: int, ingreso: IngresoUpdate):
        return await self.connection.prisma.ingreso.update(where={"id": ingreso_id}, data=ingreso)

    async def delete(self, ingreso_id: int):
        return await self.connection.prisma.ingreso.delete(where={"id": ingreso_id})
    

    async def ingreso(self, fecha:datetime=None):
        query = f"""
            SELECT SUM(monto) AS total_monto
            FROM "Ingreso" 
            WHERE 1=1
        """ 

        if fecha:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        
        result = await self.connection.prisma.query_raw(query)

        if (result[0]["total_monto"] is None):
            return 0
        return result[0]["total_monto"]
    
    async def ingreso_pron(self, fecha:datetime=None, test:bool=False, tipo_salida:int=(TipoSalida.FIN)):
        WHERE =f"AND t.test = {test}\n"
        if not test:
            WHERE +=f"AND s.test = {test}\n"

        if fecha:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            WHERE += f"AND s.fecha_programada BETWEEN '{first_day}' AND '{last_day}'\n"
            WHERE += f"AND t.fecha BETWEEN '{first_day}' AND '{last_day}'\n"

        query = f"""
            SELECT sum(round((((s.costo_lb+t.costo_lb)*s.capacidad_lb)*(1+(t.ganancia_envio/100)))::numeric,2)) as total_monto
            FROM "Salida" s
            JOIN "Tarifario" t ON
                EXTRACT(YEAR FROM s.fecha_programada) = EXTRACT(YEAR FROM t.fecha) AND
                EXTRACT(MONTH FROM s.fecha_programada) = EXTRACT(MONTH FROM t.fecha)
            WHERE tipo_salida_id<={tipo_salida}
            {WHERE}
        """
        result = await self.connection.prisma.query_raw(query)
        if (result[0]["total_monto"] is None):
            return 0
        return result[0]["total_monto"]
    
    async def ingreso_real_vs_pron(self, fecha:datetime=None, test:bool=False):
        result_1=await self.ingreso(fecha=fecha)
        result_2=await self.ingreso_pron(fecha=fecha, test=test, tipo_salida=TipoSalida.CARGANDO)
        return result_1, result_2
    
    async def ingreso_sucursal(self, fecha:datetime=None):
        WHERE=''

        if fecha:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            WHERE += f"AND i.fecha BETWEEN '{first_day}' AND '{last_day}'\n"

        query = f"""
            SELECT s.nombre as name, ROUND(SUM(i.monto)::numeric, 2) AS value
            FROM "Ingreso" as i
            JOIN "Sucursal" as s ON s.id=i.sucursal_id
            WHERE 1=1
            {WHERE}
            GROUP BY (s.nombre)
            ORDER BY value desc
        """
        result = await self.connection.prisma.query_raw(query)
        return result
