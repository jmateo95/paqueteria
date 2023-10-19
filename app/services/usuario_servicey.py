from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario_model import UsuarioCreate, UsuarioUpdate, UsuarioLogin
from app.errors.usuario_errors import UsuariosNotFoundError, UsuarioLoginError, UsuarioNotFoundError, UsuarioCreationError, UsuarioUpdateError, UsuarioDeactivationError
from app.models.token_model import Token
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()


    async def get_all(self):
        usuarios = await self.repository.get_all()
        if not usuarios:
            raise UsuariosNotFoundError()
        return usuarios
    

    async def get_by_id(self, usuario_id: int):
        usuario = await self.repository.get_by_id(usuario_id)
        if not usuario:
            raise UsuarioNotFoundError(usuario_id)
        return usuario
    

    async def create(self, usuario: UsuarioCreate):
        try:
            hashed_password = pwd_context.hash(usuario.password)
            usuario_data = usuario.dict()
            usuario_data['password'] = hashed_password
            return await self.repository.create(usuario_data)
        except Exception as e:
            print(e)
            raise UsuarioCreationError()
        

    async def update(self, usuario_id: int, usuario: UsuarioUpdate):
        existing_usuario = await self.repository.get_by_id(usuario_id)
        if existing_usuario:
            usuario_update = {key: value for key, value in usuario.dict().items() if value is not None}
            if usuario_update:
                try:
                    return await self.repository.update(usuario_id, usuario_update)
                except Exception as e:
                    raise UsuarioUpdateError()
        raise UsuarioNotFoundError(usuario_id)


    async def delete(self, usuario_id: int):
        existing_usuario = await self.repository.get_by_id(usuario_id)
        if existing_usuario:
            try:
                return await self.repository.delete(usuario_id)
            except Exception as e:
                raise UsuarioDeactivationError()
        raise UsuarioNotFoundError(usuario_id)
        

    async def login(self, credentials: UsuarioLogin):
        email = credentials.email
        password = credentials.password
        usuario = await self.repository.get_by_email(email)
        if not usuario or not pwd_context.verify(password, usuario.password):
            raise UsuarioLoginError()
        return usuario

        # # Genera un token JWT
        # access_token = authenticate.create_access_token(data={"sub": usuario.email})
        # token_data = {"access_token": access_token, "token_type": "bearer"}
        # return Token(**token_data)