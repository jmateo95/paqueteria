from fastapi import HTTPException

class TipoSucursalesNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="No se encontraron tipos de sucursal.")

class TipoSucursalNotFoundError(HTTPException):
    def __init__(self, tipo_sucursal_id: int):
        detail = f"Tipo de sucursal con id {tipo_sucursal_id} no encontrado"
        super().__init__(status_code=404, detail=detail)

class TipoSucursalCreationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al crear el tipo de sucursal.")

class TipoSucursalUpdateError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al actualizar el tipo de sucursal.")

class TipoSucursalDeletionError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al eliminar el tipo de sucursal.")
