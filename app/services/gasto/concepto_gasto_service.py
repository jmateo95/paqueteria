from app.repositories.gasto.concepto_gasto_repository import ConceptoGastoRepository
from app.models.gasto.concepto_gasto_model import ConceptoGastoCreate, ConceptoGastoUpdate
from app.errors.common_errors import EntitiesNotFoundError, EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class ConceptoGastoService:
    def __init__(self):
        self.repository = ConceptoGastoRepository()

    async def get_all(self):
        concepto_gastos = await self.repository.get_all()
        if not concepto_gastos:
            return []
        return concepto_gastos

    async def get_by_id(self, concepto_gasto_id: int):
        concepto_gasto = await self.repository.get_by_id(concepto_gasto_id)
        if not concepto_gasto:
            raise EntityNotFoundError("ConceptoGasto", concepto_gasto_id)
        return concepto_gasto

    async def create(self, concepto_gasto: ConceptoGastoCreate):
        try:
            return await self.repository.create(concepto_gasto.dict())
        except Exception as e:
            print(e)
            raise EntityCreationError("ConceptoGasto")
        
    async def update(self, concepto_gasto_id: int, concepto_gasto: ConceptoGastoUpdate):
        existing_concepto_gasto = await self.repository.get_by_id(concepto_gasto_id)
        if existing_concepto_gasto:
            concepto_gasto_update = {key: value for key, value in concepto_gasto.dict().items() if value is not None}
            if concepto_gasto_update:
                try:
                    return await self.repository.update(concepto_gasto_id, concepto_gasto_update)
                except Exception as e:
                    raise EntityUpdateError("ConceptoGasto")
        raise EntityNotFoundError("ConceptoGasto", concepto_gasto_id)

    async def delete(self, concepto_gasto_id: int):
        existing_concepto_gasto = await self.repository.get_by_id(concepto_gasto_id)
        if existing_concepto_gasto:
            try:
                return await self.repository.delete(concepto_gasto_id)
            except Exception as e:
                raise EntityDeletionError("ConceptoGasto")
        raise EntityNotFoundError("ConceptoGasto", concepto_gasto_id)
