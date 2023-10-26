from app.repositories.usuario.puesto_repository import PuestoRepository
from app.models.usuario.puesto_model import PuestoCreate, PuestoUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError
from schema import ResponseSchema

class PuestoService:

    def __init__(self):
        self.repository = PuestoRepository()

    async def get_all(self):
        puestos = await self.repository.get_all()
        if not puestos:
            return []
        return puestos

    async def get_by_id(self, puesto_id: int):
        puesto = await self.repository.get_by_id(puesto_id)
        if not puesto:
            raise EntityNotFoundError("Puesto", puesto_id)
        return puesto

    async def create(self, puesto: PuestoCreate):
        try:
            return await self.repository.create(puesto.dict())
        except Exception as e:
            raise EntityCreationError("Puesto")

    async def update(self, puesto_id: int, puesto: PuestoUpdate):
        existing_puesto = await self.repository.get_by_id(puesto_id)
        if existing_puesto:
            puesto_update = {key: value for key, value in puesto.dict().items() if value is not None}
            if puesto_update:
                try:
                    return await self.repository.update(puesto_id, puesto_update)
                except Exception as e:
                    raise EntityUpdateError("Puesto")
        raise EntityNotFoundError("Puesto", puesto_id)

    async def delete(self, puesto_id: int):
        existing_puesto = await self.repository.get_by_id(puesto_id)
        if existing_puesto:
            try:
                return await self.repository.delete(puesto_id)
            except Exception as e:
                raise EntityDeletionError("Puesto")
        raise EntityNotFoundError("Puesto", puesto_id)