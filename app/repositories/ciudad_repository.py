from app.models.ciudad_model import CiudadCreate, CiudadUpdate
from config.Connection import prisma_connection

class CiudadRepository:

    @staticmethod
    async def get_all():
        return await prisma_connection.prisma.ciudad.find_many()
    

    @staticmethod
    async def get_by_id(ciudad_id: int):
        return await prisma_connection.prisma.ciudad.find_first(where={"id": ciudad_id})


    @staticmethod
    async def create(ciudad: CiudadCreate):
        return await prisma_connection.prisma.ciudad.create(ciudad)
    

    @staticmethod
    async def update(ciudad_id: int, ciudad: CiudadUpdate):
        return await prisma_connection.prisma.ciudad.update(where={"id": ciudad_id}, data=ciudad)


    @staticmethod
    async def delete(ciudad_id: int):
        return await prisma_connection.prisma.ciudad.delete(where={"id": ciudad_id})