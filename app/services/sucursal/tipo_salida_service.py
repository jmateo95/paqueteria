from app.repositories.sucursal.tipo_salida_repository import TipoSalidaRepository
from app.models.sucursal.tipo_salida_model import TipoSalidaCreate, TipoSalidaUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class TipoSalidaService:
    def __init__(self):
        self.repository = TipoSalidaRepository()

    async def get_all(self):
        tipos_salida = await self.repository.get_all()
        if not tipos_salida:
            raise EntitiesNotFoundError("Tipos de Salida")
        return tipos_salida

    async def get_by_id(self, tipo_salida_id: int):
        tipo_salida = await self.repository.get_by_id(tipo_salida_id)
        if not tipo_salida:
            raise EntityNotFoundError("Tipo de Salida", tipo_salida_id)
        return tipo_salida

    async def create(self, tipo_salida: TipoSalidaCreate):
        try:
            return await self.repository.create(tipo_salida.dict())
        except Exception as e:
            raise EntityCreationError("Tipo de Salida")
        
    async def update(self, tipo_salida_id: int, tipo_salida: TipoSalidaUpdate):
        existing_tipo_salida = await self.repository.get_by_id(tipo_salida_id)
        if existing_tipo_salida:
            tipo_salida_update = {key: value for key, value in tipo_salida.dict().items() if value is not None}
            if tipo_salida_update:
                try:
                    return await self.repository.update(tipo_salida_id, tipo_salida_update)
                except Exception as e:
                    raise EntityUpdateError("Tipo de Salida")
        raise EntityNotFoundError("Tipo de Salida", tipo_salida_id)

    async def delete(self, tipo_salida_id: int):
        existing_tipo_salida = await self.repository.get_by_id(tipo_salida_id)
        if existing_tipo_salida:
            try:
                return await self.repository.delete(tipo_salida_id)
            except Exception as e:
                raise EntityDeletionError("Tipo de Salida")
        raise EntityNotFoundError("Tipo de Salida", tipo_salida_id)
