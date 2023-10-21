from fastapi import HTTPException

class SucursalesNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="No se encontraron sucursales.")

class SucursalNotFoundError(HTTPException):
    def __init__(self, sucursal_id: int):
        detail = f"Sucursal con id {sucursal_id} no encontrada"
        super().__init__(status_code=404, detail=detail)

class SucursalCreationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al crear la sucursal.")

class SucursalUpdateError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al actualizar la sucursal.")

class SucursalDeletionError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al eliminar la sucursal.")
