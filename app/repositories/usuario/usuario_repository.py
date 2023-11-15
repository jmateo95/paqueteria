from app.models.usuario.usuario_model import UsuarioCreate, UsuarioUpdate
from config.Connection import prisma_connection

class UsuarioRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_users_by_filters(self, sucursal_id=None, test:bool=False):
        where_conditions = {}        
        if sucursal_id is not None:
            where_conditions["sucursal_id"] = sucursal_id
        if not test:
            where_conditions["test"] = test
        return await self.connection.prisma.usuario.find_many(where=where_conditions, include={"rol":True,"sucursal":True,"puesto":True})

    async def get_by_id(self, usuario_id: int):
        return await self.connection.prisma.usuario.find_first(where={"id": usuario_id})
    
    async def create(self, usuario: UsuarioCreate):
        return await self.connection.prisma.usuario.create(usuario)
    
    async def update(self, usuario_id: int, usuario: UsuarioUpdate):
        return await self.connection.prisma.usuario.update(where={"id": usuario_id}, data=usuario)

    async def delete(self, usuario_id: int):
        return await self.connection.prisma.usuario.delete(where={"id": usuario_id})
    
    async def get_by_email(self, email: str):
        return await self.connection.prisma.usuario.find_first(where={"email": email}, include={"rol": True})