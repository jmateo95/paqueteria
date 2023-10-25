from app.repositories.sucursal.salida_repository import SalidaRepository
from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError,  EntityDeletionError

class SalidaService:
    def __init__(self):
        self.repository = SalidaRepository()

    async def get_all(self):
        salidas = await self.repository.get_all()
        if not salidas:
            raise EntitiesNotFoundError("Salidas")
        return salidas

    async def get_by_id(self, salida_id: int):
        salida = await self.repository.get_by_id(salida_id)
        if not salida:
            raise EntityNotFoundError("Salida", salida_id)
        return salida

    async def create(self, salida: SalidaCreate):
        try:
            return await self.repository.create(salida)
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
