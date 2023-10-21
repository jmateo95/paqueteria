from app.models.tipo_sucursal_model import TipoSucursalCreate, TipoSucursalUpdate
from config.Connection import prisma_connection

class TipoSucursalRepository:

    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.tiposucursal.find_many()

    async def get_by_id(self, tipo_sucursal_id: int):
        return await self.connection.prisma.tiposucursal.find_first(where={"id": tipo_sucursal_id})

    async def create(self, tipo_sucursal: TipoSucursalCreate):
        return await self.connection.prisma.tiposucursal.create(tipo_sucursal)

    async def update(self, tipo_sucursal_id: int, tipo_sucursal: TipoSucursalUpdate):
        return await self.connection.prisma.tiposucursal.update(where={"id": tipo_sucursal_id}, data=tipo_sucursal)

    async def delete(self, tipo_sucursal_id: int):
        return await self.connection.prisma.tiposucursal.delete(where={"id": tipo_sucursal_id})
