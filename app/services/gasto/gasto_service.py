from app.repositories.gasto.gasto_repository import GastoRepository
from app.models.gasto.gasto_model import GastoCreate, GastoUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class GastoService:
    def __init__(self):
        self.repository = GastoRepository()
    
    async def get_gastos_by_filters(self, sucursal_id=None, tipo_gasto_id=None, fecha=None, test:bool=False):
        gastos = await self.repository.get_gastos_by_filters(sucursal_id=sucursal_id, tipo_gasto_id=tipo_gasto_id, fecha=fecha, test=test)
        return [] if not gastos else gastos

    async def get_by_id(self, gasto_id: int):
        gasto = await self.repository.get_by_id(gasto_id)
        if not gasto:
            raise EntityNotFoundError("Gasto", gasto_id)
        return gasto

    async def create(self, gasto: GastoCreate):
        try:
            return await self.repository.create(gasto.dict())
        except Exception as e:
            raise EntityCreationError("Gasto")
        
    async def update(self, gasto_id: int, gasto: GastoUpdate):
        existing_gasto = await self.repository.get_by_id(gasto_id)
        if existing_gasto:
            gasto_update = {key: value for key, value in gasto.dict().items() if value is not None}
            if gasto_update:
                try:
                    return await self.repository.update(gasto_id, gasto_update)
                except Exception as e:
                    raise EntityUpdateError("Gasto")
        raise EntityNotFoundError("Gasto", gasto_id)

    async def delete(self, gasto_id: int):
        existing_gasto = await self.repository.get_by_id(gasto_id)
        if existing_gasto:
            try:
                return await self.repository.delete(gasto_id)
            except Exception as e:
                raise EntityDeletionError("Gasto")
        raise EntityNotFoundError("Gasto", gasto_id)
