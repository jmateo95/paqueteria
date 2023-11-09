from app.models.paquete.paquete_model import PaqueteCreate, PaqueteUpdate, PaqueteCotizar
from config.Connection import prisma_connection

class PaqueteRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_paquetes_by_filters(self, salida_id:int=None, tipo_tracking_id:int=None, estado_paquete_id:int=None):
        query = """
            SELECT DISTINCT P.*
            FROM public."Paquete" P
            INNER JOIN public."Tracking" T ON P.id = T.paquete_id
            WHERE 1=1
        """
        if salida_id is not None:
            query += f"AND T.salida_id = {salida_id}\n"
        if tipo_tracking_id is not None:
            query += f"AND T.estado_tracking_id = {tipo_tracking_id}\n"
        if estado_paquete_id is not None:
            query += f"AND P.estado_paquete_id = {estado_paquete_id}\n"
        return await self.connection.prisma.query_raw(query)

    async def get_by_id(self, paquete_id: int):
        return await self.connection.prisma.paquete.find_first(where={"id": paquete_id})
    
    async def create(self, paquete: PaqueteCreate):
        return await self.connection.prisma.paquete.create(paquete)
    
    async def update(self, paquete_id: int, paquete: PaqueteUpdate):
        return await self.connection.prisma.paquete.update(where={"id": paquete_id}, data=paquete)

    async def delete(self, paquete_id: int):
        return await self.connection.prisma.paquete.delete(where={"id": paquete_id})
