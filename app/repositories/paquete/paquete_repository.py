from app.models.paquete.paquete_model import PaqueteCreate, PaqueteUpdate, PaqueteCotizar
from config.Connection import prisma_connection

class PaqueteRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_paquetes_by_filters(self, salida_id:int=None, tipo_tracking_id:int=None, estado_paquete_id:int=None, sucursal_id:int=None):
        query = """
            SELECT DISTINCT ON (P.id) P.*, 
            (
                SELECT SU1.nombre
                FROM public."Tracking" T1 
                INNER JOIN public."Salida" S1 ON T1.salida_id = S1.id
                INNER JOIN public."Segmento" SE1 ON S1.segmento_id = SE1.id
                INNER JOIN public."Sucursal" SU1 ON SE1.sucursal_origen_id = SU1.id
                WHERE T1.paquete_id = P.id 
                ORDER BY T1.id ASC 
                LIMIT 1
            ) AS origen,
            (
                SELECT SU2.nombre
                FROM public."Tracking" T2 
                INNER JOIN public."Salida" S2 ON T2.salida_id = S2.id
                INNER JOIN public."Segmento" SE2 ON S2.segmento_id = SE2.id
                INNER JOIN public."Sucursal" SU2 ON SE2.sucursal_destino_id = SU2.id
                WHERE T2.paquete_id = P.id 
                ORDER BY T2.id DESC 
                LIMIT 1
            ) AS destino
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
        if sucursal_id is not None:
            query += f"AND T.sucursal_id = {sucursal_id}\n"
        return await self.connection.prisma.query_raw(query)

    async def get_by_id(self, paquete_id: int):
        return await self.connection.prisma.paquete.find_first(where={"id": paquete_id})
    
    async def get_by_no_guia(self, no_guia: int):
        return await self.connection.prisma.paquete.find_first(where={"no_guia": no_guia})
    
    async def create(self, paquete: PaqueteCreate):
        return await self.connection.prisma.paquete.create(paquete)
    
    async def update(self, paquete_id: int, paquete: PaqueteUpdate):
        return await self.connection.prisma.paquete.update(where={"id": paquete_id}, data=paquete)

    async def delete(self, paquete_id: int):
        return await self.connection.prisma.paquete.delete(where={"id": paquete_id})
