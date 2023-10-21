# common_errors.py
from fastapi import HTTPException

class EntitiesNotFoundError(HTTPException):
    def __init__(self, entity_name: str):
        detail = f"No se encontraron {entity_name}"
        super().__init__(status_code=404, detail=detail)

class EntityNotFoundError(HTTPException):
    def __init__(self, entity_name: str, entity_id: int):
        detail = f"{entity_name} con ID {entity_id} no encontrado"
        super().__init__(status_code=404, detail=detail)

class EntityCreationError(HTTPException):
    def __init__(self, entity_name: str):
        detail = f"Error al crear {entity_name}"
        super().__init__(status_code=400, detail=detail)

class EntityUpdateError(HTTPException):
    def __init__(self, entity_name: str):
        detail = f"Error al actualizar {entity_name}"
        super().__init__(status_code=400, detail=detail)

class EntityDeletionError(HTTPException):
    def __init__(self, entity_name: str):
        detail = f"Error al eliminar {entity_name}"
        super().__init__(status_code=400, detail=detail)

class UsuarioLoginError(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Inicio de sesión fallido. Credenciales incorrectas")
