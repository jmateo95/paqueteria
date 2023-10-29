from app.enums.enums import ConceptoGasto, TipoGasto
from app.repositories.gasto.gasto_repository import GastoRepository
from app.models.gasto.gasto_model import GastoCreate
from app.repositories.sucursal.salida_repository import SalidaRepository
from app.repositories.sucursal.sucursal_repository import SucursalRepository
from app.repositories.sucursal.tarifario_repository import TarifarioRepository
from app.models.sucursal.tarifario_model import TarifarioCreate, TarifarioUpdate, Tarifario
from app.errors.common_errors import EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError
from datetime import datetime


class TarifarioService:
    def __init__(self):
        self.repository = TarifarioRepository()
        self.gasto_repository = GastoRepository()
        self.sucursal_repository = SucursalRepository()
        self.salida_repository = SalidaRepository()

    async def get_all(self):
        tarifarios = await self.repository.get_all()
        return [] if not tarifarios else tarifarios

    async def get_by_id(self, tarifario_id: int):
        tarifario = await self.repository.get_by_id(tarifario_id)
        if not tarifario:
            raise EntityNotFoundError("Tarifario", tarifario_id)
        return tarifario

    async def create(self, tarifario: TarifarioCreate):
        try:
            #Eliminar y Crear Gastos de plantilla
            await self.gasto_repository.delete_by_concepto_rango(concepto_gasto_id=ConceptoGasto.PLANILLA)
            planillas= await self.sucursal_repository.get_total_salary_by_sucursal()
            for planilla in planillas:
                gasto=GastoCreate(
                    sucursal_id=planilla['id'],
                    tipo_gasto_id=TipoGasto.FIJO,
                    concepto_gasto_id=ConceptoGasto.PLANILLA,
                    detalles="Gastos de Planilla",
                    monto=planilla['total_salarios'],
                    fecha = datetime.now()
                )
                await self.gasto_repository.create(gasto=gasto.dict())
            
            #Obtener los tales de este mes
            costos_totales= await self.repository.calculate_total_gasto()
            libras_totales= await self.repository.calculate_total_libras()
            
            #Eliminar y Crear Tarifario
            await self.repository.delete_by_fecha()
            tarifario=Tarifario(
                fecha=datetime.now(),
                ganancia_envio=tarifario.ganancia_envio,
                costo_lb=round((costos_totales/libras_totales), 4)
            )
            return await self.repository.create(tarifario.dict())
        except Exception as e:
            print(e)
            raise EntityCreationError("Tarifario")
        
    async def update(self, tarifario_id: int, tarifario: TarifarioUpdate):
        existing_tarifario = await self.repository.get_by_id(tarifario_id)
        if existing_tarifario:
            tarifario_update = {key: value for key, value in tarifario.dict().items() if value is not None}
            if tarifario_update:
                try:
                    return await self.repository.update(tarifario_id, tarifario_update)
                except Exception as e:
                    raise EntityUpdateError("Tarifario")
        raise EntityNotFoundError("Tarifario", tarifario_id)

    async def delete(self, tarifario_id: int):
        existing_tarifario = await self.repository.get_by_id(tarifario_id)
        if existing_tarifario:
            try:
                return await self.repository.delete(tarifario_id)
            except Exception as e:
                raise EntityDeletionError("Tarifario")
        raise EntityNotFoundError("Tarifario", tarifario_id)
