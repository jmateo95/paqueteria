from app.enums.enums import EstadoTracking, TipoSalida
from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate
from config.Connection import prisma_connection
from datetime import datetime
import calendar

class SalidaRepository:
    def __init__(self):
        self.connection = prisma_connection
    
    async def get_salidas_by_filters(self, sucursal_id:int=None, tipo_salida_id:int=None,  fecha:datetime=None):
        where_conditions = {}
        
        if tipo_salida_id is not None:
            where_conditions = {"tipo_salida_id": tipo_salida_id}   

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
        return await self.connection.prisma.salida.find_many(include={"segmento": {"include": {"sucursal_origen": True}}},where=where_conditions)

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
    
    async def update_status_salida_and_tracking(self, salida_id):
        await self.connection.prisma.execute_raw("BEGIN;")
        try:
            # Actualiza la salida a tipo_salida_id igual a $2 si se cumplen las condiciones
            await self.connection.prisma.execute_raw(
                """
                UPDATE public."Salida" S
                SET tipo_salida_id = CASE
                    WHEN NOT EXISTS (
                        SELECT 1
                        FROM public."Tracking" T
                        WHERE T.salida_id = S.id
                        AND T.estado_tracking_id <> $3
                    ) AND S.capacidad_reservada = S.capacidad_lb THEN $2
                    ELSE S.tipo_salida_id
                END
                WHERE S.id = $1;
                """,
                salida_id, TipoSalida.LISTO_PARA_CARGAR, EstadoTracking.EN_BODEGA
            )

            # Actualiza los trackings a estado $4 si la salida se actualiza
            await self.connection.prisma.execute_raw(
                """
                UPDATE public."Tracking" T
                SET estado_tracking_id = $3
                WHERE T.salida_id = $1
                AND EXISTS (
                    SELECT 1
                    FROM public."Salida" S
                    WHERE S.id = $1
                    AND S.tipo_salida_id = $2
                );
                """,
                salida_id, TipoSalida.LISTO_PARA_CARGAR, EstadoTracking.CARGANDO
            )
            # Confirmar la transacción
            await self.connection.prisma.execute_raw("COMMIT;")
        except Exception as e:
            # En caso de error, realizar un rollback
            await self.connection.prisma.execute_raw("ROLLBACK;")
            raise e
        return "Operación completada exitosamente"