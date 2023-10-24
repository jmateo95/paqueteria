from app.models.sucursal.ciudad_model import CiudadCreate, CiudadUpdate
from config.Connection import prisma_connection

class CiudadRepository:

    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.ciudad.find_many()

    async def get_by_id(self, ciudad_id: int):
        return await self.connection.prisma.ciudad.find_first(where={"id": ciudad_id})

    async def create(self, ciudad: CiudadCreate):
        return await self.connection.prisma.ciudad.create(ciudad)

    async def update(self, ciudad_id: int, ciudad: CiudadUpdate):
        return await self.connection.prisma.ciudad.update(where={"id": ciudad_id}, data=ciudad)

    async def delete(self, ciudad_id: int):
        return await self.connection.prisma.ciudad.delete(where={"id": ciudad_id})