from app.repositories.paquete.estado_paquete_repository import EstadoPaqueteRepository
from app.models.paquete.estado_paquete_model import EstadoPaqueteCreate, EstadoPaqueteUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class EstadoPaqueteService:
    def __init(self):
        self.repository = EstadoPaqueteRepository()

    async def get_all(self):
        estados_paquete = await self.repository.get_all()
        if not estados_paquete:
            raise EntitiesNotFoundError("Estados de Paquete")
        return estados_paquete

    async def get_by_id(self, estado_paquete_id: int):
        estado_paquete = await self.repository.get_by_id(estado_paquete_id)
        if not estado_paquete:
            raise EntityNotFoundError("Estado de Paquete", estado_paquete_id)
        return estado_paquete

    async def create(self, estado_paquete: EstadoPaqueteCreate):
        try:
            return await self.repository.create(estado_paquete.dict())
        except Exception as e:
            raise EntityCreationError("Estado de Paquete")
        
    async def update(self, estado_paquete_id: int, estado_paquete: EstadoPaqueteUpdate):
        existing_estado_paquete = await self.repository.get_by_id(estado_paquete_id)
        if existing_estado_paquete:
            estado_paquete_update = {key: value for key, value in estado_paquete.dict().items() if value is not None}
            if estado_paquete_update:
                try:
                    return await self.repository.update(estado_paquete_id, estado_paquete_update)
                except Exception as e:
                    raise EntityUpdateError("Estado de Paquete")
        raise EntityNotFoundError("Estado de Paquete", estado_paquete_id)

    async def delete(self, estado_paquete_id: int):
        existing_estado_paquete = await self.repository.get_by_id(estado_paquete_id)
        if existing_estado_paquete:
            try:
                return await self.repository.delete(estado_paquete_id)
            except Exception as e:
                raise EntityDeletionError("Estado de Paquete")
        raise EntityNotFoundError("Estado de Paquete", estado_paquete_id)
