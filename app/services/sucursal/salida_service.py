from app.enums.enums import TipoSalida
from app.repositories.sucursal.salida_repository import SalidaRepository
from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate, Salida
from app.errors.common_errors import EntityNotFoundError, EntityCreationError, EntityUpdateError,  EntityDeletionError
from app.repositories.sucursal.segmento_repository import SegmentoRepository
from app.repositories.sucursal.vehiculo_repository import VehiculoRepository
from datetime import datetime

class SalidaService:
    def __init__(self):
        self.repository = SalidaRepository()
        self.vehiculo_repository = VehiculoRepository()
        self.segmento_repository = SegmentoRepository()

    async def get_salidas_by_filters(self, sucursal_id=None, fecha=None):
        salidas = await self.repository.get_salidas_by_filters(sucursal_id, fecha)
        return [] if not salidas else salidas

    async def get_by_id(self, salida_id: int):
        salida = await self.repository.get_by_id(salida_id)
        if not salida:
            raise EntityNotFoundError("Salida", salida_id)
        return salida

    async def create(self, salida: SalidaCreate):
        try:
            #Obtener los valores
            vehiculo = await self.vehiculo_repository.get_by_id(salida.vehiculo_id)
            segmento = await self.segmento_repository.get_by_id(salida.segmento_id)
            segmento_2=await self.segmento_repository.get_by_sucursales(sucursal_origen_id=segmento.sucursal_destino_id, sucursal_destino_id=segmento.sucursal_origen_id)
            if not vehiculo or not segmento or not segmento_2:
                raise EntityCreationError("Salida")
            #Crear Objeto Salida
            salida_1 = Salida(
                tipo_salida_id      = TipoSalida.PROYECCION,
                vehiculo_id         = vehiculo.id,
                segmento_id         = segmento.id,
                fecha_programada    = datetime.now(),
                comentario          = '',
                costo_lb            = round(vehiculo.costo_km * segmento.distancia / vehiculo.capacidad_lb, 2),
                capacidad_lb        = vehiculo.capacidad_lb,
                capacidad_reservada = 0,
                capacidad_ocupada   = 0,
            )

            salida_2 = Salida(
                **salida_1.dict(exclude={"segmento_id"}),
                segmento_id = segmento_2.id,
            )
            
            #Guardar Salidias
            await self.repository.create(salida_1.dict())
            return await self.repository.create(salida_2.dict())
        except Exception as e:
            raise EntityCreationError("Salida")
        
    async def update(self, salida_id: int, salida: SalidaUpdate):
        existing_salida = await self.repository.get_by_id(salida_id)
        if existing_salida:
            salida_update = {key: value for key, value in salida.dict().items() if value is not None}
            if salida_update:
                try:
                    return await self.repository.update(salida_id, salida_update)
                except Exception as e:
                    raise EntityUpdateError("Salida")
        raise EntityNotFoundError("Salida", salida_id)

    async def delete(self, salida_id: int):
        existing_salida = await self.repository.get_by_id(salida_id)
        if existing_salida:
            try:
                return await self.repository.delete(salida_id)
            except Exception as e:
                raise EntityDeletionError("Salida")
        raise EntityNotFoundError("Salida", salida_id)
