from app.repositories.ciudad_repository import CiudadRepository
from app.models.ciudad_model import CiudadCreate, CiudadUpdate

class CiudadService:

    @staticmethod
    async def get_by_id(ciudad_id: int):
        return await CiudadRepository.get_by_id(ciudad_id)


    @staticmethod
    async def get_all():
        return await CiudadRepository.get_all()


    @staticmethod
    async def create(ciudad: CiudadCreate):
        return await CiudadRepository.create(ciudad.dict())


    @staticmethod
    async def update(ciudad_id: int, ciudad: CiudadUpdate):
        return await CiudadRepository.update(ciudad_id, ciudad.dict())


    @staticmethod
    async def delete(ciudad_id: int):
        return await CiudadRepository.delete(ciudad_id)