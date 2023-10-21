from fastapi import HTTPException

class PuestosNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="No se encontraron puestos.")

class PuestoNotFoundError(HTTPException):
    def __init__(self, puesto_id: int):
        detail = f"Puesto con id {puesto_id} no encontrado"
        super().__init__(status_code=404, detail=detail)

class PuestoCreationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al crear el puesto.")

class PuestoUpdateError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al actualizar el puesto.")

class PuestoDeletionError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al eliminar el puesto.")