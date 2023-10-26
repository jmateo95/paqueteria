from app.repositories.sucursal.sucursal_repository import SucursalRepository
from app.models.sucursal.sucursal_model import SucursalCreate, SucursalUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class SucursalService:

    def __init__(self):
        self.repository = SucursalRepository()

    async def get_all(self):
        sucursales = await self.repository.get_all()
        if not sucursales:
            return []
        return sucursales

    async def get_by_id(self, sucursal_id: int):
        sucursal = await self.repository.get_by_id(sucursal_id)
        if not sucursal:
            raise EntityNotFoundError("Sucursal", sucursal_id)
        return sucursal

    async def create(self, sucursal: SucursalCreate):
        try:
            return await self.repository.create(sucursal.dict())
        except Exception as e:
            raise EntityCreationError("Sucursal")

    async def update(self, sucursal_id: int, sucursal: SucursalUpdate):
        existing_sucursal = await self.repository.get_by_id(sucursal_id)
        if existing_sucursal:
            sucursal_update = {key: value for key, value in sucursal.dict().items() if value is not None}
            if sucursal_update:
                try:
                    return await self.repository.update(sucursal_id, sucursal_update)
                except Exception as e:
                    raise EntityUpdateError("Sucursal")
        raise EntityNotFoundError("Sucursal", sucursal_id)

    async def delete(self, sucursal_id: int):
        existing_sucursal = await self.repository.get_by_id(sucursal_id)
        if existing_sucursal:
            try:
                return await self.repository.delete(sucursal_id)
            except Exception as e:
                raise EntityDeletionError("Sucursal")
        raise EntityNotFoundError("Sucursal", sucursal_id)