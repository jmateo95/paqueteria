from app.models.sucursal.sucursal_model import SucursalCreate, SucursalUpdate
from config.Connection import prisma_connection

class SucursalRepository:

    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.sucursal.find_many()

    async def get_by_id(self, sucursal_id: int):
        return await self.connection.prisma.sucursal.find_first(where={"id": sucursal_id})

    async def create(self, sucursal: SucursalCreate):
        return await self.connection.prisma.sucursal.create(sucursal)

    async def update(self, sucursal_id: int, sucursal: SucursalUpdate):
        return await self.connection.prisma.sucursal.update(where={"id": sucursal_id}, data=sucursal)

    async def delete(self, sucursal_id: int):
        return await self.connection.prisma.sucursal.delete(where={"id": sucursal_id})
    
    async def get_total_salary_by_sucursal(self):
        query = """
            SELECT s.id AS id, SUM(u.horas * p.salario_horario) AS total_salarios
            FROM "Sucursal" s
            JOIN "Usuario" u ON s.id = u.sucursal_id
            JOIN "Puesto" p ON u.puesto_id = p.id
            GROUP BY s.id
        """
        result = await self.connection.prisma.query_raw(query=query)
        return result
        