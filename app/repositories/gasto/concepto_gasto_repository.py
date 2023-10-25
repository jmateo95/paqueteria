from app.models.gasto.concepto_gasto_model import ConceptoGastoCreate, ConceptoGastoUpdate
from config.Connection import prisma_connection

class ConceptoGastoRepository:
    def __init__(self):
        self.connection = prisma_connection

    async def get_all(self):
        return await self.connection.prisma.conceptogasto.find_many()

    async def get_by_id(self, concepto_gasto_id: int):
        return await self.connection.prisma.conceptogasto.find_first(where={"id": concepto_gasto_id})
    
    async def create(self, concepto_gasto: ConceptoGastoCreate):
        return await self.connection.prisma.conceptogasto.create(concepto_gasto)
    
    async def update(self, concepto_gasto_id: int, concepto_gasto: ConceptoGastoUpdate):
        return await self.connection.prisma.conceptogasto.update(where={"id": concepto_gasto_id}, data=concepto_gasto)

    async def delete(self, concepto_gasto_id: int):
        return await self.connection.prisma.conceptogasto.delete(where={"id": concepto_gasto_id})
