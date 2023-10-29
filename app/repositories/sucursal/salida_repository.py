from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate
from config.Connection import prisma_connection
from datetime import datetime
import calendar

class SalidaRepository:
    def __init__(self):
        self.connection = prisma_connection
    
    async def get_salidas_by_filters(self, sucursal_id=None, fecha:datetime=None):
        where_conditions = {}        
        if sucursal_id is not None:
            original_filter = {
                'segmento': {
                    'is': {
                        'sucursal_origen_id': sucursal_id,
                    },
                }
            }
            where_conditions.update(original_filter)

        if fecha is not None:
           first_day = fecha.replace(day=1, hour=0, minute=0, second=0)
           last_day = fecha.replace(day=calendar.monthrange(fecha.year, fecha.month)[1], hour=23, minute=59, second=59)
           where_conditions["fecha_programada"] = {"gte": first_day, "lte": last_day}
        return await self.connection.prisma.salida.find_many(include={"segmento": True},where=where_conditions)

    async def get_by_id(self, salida_id: int):
        return await self.connection.prisma.salida.find_first(where={"id": salida_id})
    
    async def create(self, salida: SalidaCreate):
        return await self.connection.prisma.salida.create(salida)
    
    async def update(self, salida_id: int, salida: SalidaUpdate):
        return await self.connection.prisma.salida.update(where={"id": salida_id}, data=salida)

    async def delete(self, salida_id: int):
        return await self.connection.prisma.salida.delete(where={"id": salida_id})
    
    async def get_salidas_by_capacity(self, tipo_salida, peso):
        query = """
                SELECT S.id, S.costo_lb, SE.distancia, SE.sucursal_origen_id, SE.sucursal_destino_id, S.capacidad_reservada
                FROM public."Salida" S
                INNER JOIN public."Segmento" SE on SE.id=S.segmento_id
                WHERE S.tipo_salida_id=$1 AND S.capacidad_lb>=(S.capacidad_reservada+$2)"""
        return await self.connection.prisma.query_raw(query, tipo_salida, peso)