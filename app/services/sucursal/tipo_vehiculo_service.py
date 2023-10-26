from app.repositories.sucursal.tipo_vehiculo_repository import TipoVehiculoRepository
from app.models.sucursal.tipo_vehiculo_model import TipoVehiculoCreate, TipoVehiculoUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class TipoVehiculoService:
    def __init__(self):
        self.repository = TipoVehiculoRepository()

    async def get_all(self):
        tipo_vehiculos = await self.repository.get_all()
        if not tipo_vehiculos:
            return []
        return tipo_vehiculos

    async def get_by_id(self, tipo_vehiculo_id: int):
        tipo_vehiculo = await self.repository.get_by_id(tipo_vehiculo_id)
        if not tipo_vehiculo:
            raise EntityNotFoundError("TipoVehiculo", tipo_vehiculo_id)
        return tipo_vehiculo

    async def create(self, tipo_vehiculo: TipoVehiculoCreate):
        try:
            return await self.repository.create(tipo_vehiculo.dict())
        except Exception as e:
            raise EntityCreationError("TipoVehiculo")
        
    async def update(self, tipo_vehiculo_id: int, tipo_vehiculo: TipoVehiculoUpdate):
        existing_tipo_vehiculo = await self.repository.get_by_id(tipo_vehiculo_id)
        if existing_tipo_vehiculo:
            tipo_vehiculo_update = {key: value for key, value in tipo_vehiculo.dict().items() if value is not None}
            if tipo_vehiculo_update:
                try:
                    return await self.repository.update(tipo_vehiculo_id, tipo_vehiculo_update)
                except Exception as e:
                    raise EntityUpdateError("TipoVehiculo")
        raise EntityNotFoundError("TipoVehiculo", tipo_vehiculo_id)

    async def delete(self, tipo_vehiculo_id: int):
        existing_tipo_vehiculo = await self.repository.get_by_id(tipo_vehiculo_id)
        if existing_tipo_vehiculo:
            try:
                return await self.repository.delete(tipo_vehiculo_id)
            except Exception as e:
                raise EntityDeletionError("TipoVehiculo")
        raise EntityNotFoundError("TipoVehiculo", tipo_vehiculo_id)
