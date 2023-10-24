from app.models.usuario.puesto_model import PuestoCreate, PuestoUpdate
from config.Connection import prisma_connection

class PuestoRepository:

    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.puesto.find_many()

    async def get_by_id(self, puesto_id: int):
        return await self.connection.prisma.puesto.find_first(where={"id": puesto_id})

    async def create(self, puesto: PuestoCreate):
        return await self.connection.prisma.puesto.create(puesto)

    async def update(self, puesto_id: int, puesto: PuestoUpdate):
        return await self.connection.prisma.puesto.update(where={"id": puesto_id}, data=puesto)

    async def delete(self, puesto_id: int):
        return await self.connection.prisma.puesto.delete(where={"id": puesto_id})
