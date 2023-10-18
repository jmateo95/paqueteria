from schema import ResponseSchema
from app.services.ciudad_service import CiudadService
from app.models.ciudad_model import CiudadCreate, CiudadUpdate

class CiudadController:
    def __init__(self):
        self.service = CiudadService()

    async def get_all(self):
        result = await self.service.get_all()
        return ResponseSchema(detail="", result=result)


    async def get_by_id(self, ciudad_id: int):
        result = await self.service.get_by_id(ciudad_id)
        return ResponseSchema(detail="", result=result)


    async def create(self, ciudad: CiudadCreate):
        await self.service.create(ciudad)
        return ResponseSchema(detail="")


    async def delete(self, ciudad_id: int):
        await self.service.delete(ciudad_id)
        return ResponseSchema(detail="")


    async def update(self, ciudad_id: int, ciudad: CiudadUpdate):
        await self.service.update(ciudad_id, ciudad)
        return ResponseSchema(detail="")


ciudad_controller = CiudadController()
