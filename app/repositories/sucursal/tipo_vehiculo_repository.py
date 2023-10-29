from app.models.sucursal.tipo_vehiculo_model import TipoVehiculoCreate, TipoVehiculoUpdate
from config.Connection import prisma_connection

class TipoVehiculoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.tipovehiculo.find_many()

    async def get_by_id(self, tipo_vehiculo_id: int):
        return await self.connection.prisma.tipovehiculo.find_first(where={"id": tipo_vehiculo_id})
    
    async def create(self, tipo_vehiculo: TipoVehiculoCreate):
        return await self.connection.prisma.tipovehiculo.create(tipo_vehiculo)
    
    async def update(self, tipo_vehiculo_id: int, tipo_vehiculo: TipoVehiculoUpdate):
        return await self.connection.prisma.tipovehiculo.update(where={"id": tipo_vehiculo_id}, data=tipo_vehiculo)

    async def delete(self, tipo_vehiculo_id: int):
        return await self.connection.prisma.tipovehiculo.delete(where={"id": tipo_vehiculo_id})
