from fastapi import HTTPException

class CiudadesNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="No se encontraron ciudades.")


class CiudadNotFoundError(HTTPException):
    def __init__(self, ciudad_id: int)->None:
        detail = f"Ciudad con id {ciudad_id} no encontrada"
        super().__init__(status_code=404, detail=detail)


class CiudadCreationError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al crear la ciudad.")


class CiudadUpdateError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al actualizar la ciudad.")


class CiudadDeletionError(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Error al eliminar la ciudad.")