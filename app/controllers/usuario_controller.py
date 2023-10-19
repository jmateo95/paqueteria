from schema import ResponseSchema
from app.services.usuario_servicey import UsuarioService
from app.models.usuario_model import UsuarioCreate, UsuarioUpdate, UsuarioLogin

class UsuarioController:
    def __init__(self):
        self.service = UsuarioService()

    async def get_all(self):
        result = await self.service.get_all()
        return ResponseSchema(detail="", result=result)
    

    async def get_by_id(self, usuario_id: int):
        result = await self.service.get_by_id(usuario_id)
        return ResponseSchema(detail="", result=result)
    

    async def create(self, usuario: UsuarioCreate):
        await self.service.create(usuario)
        return ResponseSchema(detail="Usuario creado con éxito")


    async def update(self, usuario_id: int, usuario: UsuarioUpdate):
        await self.service.update(usuario_id, usuario)
        return ResponseSchema(detail="")


    async def delete(self, usuario_id: int):
        await self.service.delete(usuario_id)
        return ResponseSchema(detail="")


    async def login(self, credentials: UsuarioLogin):
        usuario = await self.service.login(credentials)
        # Puedes generar un token de autenticación y devolverlo en la respuesta
        return ResponseSchema(detail="Inicio de sesión exitoso", result=usuario)


usuario_controller = UsuarioController()
