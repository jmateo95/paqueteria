from app.enums.enums import ConceptoGasto, EstadoPaquete, EstadoTracking, TipoGasto, TipoSalida
from app.models.gasto.gasto_model import GastoCreate
from app.models.paquete.paquete_model import PaqueteUpdate
from app.models.paquete.tracking_model import TrackingUpdate
from app.models.sucursal.ingreso_model import IngresoCreate
from app.repositories.gasto.gasto_repository import GastoRepository
from app.repositories.paquete.paquete_repository import PaqueteRepository
from app.repositories.paquete.tracking_repository import TrackingRepository
from app.repositories.sucursal.ingreso_repository import IngresoRepository
from app.repositories.sucursal.salida_repository import SalidaRepository
from app.models.sucursal.salida_model import SalidaCreate, SalidaUpdate, Salida
from app.errors.common_errors import EntityNotFoundError, EntityCreationError, EntityUpdateError,  EntityDeletionError
from app.repositories.sucursal.segmento_repository import SegmentoRepository
from app.repositories.sucursal.tarifario_repository import TarifarioRepository
from app.repositories.sucursal.vehiculo_repository import VehiculoRepository
from datetime import datetime
import math

class SalidaService:
    def __init__(self):
        self.repository = SalidaRepository()
        self.vehiculo_repository  = VehiculoRepository()
        self.segmento_repository  = SegmentoRepository()
        self.tracking_repository  = TrackingRepository()
        self.paquete_repository   = PaqueteRepository()
        self.tarifario_repository = TarifarioRepository()
        self.ingreso_repository   = IngresoRepository()
        self.gasto_repository     = GastoRepository()

    async def get_salidas_by_filters(self, sucursal_id:int =None, tipo_salida_id:int=None, fecha:datetime=None, test:bool=False):
        salidas = await self.repository.get_salidas_by_filters(sucursal_id=sucursal_id, tipo_salida_id=tipo_salida_id, fecha=fecha, test=test)
        return [] if not salidas else salidas

    async def get_by_id(self, salida_id: int):
        salida = await self.repository.get_by_id(salida_id)
        if not salida:
            raise EntityNotFoundError("Salida", salida_id)
        return salida

    async def create(self, salida: SalidaCreate):
        try:
            #Obtener los valores
            vehiculo = await self.vehiculo_repository.get_by_id(salida.vehiculo_id)
            segmento = await self.segmento_repository.get_by_id(salida.segmento_id)
            segmento_2=await self.segmento_repository.get_by_sucursales(sucursal_origen_id=segmento.sucursal_destino_id, sucursal_destino_id=segmento.sucursal_origen_id)
            if not vehiculo or not segmento or not segmento_2:
                raise EntityCreationError("Salida")
            #Crear Objeto Salida
            salida_1 = Salida(
                tipo_salida_id      = TipoSalida.PROYECCION,
                vehiculo_id         = vehiculo.id,
                segmento_id         = segmento.id,
                fecha_programada    = datetime.now(),
                comentario          = '',
                costo_lb            = round(math.ceil((vehiculo.costo_km * segmento.distancia / vehiculo.capacidad_lb) * 100) / 100, 2),
                capacidad_lb        = vehiculo.capacidad_lb,
                capacidad_reservada = 0,
                capacidad_ocupada   = 0,
                test                = salida.test
            )

            salida_2 = Salida(
                **salida_1.dict(exclude={"segmento_id"}),
                segmento_id = segmento_2.id,
            )
            
            #Guardar Salidias
            await self.repository.create(salida_1.dict())
            return await self.repository.create(salida_2.dict())
        except Exception as e:
            raise EntityCreationError("Salida")
        
    async def update(self, salida_id: int, salida: SalidaUpdate):
        existing_salida = await self.repository.get_by_id(salida_id)
        if existing_salida:
            salida_update = {key: value for key, value in salida.dict().items() if value is not None}
            if salida_update:
                try:
                    return await self.repository.update(salida_id, salida_update)
                except Exception as e:
                    raise EntityUpdateError("Salida")
        raise EntityNotFoundError("Salida", salida_id)

    async def delete(self, salida_id: int):
        existing_salida = await self.repository.get_by_id(salida_id)
        if existing_salida:
            try:
                return await self.repository.delete(salida_id)
            except Exception as e:
                raise EntityDeletionError("Salida")
        raise EntityNotFoundError("Salida", salida_id)
    
    async def dar_salida(self, salida_id: int):
        salida=await self.get_by_id(salida_id=salida_id)
        if(salida.tipo_salida_id==TipoSalida.CARGADO):
            #Actualizar Salida
            await self.repository.update(salida_id, {"tipo_salida_id":TipoSalida.EN_RUTA, "fecha_salida":datetime.now()})
            
            #Actualizar Tracking
            await self.tracking_repository.update_trackings_salida(salida_id, EstadoTracking.EN_RUTA)
            
            #Insertar el gasto
            total = round(math.ceil((salida.costo_lb*salida.capacidad_lb) * 100) / 100, 2)
            segmento = await self.segmento_repository.get_by_id(segmento_id=salida.segmento_id)
            await self.gasto_repository.create(GastoCreate(sucursal_id=segmento.sucursal_origen_id, tipo_gasto_id=TipoGasto.TRANSPORTE, concepto_gasto_id=ConceptoGasto.GASOLINA, detalles=f"Gasto por salida {salida.id}", monto=total, fecha=salida.fecha_programada, test=False).dict())
            #Actualizar Paquete 
            paquetes = await self.paquete_repository.get_paquetes_by_filters(salida_id=salida_id)
            for paquete in paquetes:
                trackings=await self.tracking_repository.get_tracking_by_filters(paquete_id=paquete['id'])
                if all(tracking.estado_tracking_id >= EstadoTracking.EN_RUTA for tracking in trackings):
                    # Cambiar el estado del paquete
                    await self.paquete_repository.update(paquete['id'], {"estado_paquete_id":EstadoPaquete.RUTA_FINAL})
                else:
                    await self.paquete_repository.update(paquete['id'], {"estado_paquete_id":EstadoPaquete.TRANSITO})
            return
        raise EntityNotFoundError("Salida", salida_id)


    async def ingresar(self, salida_id: int):
        salida= await self.get_by_id(salida_id=salida_id)
        if(salida.tipo_salida_id==TipoSalida.EN_RUTA):
            #Actualizar Salida
            await self.repository.update(salida_id, {"tipo_salida_id":TipoSalida.FIN, "fecha_llegada":datetime.now()})
            #Inserta el Ingreso
            tarifarios = await self.tarifario_repository.get_tarifarios_by_filters(fecha = salida.fecha_programada)
            segmento = await self.segmento_repository.get_by_id(segmento_id=salida.segmento_id)
            if len(tarifarios) > 0:
                tarifario = tarifarios[0]
                total = round(math.ceil(((salida.capacidad_lb * (salida.costo_lb+tarifario.costo_lb)) * (1 + (tarifario.ganancia_envio / 100))) * 100) / 100, 2)
                await self.ingreso_repository.create(IngresoCreate(sucursal_id=segmento.sucursal_origen_id, detalles=f"Ingreso por salida: {salida.id}", monto=total, fecha=salida.fecha_programada).dict())
            
            #Actualizar Tracking Actual
            await self.tracking_repository.update_trackings_salida(salida_id, EstadoTracking.COMPLETADO)
            
            #Actualizar los paquetes en rutas finales
            paquetes = await self.paquete_repository.get_paquetes_by_filters(salida_id=salida_id)
            for paquete in paquetes:
                if(paquete['estado_paquete_id']==EstadoPaquete.RUTA_FINAL):
                    await self.paquete_repository.update(paquete['id'], {"estado_paquete_id":EstadoPaquete.POR_ENTREGAR})

                    #Si no esta en una ruta final actualizar el siguiente tracking
                else:
                    #Obtengo el tracking actual
                    tracking = await self.tracking_repository.get_by_paquete_and_status(paquete_id=paquete['id'], estado_tracking_id=EstadoTracking.COMPLETADO)
                    if tracking is not None: 
                        #obtengo el siguiente tracking
                        tracking_next = await self.tracking_repository.get_by_id(tracking_id=(tracking.id+1))
                        if tracking_next is not None: 
                            if(tracking_next.paquete_id==paquete['id']):
                                #Pongo en bodega el tracking siguiene
                                await self.tracking_repository.update(tracking_next.id, {"estado_tracking_id":EstadoTracking.EN_BODEGA})
                                #Compruebo si la salida del tracking siguiente ya se puede poner en lista para cargar
                                await self.repository.update_status_salida_and_tracking(tracking_next.salida_id)
            return
        
        raise EntityNotFoundError("Salida", salida_id)