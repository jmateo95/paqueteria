from app.repositories.sucursal.tarifario_repository import TarifarioRepository
from app.models.sucursal.tarifario_model import TarifarioCreate, TarifarioUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class TarifarioService:
    def __init__(self):
        self.repository = TarifarioRepository()

    async def get_all(self):
        tarifarios = await self.repository.get_all()
        if not tarifarios:
            return []
        return tarifarios

    async def get_by_id(self, tarifario_id: int):
        tarifario = await self.repository.get_by_id(tarifario_id)
        if not tarifario:
            raise EntityNotFoundError("Tarifario", tarifario_id)
        return tarifario

    async def create(self, tarifario: TarifarioCreate):
        try:
            return await self.repository.create(tarifario.dict())
        except Exception as e:
            raise EntityCreationError("Tarifario")
        
    async def update(self, tarifario_id: int, tarifario: TarifarioUpdate):
        existing_tarifario = await self.repository.get_by_id(tarifario_id)
        if existing_tarifario:
            tarifario_update = {key: value for key, value in tarifario.dict().items() if value is not None}
            if tarifario_update:
                try:
                    return await self.repository.update(tarifario_id, tarifario_update)
                except Exception as e:
                    raise EntityUpdateError("Tarifario")
        raise EntityNotFoundError("Tarifario", tarifario_id)

    async def delete(self, tarifario_id: int):
        existing_tarifario = await self.repository.get_by_id(tarifario_id)
        if existing_tarifario:
            try:
                return await self.repository.delete(tarifario_id)
            except Exception as e:
                raise EntityDeletionError("Tarifario")
        raise EntityNotFoundError("Tarifario", tarifario_id)
