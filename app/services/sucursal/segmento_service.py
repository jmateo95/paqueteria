from app.repositories.sucursal.segmento_repository import SegmentoRepository
from app.models.sucursal.segmento_model import SegmentoCreate, SegmentoUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class SegmentoService:
    def __init(self):
        self.repository = SegmentoRepository()

    async def get_all(self):
        segmentos = await self.repository.get_all()
        if not segmentos:
            raise EntitiesNotFoundError("Segmentos")
        return segmentos

    async def get_by_id(self, segmento_id: int):
        segmento = await self.repository.get_by_id(segmento_id)
        if not segmento:
            raise EntityNotFoundError("Segmento", segmento_id)
        return segmento

    async def create(self, segmento: SegmentoCreate):
        try:
            return await self.repository.create(segmento.dict())
        except Exception as e:
            raise EntityCreationError("Segmento")
        
    async def update(self, segmento_id: int, segmento: SegmentoUpdate):
        existing_segmento = await self.repository.get_by_id(segmento_id)
        if existing_segmento:
            segmento_update = {key: value for key, value in segmento.dict().items() if value is not None}
            if segmento_update:
                try:
                    return await self.repository.update(segmento_id, segmento_update)
                except Exception as e:
                    raise EntityUpdateError("Segmento")
        raise EntityNotFoundError("Segmento", segmento_id)

    async def delete(self, segmento_id: int):
        existing_segmento = await self.repository.get_by_id(segmento_id)
        if existing_segmento:
            try:
                return await self.repository.delete(segmento_id)
            except Exception as e:
                raise EntityDeletionError("Segmento")
        raise EntityNotFoundError("Segmento", segmento_id)
