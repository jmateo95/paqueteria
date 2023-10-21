from app.repositories.tipo_sucursal_repository import TipoSucursalRepository
from app.models.tipo_sucursal_model import TipoSucursalCreate, TipoSucursalUpdate
from app.errors.tipo_sucursal_errors import TipoSucursalNotFoundError, TipoSucursalesNotFoundError, TipoSucursalCreationError, TipoSucursalUpdateError, TipoSucursalDeletionError

class TipoSucursalService:

    def __init(self):
        self.repository = TipoSucursalRepository()

    async def get_all(self):
        tipo_sucursales = await self.repository.get_all()
        if not tipo_sucursales:
            raise TipoSucursalesNotFoundError()
        return tipo_sucursales

    async def get_by_id(self, tipo_sucursal_id: int):
        tipo_sucursal = await self.repository.get_by_id(tipo_sucursal_id)
        if not tipo_sucursal:
            raise TipoSucursalNotFoundError(tipo_sucursal_id)
        return tipo_sucursal

    async def create(self, tipo_sucursal: TipoSucursalCreate):
        try:
            return await self.repository.create(tipo_sucursal.dict())
        except Exception as e:
            raise TipoSucursalCreationError()

    async def update(self, tipo_sucursal_id: int, tipo_sucursal: TipoSucursalUpdate):
        existing_tipo_sucursal = await self.repository.get_by_id(tipo_sucursal_id)
        if existing_tipo_sucursal:
            tipo_sucursal_update = {key: value for key, value in tipo_sucursal.dict().items() if value is not None}
            if tipo_sucursal_update:
                try:
                    return await self.repository.update(tipo_sucursal_id, tipo_sucursal_update)
                except Exception as e:
                    raise TipoSucursalUpdateError()
        raise TipoSucursalNotFoundError(tipo_sucursal_id)

    async def delete(self, tipo_sucursal_id: int):
        existing_tipo_sucursal = await self.repository.get_by_id(tipo_sucursal_id)
        if existing_tipo_sucursal:
            try:
                return await self.repository.delete(tipo_sucursal_id)
            except Exception as e:
                raise TipoSucursalDeletionError()
        raise TipoSucursalNotFoundError(tipo_sucursal_id)