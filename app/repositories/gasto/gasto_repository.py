from app.models.gasto.gasto_model import GastoCreate, GastoUpdate
from config.Connection import prisma_connection
from datetime import datetime
import calendar

class GastoRepository:
    def __init__(self):
        self.connection = prisma_connection
    
    async def get_gastos_by_filters(self, sucursal_id=None, tipo_gasto_id=None, fecha:datetime=None,  test:bool=False):
        where_conditions = {}
        if sucursal_id is not None:
            where_conditions["sucursal_id"] = sucursal_id
        if tipo_gasto_id is not None:
            where_conditions["tipo_gasto_id"] = tipo_gasto_id
        if fecha is not None:
           first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
           last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
           where_conditions["fecha"] = {"gte": first_day, "lte": last_day}
        if not test:
            where_conditions["test"] = test
        return await self.connection.prisma.gasto.find_many(include={"sucursal":True,"conceptoGasto":True,"tipoGasto":True}, where=where_conditions)

    async def get_by_id(self, gasto_id: int):
        return await self.connection.prisma.gasto.find_first(where={"id": gasto_id})
    
    async def create(self, gasto: GastoCreate):
        return await self.connection.prisma.gasto.create(gasto)
    
    async def update(self, gasto_id: int, gasto: GastoUpdate):
        return await self.connection.prisma.gasto.update(where={"id": gasto_id}, data=gasto)

    async def delete(self, gasto_id: int):
        return await self.connection.prisma.gasto.delete(where={"id": gasto_id})
    
    async def delete_by_concepto_rango(self, concepto_gasto_id: int, fecha:datetime=None, test=False):
        if fecha is None:
            fecha = datetime.now()
        first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
        last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
        return await self.connection.prisma.gasto.delete_many(
            where={
                "concepto_gasto_id": concepto_gasto_id,
                "fecha": {"gte": first_day, "lte": last_day},
                "test": test
            }
        )
    
    async def gasto(self, fecha:datetime=None, test:bool=False):
        query = f"""
            SELECT SUM(monto) AS total_monto
            FROM "Gasto" 
            WHERE 1=1
        """
        if not test:
            query +=f"AND test = '{test}'\n"

        if fecha:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        
        result = await self.connection.prisma.query_raw(query)
        if result[0]["total_monto"]==None:
            return 0
        return result[0]["total_monto"]

    async def gasto_promedio(self, fecha:datetime=None, test:bool=False):
        WHERE=''
        if not test:
            WHERE +=f"AND test = '{test}'\n"

        if fecha:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            WHERE += f"AND fecha BETWEEN '{first_day}' AND '{last_day}'\n"

        query = f"""
            SELECT avg (gasto) AS total_monto
            FROM(
                SELECT sucursal_id, SUM(monto) AS gasto
                FROM "Gasto"
                WHERE 1=1
                {WHERE}
                GROUP BY sucursal_id
            ) AS gastos
        """
        result = await self.connection.prisma.query_raw(query)
        if result[0]["total_monto"]==None:
            return 0
        return result[0]["total_monto"]
    
    async def tipo_gasto(self, fecha:datetime=None, test:bool=False):
        WHERE=''
        if not test:
            WHERE +=f"AND g.test = '{test}'\n"

        if fecha:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            WHERE += f"AND g.fecha BETWEEN '{first_day}' AND '{last_day}'\n"

        query = f"""
            SELECT tg.nombre as name, ROUND(SUM(g.monto)::numeric, 2) AS value
            FROM "Gasto" as g
            JOIN "TipoGasto" as tg ON tg.id=g.tipo_gasto_id
            WHERE 1=1
            {WHERE}
            GROUP BY (tg.nombre)
            ORDER BY value desc
        """
        result = await self.connection.prisma.query_raw(query)
        return result
    
    async def concepto_gasto(self, fecha:datetime=None, test:bool=False):
        WHERE=''
        if not test:
            WHERE +=f"AND g.test = '{test}'\n"

        if fecha:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            WHERE += f"AND g.fecha BETWEEN '{first_day}' AND '{last_day}'\n"

        query = f"""
            SELECT cg.nombre as name, ROUND(SUM(g.monto)::numeric, 2) AS value
            FROM "Gasto" as g
            JOIN "ConceptoGasto" as cg ON cg.id=g.tipo_gasto_id
            WHERE 1=1
            {WHERE}
            GROUP BY (cg.nombre)
            ORDER BY value desc
        """
        result = await self.connection.prisma.query_raw(query)
        return result
    
    async def gasto_sucursal(self, fecha:datetime=None, test:bool=False):
        WHERE=''
        if not test:
            WHERE +=f"AND g.test = '{test}'\n"

        if fecha:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            WHERE += f"AND g.fecha BETWEEN '{first_day}' AND '{last_day}'\n"

        query = f"""
            SELECT s.nombre as name, ROUND(SUM(g.monto)::numeric, 2) AS value
            FROM "Gasto" as g
            JOIN "Sucursal" as s ON s.id=g.sucursal_id
            WHERE 1=1
            {WHERE}
            GROUP BY (s.nombre)
            ORDER BY value desc
        """
        result = await self.connection.prisma.query_raw(query)
        return result