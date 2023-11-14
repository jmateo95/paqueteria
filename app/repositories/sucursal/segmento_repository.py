from app.models.sucursal.segmento_model import SegmentoCreate, SegmentoUpdate
from config.Connection import prisma_connection

class SegmentoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self, test:bool=False):
        where_conditions = {}
        if not test:
            where_conditions["test"] = test
        return await self.connection.prisma.segmento.find_many(include={"sucursal_destino":True,"sucursal_origen":True}, where=where_conditions, order=[{"id": "desc"}])

    async def get_by_id(self, segmento_id: int):
        return await self.connection.prisma.segmento.find_first(where={"id": segmento_id})
    
    async def get_by_sucursal_origen(self, sucursal_origen_id: int, test:bool=False):
        where_params = {"sucursal_origen_id": sucursal_origen_id}
        if not test:
            where_params["test"] = False
        return await self.connection.prisma.segmento.find_many(where=where_params)
    
    async def get_by_sucursales(self, sucursal_origen_id: int, sucursal_destino_id: int, test:bool=False):
        where_params = {"sucursal_origen_id": sucursal_origen_id, "sucursal_destino_id": sucursal_destino_id}
        if not test:
            where_params["test"] = False
        return await self.connection.prisma.segmento.find_first(where=where_params)
    
    async def create(self, segmento: SegmentoCreate):
        return await self.connection.prisma.segmento.create(segmento)
    
    async def update(self, segmento_id: int, segmento: SegmentoUpdate):
        return await self.connection.prisma.segmento.update(where={"id": segmento_id}, data=segmento)

    async def delete(self, segmento_id: int):
        return await self.connection.prisma.segmento.delete(where={"id": segmento_id})
