from datetime import datetime
import calendar
from app.models.sucursal.sucursal_model import SucursalCreate, SucursalUpdate
from config.Connection import prisma_connection

class SucursalRepository:

    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self, test:bool=False):
        where_conditions = {}
        if not test:
            where_conditions["test"] = test
        return await self.connection.prisma.sucursal.find_many(include={"ciudad":True,"tipoSucursal":True}, where=where_conditions, order=[{"id": "desc"}])

    async def get_by_id(self, sucursal_id: int):
        return await self.connection.prisma.sucursal.find_first(where={"id": sucursal_id})

    async def create(self, sucursal: SucursalCreate):
        return await self.connection.prisma.sucursal.create(sucursal)

    async def update(self, sucursal_id: int, sucursal: SucursalUpdate):
        return await self.connection.prisma.sucursal.update(where={"id": sucursal_id}, data=sucursal)

    async def delete(self, sucursal_id: int):
        return await self.connection.prisma.sucursal.delete(where={"id": sucursal_id})
    
    async def get_total_salary_by_sucursal(self, test:bool=False):
        query = """
            SELECT s.id AS id, SUM(u.horas * p.salario_horario) AS total_salarios
            FROM "Sucursal" s
            JOIN "Usuario" u ON s.id = u.sucursal_id
            JOIN "Puesto" p ON u.puesto_id = p.id
            WHERE s.test = $1 AND u.test = $1
            GROUP BY s.id
        """
        result = await self.connection.prisma.query_raw(query,test)
        return result
        

    async def sucursales_tot(self, test:bool=None):
        where_conditions = {}
        if not test:
            where_conditions["test"] = test
        return await self.connection.prisma.sucursal.find_many(where=where_conditions)
    
    async def top_sucursales(self, fecha:datetime=None):
        query = """
            SELECT count (p.id) as value, s.nombre as name
            FROM (
                SELECT
                    p.*,
                    (
                        SELECT MIN(actualizacion)
                        FROM "Tracking"
                        WHERE paquete_id = p.id
                    ) AS fecha,
                    (
                        SELECT sucursal_id
                        FROM "Tracking"
                        WHERE paquete_id = p.id
                        ORDER BY actualizacion
                        LIMIT 1
                    ) AS sucursal_id
                FROM "Paquete" p) AS p
            JOIN "Sucursal" s ON s.id = p.sucursal_id
            WHERE 1 = 1
        """
        if fecha is not None:
            first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
            last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
            query += f"AND fecha BETWEEN '{first_day}' AND '{last_day}'\n"
        query += f"GROUP BY s.nombre\n"
        return await self.connection.prisma.query_raw(query)