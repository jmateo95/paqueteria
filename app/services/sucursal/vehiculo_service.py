from app.repositories.sucursal.vehiculo_repository import VehiculoRepository
from app.models.sucursal.vehiculo_model import VehiculoCreate, VehiculoUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class VehiculoService:
    def __init__(self):
        self.repository = VehiculoRepository()

    async def get_all(self):
        vehiculos = await self.repository.get_all()
        if not vehiculos:
            raise EntitiesNotFoundError("Vehiculos")
        return vehiculos

    async def get_by_id(self, vehiculo_id: int):
        vehiculo = await self.repository.get_by_id(vehiculo_id)
        if not vehiculo:
            raise EntityNotFoundError("Vehiculo", vehiculo_id)
        return vehiculo

    async def create(self, vehiculo: VehiculoCreate):
        try:
            return await self.repository.create(vehiculo)
        except Exception as e:
            raise EntityCreationError("Vehiculo")
        
    async def update(self, vehiculo_id: int, vehiculo: VehiculoUpdate):
        existing_vehiculo = await self.repository.get_by_id(vehiculo_id)
        if existing_vehiculo:
            vehiculo_update = {key: value for key, value in vehiculo.dict().items() if value is not None}
            if vehiculo_update:
                try:
                    return await self.repository.update(vehiculo_id, vehiculo_update)
                except Exception as e:
                    raise EntityUpdateError("Vehiculo")
        raise EntityNotFoundError("Vehiculo", vehiculo_id)

    async def delete(self, vehiculo_id: int):
        existing_vehiculo = await self.repository.get_by_id(vehiculo_id)
        if existing_vehiculo:
            try:
                return await self.repository.delete(vehiculo_id)
            except Exception as e:
                raise EntityDeletionError("Vehiculo")
        raise EntityNotFoundError("Vehiculo", vehiculo_id)
