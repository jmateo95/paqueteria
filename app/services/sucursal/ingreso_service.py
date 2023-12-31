from datetime import datetime
from app.repositories.sucursal.ingreso_repository import IngresoRepository
from app.models.sucursal.ingreso_model import IngresoCreate, IngresoUpdate
from app.errors.common_errors import EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError

class IngresoService:
    def __init__(self):
        self.repository = IngresoRepository()

    async def get_ingresos_by_filters(self, sucursal_id=None, fecha=None):
        ingresos = await self.repository.get_ingresos_by_filters(sucursal_id, fecha)
        return [] if not ingresos else ingresos
    
    async def get_ingresos_pronosticados_by_filters(self, sucursal_id=None, fecha=None, test:bool=False):
        ingresos = await self.repository.get_ingresos_pronosticados_by_filters(sucursal_id=sucursal_id, fecha=fecha, test=test)
        return [] if not ingresos else ingresos

    async def get_by_id(self, ingreso_id: int):
        ingreso = await self.repository.get_by_id(ingreso_id)
        if not ingreso:
            raise EntityNotFoundError("Ingreso", ingreso_id)
        return ingreso

    async def create(self, ingreso: IngresoCreate):
        try:
            return await self.repository.create(ingreso.dict())
        except Exception as e:
            raise EntityCreationError("Ingreso")
        
    async def update(self, ingreso_id: int, ingreso: IngresoUpdate):
        existing_ingreso = await self.repository.get_by_id(ingreso_id)
        if existing_ingreso:
            ingreso_update = {key: value for key, value in ingreso.dict().items() if value is not None}
            if ingreso_update:
                try:
                    return await self.repository.update(ingreso_id, ingreso_update)
                except Exception as e:
                    raise EntityUpdateError("Ingreso")
        raise EntityNotFoundError("Ingreso", ingreso_id)

    async def delete(self, ingreso_id: int):
        existing_ingreso = await self.repository.get_by_id(ingreso_id)
        if existing_ingreso:
            try:
                return await self.repository.delete(ingreso_id)
            except Exception as e:
                raise EntityDeletionError("Ingreso")
        raise EntityNotFoundError("Ingreso", ingreso_id)


    async def ingreso(self, fecha: datetime=None):
        ingresos = await self.repository.ingreso(fecha=fecha)
        return {"ingresos":(round( ingresos, 2))}
    
    async def ingreso_pron(self, fecha: datetime=None, test:bool=False):
        ingresos = await self.repository.ingreso_pron(fecha=fecha, test=test)
        return {"ingresos":(round( ingresos, 2))}
    
    async def ingreso_real_vs_pron(self, fecha: datetime=None, test:bool=False):
        real, pronosticado = await self.repository.ingreso_real_vs_pron(fecha=fecha, test=test)
        return [{"real":(round( real, 2))},{"pronosticado":(round( pronosticado, 2))}]
    
    async def ingreso_sucursal(self, fecha: datetime=None):
        ingresos = await self.repository.ingreso_sucursal(fecha=fecha)
        return ingresos