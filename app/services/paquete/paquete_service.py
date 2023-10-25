from app.repositories.paquete.paquete_repository import PaqueteRepository
from app.models.paquete.paquete_model import PaqueteCreate, PaqueteUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class PaqueteService:
    def __init(self):
        self.repository = PaqueteRepository()

    async def get_all(self):
        paquetes = await self.repository.get_all()
        if not paquetes:
            raise EntitiesNotFoundError("Paquetes")
        return paquetes

    async def get_by_id(self, paquete_id: int):
        paquete = await self.repository.get_by_id(paquete_id)
        if not paquete:
            raise EntityNotFoundError("Paquete", paquete_id)
        return paquete

    async def create(self, paquete: PaqueteCreate):
        try:
            return await self.repository.create(paquete)
        except Exception as e:
            raise EntityCreationError("Paquete")
        
    async def update(self, paquete_id: int, paquete: PaqueteUpdate):
        existing_paquete = await self.repository.get_by_id(paquete_id)
        if existing_paquete:
            paquete_update = {key: value for key, value in paquete.dict().items() if value is not None}
            if paquete_update:
                try:
                    return await self.repository.update(paquete_id, paquete_update)
                except Exception as e:
                    raise EntityUpdateError("Paquete")
        raise EntityNotFoundError("Paquete", paquete_id)

    async def delete(self, paquete_id: int):
        existing_paquete = await self.repository.get_by_id(paquete_id)
        if existing_paquete:
            try:
                return await self.repository.delete(paquete_id)
            except Exception as e:
                raise EntityDeletionError("Paquete")
        raise EntityNotFoundError("Paquete", paquete_id)
