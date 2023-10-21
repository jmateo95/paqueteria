from app.repositories.puesto_repository import PuestoRepository
from app.models.puesto_model import PuestoCreate, PuestoUpdate
from app.errors.puesto_errors import PuestoNotFoundError, PuestosNotFoundError, PuestoCreationError, PuestoUpdateError, PuestoDeletionError

class PuestoService:

    def __init__(self):
        self.repository = PuestoRepository()

    async def get_all(self):
        puestos = await self.repository.get_all()
        if not puestos:
            raise PuestosNotFoundError()
        return puestos

    async def get_by_id(self, puesto_id: int):
        puesto = await self.repository.get_by_id(puesto_id)
        if not puesto:
            raise PuestoNotFoundError(puesto_id)
        return puesto

    async def create(self, puesto: PuestoCreate):
        try:
            return await self.repository.create(puesto.dict())
        except Exception as e:
            raise PuestoCreationError()

    async def update(self, puesto_id: int, puesto: PuestoUpdate):
        existing_puesto = await self.repository.get_by_id(puesto_id)
        if existing_puesto:
            puesto_update = {key: value for key, value in puesto.dict().items() if value is not None}
            if puesto_update:
                try:
                    return await self.repository.update(puesto_id, puesto_update)
                except Exception as e:
                    raise PuestoUpdateError()
        raise PuestoNotFoundError(puesto_id)

    async def delete(self, puesto_id: int):
        existing_puesto = await self.repository.get_by_id(puesto_id)
        if existing_puesto:
            try:
                return await self.repository.delete(puesto_id)
            except Exception as e:
                raise PuestoDeletionError()
        raise PuestoNotFoundError(puesto_id)