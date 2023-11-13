from app.repositories.sucursal.segmento_repository import SegmentoRepository
from app.models.sucursal.segmento_model import SegmentoCreate, SegmentoUpdate
from app.errors.common_errors import EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError, EntityNotFoundErrorByCharacteristics, CustomValidationError

class SegmentoService:
    def __init__(self):
        self.repository = SegmentoRepository()

    async def get_all(self):
        segmentos = await self.repository.get_all()
        return [] if not segmentos else segmentos

    async def get_by_id(self, segmento_id: int):
        segmento = await self.repository.get_by_id(segmento_id)
        if not segmento:
            raise EntityNotFoundError("Segmento", segmento_id)
        return segmento
    
    async def get_by_sucursal_origen(self, sucursal_origen_id: int):
        segmentos = await self.repository.get_by_sucursal_origen(sucursal_origen_id)
        return [] if not segmentos else segmentos
    
    async def get_by_sucursales(self, sucursal_origen_id: int, sucursal_destino_id: int):
        segmento = await self.repository.get_by_sucursales(sucursal_origen_id, sucursal_destino_id)
        return [] if not segmento else segmento

    async def create(self, segmento: SegmentoCreate):
        if segmento.sucursal_origen_id == segmento.sucursal_destino_id:
            raise CustomValidationError("Las sucursales de origen y destino deben ser diferentes.")
        try:
            segmento_2 = SegmentoCreate(
                **segmento.dict(exclude={"sucursal_origen_id", "sucursal_destino_id"}),
                sucursal_origen_id=segmento.sucursal_destino_id,
                sucursal_destino_id=segmento.sucursal_origen_id
            )
            await self.repository.create(segmento.dict())
            return await self.repository.create(segmento_2.dict())
        except Exception as e:
            raise EntityCreationError("Segmento")
        
    async def update(self, segmento_id: int, segmento: SegmentoUpdate):
        existing = await self.repository.get_by_id(segmento_id)
        if existing:
            segmento_update = {key: value for key, value in segmento.dict().items() if value is not None}
            if segmento_update:
                try:
                    return await self.repository.update(segmento_id, segmento_update)
                except Exception as e:
                    raise EntityUpdateError("Segmento")
        raise EntityNotFoundError("Segmento", segmento_id)

    async def delete(self, segmento_id: int):
        existing = await self.repository.get_by_id(segmento_id)
        if existing:
            try:
                return await self.repository.delete(segmento_id)
            except Exception as e:
                raise EntityDeletionError("Segmento")
        raise EntityNotFoundError("Segmento", segmento_id)
