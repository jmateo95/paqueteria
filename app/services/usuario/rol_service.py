from app.repositories.usuario.rol_repository import RolRepository
from app.models.usuario.rol_model import RolCreate, RolUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class RolService:
    def __init__(self):
        self.repository = RolRepository()

    async def get_all(self):
        roles = await self.repository.get_all()
        if not roles:
            return []
        return roles

    async def get_by_id(self, rol_id: int):
        rol = await self.repository.get_by_id(rol_id)
        if not rol:
            raise EntityNotFoundError("Rol", rol_id)
        return rol

    async def create(self, rol: RolCreate):
        try:
            return await self.repository.create(rol)
        except Exception as e:
            raise EntityCreationError("Rol")
        
    async def update(self, rol_id: int, rol: RolUpdate):
        existing_rol = await self.repository.get_by_id(rol_id)
        if existing_rol:
            rol_update = {key: value for key, value in rol.dict().items() if value is not None}
            if rol_update:
                try:
                    return await self.repository.update(rol_id, rol_update)
                except Exception as e:
                    raise EntityUpdateError("Rol")
        raise EntityNotFoundError("Rol", rol_id)

    async def delete(self, rol_id: int):
        existing_rol = await self.repository.get_by_id(rol_id)
        if existing_rol:
            try:
                return await self.repository.delete(rol_id)
            except Exception as e:
                raise EntityDeletionError("Rol")
        raise EntityNotFoundError("Rol", rol_id)
