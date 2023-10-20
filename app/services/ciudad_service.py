from app.repositories.ciudad_repository import CiudadRepository
from app.models.ciudad_model import CiudadCreate, CiudadUpdate
from app.errors.ciudad_errors import CiudadNotFoundError, CiudadesNotFoundError, CiudadCreationError, CiudadUpdateError, CiudadDeletionError


class CiudadService:

    def __init__(self):
        self.repository = CiudadRepository()


    async def get_all(self):
        ciudades = await self.repository.get_all()
        if not ciudades:
            raise CiudadesNotFoundError()
        return ciudades


    async def get_by_id(self, ciudad_id: int):
        ciudad = await self.repository.get_by_id(ciudad_id)
        if not ciudad:
            raise CiudadNotFoundError(ciudad_id)
        return ciudad


    async def create(self, ciudad: CiudadCreate):
        try:
            return await self.repository.create(ciudad.dict())
        except Exception as e:
            raise CiudadCreationError()
        

    async def update(self, ciudad_id: int, ciudad: CiudadUpdate):
        existing_ciudad = await self.repository.get_by_id(ciudad_id)
        if existing_ciudad:
            ciudad_update = {key: value for key, value in ciudad.dict().items() if value is not None}
            if ciudad_update:
                try:
                    return await self.repository.update(ciudad_id, ciudad_update)
                except Exception as e:
                    raise CiudadUpdateError()
        raise CiudadNotFoundError(ciudad_id)


    async def delete(self, ciudad_id: int):
        existing_ciudad = await self.repository.get_by_id(ciudad_id)
        if existing_ciudad:
            try:
                return await self.repository.delete(ciudad_id)
            except Exception as e:
                raise CiudadDeletionError()
        raise CiudadNotFoundError(ciudad_id)