from app.repositories.paquete.estado_tracking_repository import EstadoTrackingRepository
from app.models.paquete.estado_tracking_model import EstadoTrackingCreate, EstadoTrackingUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class EstadoTrackingService:
    def __init__(self):
        self.repository = EstadoTrackingRepository()

    async def get_all(self):
        estados_tracking = await self.repository.get_all()
        if not estados_tracking:
            return []
        return estados_tracking

    async def get_by_id(self, estado_tracking_id: int):
        estado_tracking = await self.repository.get_by_id(estado_tracking_id)
        if not estado_tracking:
            raise EntityNotFoundError("Estado de Tracking", estado_tracking_id)
        return estado_tracking

    async def create(self, estado_tracking: EstadoTrackingCreate):
        try:
            return await self.repository.create(estado_tracking.dict())
        except Exception as e:
            raise EntityCreationError("Estado de Tracking")
        
    async def update(self, estado_tracking_id: int, estado_tracking: EstadoTrackingUpdate):
        existing_estado_tracking = await self.repository.get_by_id(estado_tracking_id)
        if existing_estado_tracking:
            estado_tracking_update = {key: value for key, value in estado_tracking.dict().items() if value is not None}
            if estado_tracking_update:
                try:
                    return await self.repository.update(estado_tracking_id, estado_tracking_update)
                except Exception as e:
                    raise EntityUpdateError("Estado de Tracking")
        raise EntityNotFoundError("Estado de Tracking", estado_tracking_id)

    async def delete(self, estado_tracking_id: int):
        existing_estado_tracking = await self.repository.get_by_id(estado_tracking_id)
        if existing_estado_tracking:
            try:
                return await self.repository.delete(estado_tracking_id)
            except Exception as e:
                raise EntityDeletionError("Estado de Tracking")
        raise EntityNotFoundError("Estado de Tracking", estado_tracking_id)
