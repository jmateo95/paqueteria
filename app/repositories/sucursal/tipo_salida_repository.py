from app.models.sucursal.tipo_salida_model import TipoSalidaCreate, TipoSalidaUpdate
from config.Connection import prisma_connection

class TipoSalidaRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.tiposalida.find_many()

    async def get_by_id(self, tipo_salida_id: int):
        return await self.connection.prisma.tiposalida.find_first(where={"id": tipo_salida_id})
    
    async def create(self, tipo_salida: TipoSalidaCreate):
        return await self.connection.prisma.tiposalida.create(tipo_salida)
    
    async def update(self, tipo_salida_id: int, tipo_salida: TipoSalidaUpdate):
        return await self.connection.prisma.tiposalida.update(where={"id": tipo_salida_id}, data=tipo_salida)

    async def delete(self, tipo_salida_id: int):
        return await self.connection.prisma.tiposalida.delete(where={"id": tipo_salida_id})
