from app.models.sucursal.sucursal_model import SucursalCreate, SucursalUpdate
from config.Connection import prisma_connection

class SucursalRepository:

    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.sucursal.find_many(include={"ciudad":True,"tipoSucursal":True})

    async def get_by_id(self, sucursal_id: int):
        return await self.connection.prisma.sucursal.find_first(where={"id": sucursal_id})

    async def create(self, sucursal: SucursalCreate):
        return await self.connection.prisma.sucursal.create(sucursal)

    async def update(self, sucursal_id: int, sucursal: SucursalUpdate):
        return await self.connection.prisma.sucursal.update(where={"id": sucursal_id}, data=sucursal)

    async def delete(self, sucursal_id: int):
        return await self.connection.prisma.sucursal.delete(where={"id": sucursal_id})