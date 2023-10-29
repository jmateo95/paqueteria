from app.models.sucursal.vehiculo_model import VehiculoCreate, VehiculoUpdate
from config.Connection import prisma_connection

class VehiculoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.vehiculo.find_many()

    async def get_by_id(self, vehiculo_id: int):
        return await self.connection.prisma.vehiculo.find_first(where={"id": vehiculo_id})
    
    async def get_by_sucursal(self, sucursal_id: int):
        return await self.connection.prisma.vehiculo.find_many(
            where={"sucursal_id": sucursal_id}
        )
    
    async def create(self, vehiculo: VehiculoCreate):
        return await self.connection.prisma.vehiculo.create(vehiculo)
    
    async def update(self, vehiculo_id: int, vehiculo: VehiculoUpdate):
        return await self.connection.prisma.vehiculo.update(where={"id": vehiculo_id}, data=vehiculo)

    async def delete(self, vehiculo_id: int):
        return await self.connection.prisma.vehiculo.delete(where={"id": vehiculo_id})
