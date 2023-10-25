from app.repositories.paquete.tracking_repository import TrackingRepository
from app.models.paquete.tracking_model import TrackingCreate, TrackingUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class TrackingService:
    def __init(self):
        self.repository = TrackingRepository()

    async def get_all(self):
        trackings = await self.repository.get_all()
        if not trackings:
            raise EntitiesNotFoundError("Trackings")
        return trackings

    async def get_by_id(self, tracking_id: int):
        tracking = await self.repository.get_by_id(tracking_id)
        if not tracking:
            raise EntityNotFoundError("Tracking", tracking_id)
        return tracking

    async def create(self, tracking: TrackingCreate):
        try:
            return await self.repository.create(tracking)
        except Exception as e:
            raise EntityCreationError("Tracking")
        
    async def update(self, tracking_id: int, tracking: TrackingUpdate):
        existing_tracking = await self.repository.get_by_id(tracking_id)
        if existing_tracking:
            tracking_update = {key: value for key, value in tracking.dict().items() if value is not None}
            if tracking_update:
                try:
                    return await self.repository.update(tracking_id, tracking_update)
                except Exception as e:
                    raise EntityUpdateError("Tracking")
        raise EntityNotFoundError("Tracking", tracking_id)

    async def delete(self, tracking_id: int):
        existing_tracking = await self.repository.get_by_id(tracking_id)
        if existing_tracking:
            try:
                return await self.repository.delete(tracking_id)
            except Exception as e:
                raise EntityDeletionError("Tracking")
        raise EntityNotFoundError("Tracking", tracking_id)
