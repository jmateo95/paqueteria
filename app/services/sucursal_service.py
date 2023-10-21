from app.repositories.sucursal_repository import SucursalRepository
from app.models.sucursal_model import SucursalCreate, SucursalUpdate
from app.errors.sucursal_errors import SucursalNotFoundError, SucursalesNotFoundError, SucursalCreationError, SucursalUpdateError, SucursalDeletionError

class SucursalService:

    def __init__(self):
        self.repository = SucursalRepository()

    async def get_all(self):
        sucursales = await self.repository.get_all()
        if not sucursales:
            raise SucursalesNotFoundError()
        return sucursales

    async def get_by_id(self, sucursal_id: int):
        sucursal = await self.repository.get_by_id(sucursal_id)
        if not sucursal:
            raise SucursalNotFoundError(sucursal_id)
        return sucursal

    async def create(self, sucursal: SucursalCreate):
        try:
            return await self.repository.create(sucursal.dict())
        except Exception as e:
            raise SucursalCreationError()

    async def update(self, sucursal_id: int, sucursal: SucursalUpdate):
        existing_sucursal = await self.repository.get_by_id(sucursal_id)
        if existing_sucursal:
            sucursal_update = {key: value for key, value in sucursal.dict().items() if value is not None}
            if sucursal_update:
                try:
                    return await self.repository.update(sucursal_id, sucursal_update)
                except Exception as e:
                    raise SucursalUpdateError()
        raise SucursalNotFoundError(sucursal_id)

    async def delete(self, sucursal_id: int):
        existing_sucursal = await self.repository.get_by_id(sucursal_id)
        if existing_sucursal:
            try:
                return await self.repository.delete(sucursal_id)
            except Exception as e:
                raise SucursalDeletionError()
        raise SucursalNotFoundError(sucursal_id)