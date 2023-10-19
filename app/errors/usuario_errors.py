from fastapi import HTTPException

class UsuariosNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="No se encontraron usuarios.")

class UsuarioNotFoundError(HTTPException):
    def __init__(self, usuario_id: int)->None:
        detail = f"Usuario con ID {usuario_id} no encontrado"
        super().__init__(status_code=404, detail=detail)

class UsuarioCreationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al crear el usuario")

class UsuarioUpdateError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al actualizar el usuario")

class UsuarioDeactivationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al desactivar el usuario")

class UsuarioLoginError(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Inicio de sesión fallido. Credenciales incorrectas")