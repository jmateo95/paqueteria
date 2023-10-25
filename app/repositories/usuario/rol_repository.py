from app.models.usuario.rol_model import RolCreate, RolUpdate
from config.Connection import prisma_connection

class RolRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.rol.find_many()

    async def get_by_id(self, rol_id: int):
        return await self.connection.prisma.rol.find_first(where={"id": rol_id})
    
    async def create(self, rol: RolCreate):
        return await self.connection.prisma.rol.create(rol)
    
    async def update(self, rol_id: int, rol: RolUpdate):
        return await self.connection.prisma.rol.update(where={"id": rol_id}, data=rol)

    async def delete(self, rol_id: int):
        return await self.connection.prisma.rol.delete(where={"id": rol_id})
