from app.repositories.gasto.tipo_gasto_repository import TipoGastoRepository
from app.models.gasto.tipo_gasto_model import TipoGastoCreate, TipoGastoUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class TipoGastoService:
    def __init__(self):
        self.repository = TipoGastoRepository()

    async def get_all(self):
        tipo_gastos = await self.repository.get_all()
        if not tipo_gastos:
            return []
        return tipo_gastos

    async def get_by_id(self, tipo_gasto_id: int):
        tipo_gasto = await self.repository.get_by_id(tipo_gasto_id)
        if not tipo_gasto:
            raise EntityNotFoundError("TipoGasto", tipo_gasto_id)
        return tipo_gasto

    async def create(self, tipo_gasto: TipoGastoCreate):
        try:
            return await self.repository.create(tipo_gasto.dict())
        except Exception as e:
            raise EntityCreationError("TipoGasto")
        
    async def update(self, tipo_gasto_id: int, tipo_gasto: TipoGastoUpdate):
        existing_tipo_gasto = await self.repository.get_by_id(tipo_gasto_id)
        if existing_tipo_gasto:
            tipo_gasto_update = {key: value for key, value in tipo_gasto.dict().items() if value is not None}
            if tipo_gasto_update:
                try:
                    return await self.repository.update(tipo_gasto_id, tipo_gasto_update)
                except Exception as e:
                    raise EntityUpdateError("TipoGasto")
        raise EntityNotFoundError("TipoGasto", tipo_gasto_id)

    async def delete(self, tipo_gasto_id: int):
        existing_tipo_gasto = await self.repository.get_by_id(tipo_gasto_id)
        if existing_tipo_gasto:
            try:
                return await self.repository.delete(tipo_gasto_id)
            except Exception as e:
                raise EntityDeletionError("TipoGasto")
        raise EntityNotFoundError("TipoGasto", tipo_gasto_id)
