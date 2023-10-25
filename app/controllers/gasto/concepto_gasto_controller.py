from schema import ResponseSchema
from app.services.gasto.concepto_gasto_service import ConceptoGastoService
from app.models.gasto.concepto_gasto_model import ConceptoGastoCreate, ConceptoGastoUpdate
from config.auth import get_current_user_with_roles
from fastapi import Depends

class ConceptoGastoController:
    def __init__(self):
        self.service = ConceptoGastoService()

    async def get_all(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        concepto_gastos = await self.service.get_all()
        return ResponseSchema(detail="", result=concepto_gastos)

    async def get_by_id(self, concepto_gasto_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        concepto_gasto = await self.service.get_by_id(concepto_gasto_id)
        return ResponseSchema(detail="", result=concepto_gasto)

    async def create(self, concepto_gasto: ConceptoGastoCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.create(concepto_gasto)
        return ResponseSchema(detail="Concepto de gasto creado con éxito")

    async def update(self, concepto_gasto_id: int, concepto_gasto: ConceptoGastoUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.update(concepto_gasto_id, concepto_gasto)
        return ResponseSchema(detail="Concepto de gasto actualizado con éxito")

    async def delete(self, concepto_gasto_id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(concepto_gasto_id)
        return ResponseSchema(detail="Concepto de gasto eliminado con éxito")
