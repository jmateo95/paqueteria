from app.models.sucursal.ingreso_model import IngresoCreate, IngresoUpdate
from config.Connection import prisma_connection

class IngresoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.ingreso.find_many()

    async def get_by_id(self, ingreso_id: int):
        return await self.connection.prisma.ingreso.find_first(where={"id": ingreso_id})
    
    async def create(self, ingreso: IngresoCreate):
        return await self.connection.prisma.ingreso.create(ingreso)
    
    async def update(self, ingreso_id: int, ingreso: IngresoUpdate):
        return await self.connection.prisma.ingreso.update(where={"id": ingreso_id}, data=ingreso)

    async def delete(self, ingreso_id: int):
        return await self.connection.prisma.ingreso.delete(where={"id": ingreso_id})
