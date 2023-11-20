from datetime import datetime
from app.enums.enums import EstadoPaquete, EstadoTracking, TipoSalida
from app.models.paquete.tracking_model import TrackingCreate, TrackingUpdate
from app.models.sucursal.salida_model import SalidaUpdate
from app.repositories.paquete.paquete_repository import PaqueteRepository
from app.repositories.paquete.tracking_repository import TrackingRepository
from app.repositories.sucursal.salida_repository import SalidaRepository
from app.repositories.sucursal.tarifario_repository import TarifarioRepository
from app.models.paquete.paquete_model import PaqueteCotizar, PaqueteCreate, PaqueteUpdate, Paquete
from app.errors.common_errors import EntityNotFoundError, EntityCreationError, EntityUpdateError, EntityDeletionError, CustomValidationError
from app.helpers.functions import get_salidas, get_cotizar, get_costo
import uuid

class PaqueteService:
    def __init__(self):
        self.repository = PaqueteRepository()
        self.salida_repository = SalidaRepository()
        self.tarifario_repository = TarifarioRepository()
        self.tracking_repository = TrackingRepository()

    async def get_paquetes_by_filters(self, salida_id:int=None, tipo_tracking_id:int=None, estado_paquete_id:int=None, sucursal_id:int=None):
        paquetes = await self.repository.get_paquetes_by_filters(salida_id, tipo_tracking_id, estado_paquete_id, sucursal_id)
        return [] if not paquetes else paquetes

    async def get_by_id(self, paquete_id: int):
        paquete = await self.repository.get_by_id(paquete_id)
        if not paquete:
            raise EntityNotFoundError("Paquete", paquete_id)
        return paquete
    
    async def get_by_no_guia(self, no_guia: str):
        paquete = await self.repository.get_by_no_guia(no_guia=no_guia)
        if not paquete:
            raise EntityNotFoundError("Paquete", no_guia)
        return paquete
    
    async def create(self, paquete: PaqueteCreate):
        try:
            salidas_filtradas, new_paquete_created = await self.create_package(paquete)
            #Crear el tracking y aumentar la capacidad reservada
            await self.update_salidas_and_create_trackings(paquete, salidas_filtradas, new_paquete_created)
            #Revisar si el de la salida puede actualiziarse
            await self.salida_repository.update_status_salida_and_tracking(salidas_filtradas[0]['id'])
            return new_paquete_created
        except Exception as e:
            print(e)
            raise EntityCreationError("Paquete")
        
    async def create_package(self, paquete: PaqueteCreate):
        salidas = await self.salida_repository.get_salidas_by_capacity(TipoSalida.PROYECCION, paquete.peso)
        salidas_filtradas = get_salidas(salidas, paquete.sucursal_origen_id, paquete.sucursal_destino_id, paquete.campo)
        tarifario = await self.tarifario_repository.get_tarifarios_by_filters()
        if len(tarifario) < 1 or len(salidas_filtradas) < 1:
            raise CustomValidationError("No existe una ruta actualmente para este paquete")
        # Crear el paquete
        costo = get_costo(salidas_filtradas, tarifario[0], paquete.peso, paquete.campo)
        new_paquete = Paquete(
            estado_paquete_id=EstadoPaquete.RECEPCION,
            no_guia=str(uuid.uuid4().int)[0:15],
            descripcion=paquete.descripcion,
            peso=paquete.peso,
            volumen=paquete.volumen,
            remitente=paquete.remitente,
            destinatario=paquete.destinatario,
            costo=costo,
        )
        new_paquete_created = await self.repository.create(new_paquete.dict())
        return salidas_filtradas, new_paquete_created
        
    async def update(self, paquete_id: int, paquete: PaqueteUpdate):
        existing_paquete = await self.repository.get_by_id(paquete_id)
        if existing_paquete:
            paquete_update = {key: value for key, value in paquete.dict().items() if value is not None}
            if paquete_update:
                try:
                    return await self.repository.update(paquete_id, paquete_update)
                except Exception as e:
                    raise EntityUpdateError("Paquete")
        raise EntityNotFoundError("Paquete", paquete_id)

    async def delete(self, paquete_id: int):
        existing_paquete = await self.repository.get_by_id(paquete_id)
        if existing_paquete:
            try:
                return await self.repository.delete(paquete_id)
            except Exception as e:
                raise EntityDeletionError("Paquete")
        raise EntityNotFoundError("Paquete", paquete_id)

    async def cotizar(self, paquete: PaqueteCotizar):
        try:
            salidas = await self.salida_repository.get_salidas_by_capacity(TipoSalida.PROYECCION, paquete.peso)
            por_distancia = get_salidas(salidas, paquete.sucursal_origen_id, paquete.sucursal_destino_id, 'distancia')
            por_costo = get_salidas(salidas, paquete.sucursal_origen_id, paquete.sucursal_destino_id, 'costo_lb')
            tarifario = await self.tarifario_repository.get_tarifarios_by_filters()
            if len(tarifario)<1 or (len(por_distancia)+len(por_costo)<1):
                raise CustomValidationError("No existe una ruta actualmente para este paquete.")
            costo= get_cotizar(por_distancia, por_costo, tarifario[0], paquete.peso)
            return costo
        except Exception as e:
            print(e)
            raise CustomValidationError("No existe una ruta actualmente para este paquete.")
        
    async def update_salidas_and_create_trackings(self, paquete, salidas_filtradas, new_paquete_created):
        contador = 0
        for salida in salidas_filtradas:
            contador += 1
            # Actualizo la salida
            nueva_capacidad_reservada = salida['capacidad_reservada'] + paquete.peso
            await self.salida_repository.update(salida['id'], {"capacidad_reservada": nueva_capacidad_reservada})
            # Crea el tracking
            tracking_create = TrackingCreate(
                paquete_id=new_paquete_created.id,
                sucursal_id=salida['sucursal_origen_id'],
                estado_tracking_id=EstadoTracking.EN_BODEGA if contador == 1 else EstadoTracking.EN_ESPERA,
                salida_id=salida['id'],
                actualizacion=datetime.now(),
                comentario="Se recibió el paquete" if contador == 1 else "En Espera",
            )
            await self.tracking_repository.create(tracking_create.dict())

    async def cargar(self, paquete_id: int):
        # Obtener el tracking del paquete con estado 3
        tracking = await self.tracking_repository.get_by_paquete_and_status(paquete_id, EstadoTracking.CARGANDO)
        if not tracking:
            raise CustomValidationError("No existe el paquete.")
        try:
            # Actualizar el estado del tracking a 4
            await self.tracking_repository.update(tracking.id, {"estado_tracking_id":EstadoTracking.CARGADO})

            # Obtener todos los trackings para la salida del paquete
            trackings = await self.tracking_repository.get_tracking_by_filters(salida_id=tracking.salida_id)

            if all(tracking.estado_tracking_id == EstadoTracking.CARGADO for tracking in trackings):
                # Cambiar el estado de la salida a 4
                await self.salida_repository.update(tracking.salida_id, {"tipo_salida_id":TipoSalida.CARGADO})
        except Exception as e:
            print(e)
            raise CustomValidationError("Error al cargar el paquete.")
        

    async def numero_paquetes(self, fecha: datetime=None):
        paquetes = await self.repository.numero_paquetes(fecha=fecha)
        return {"no_paquetes":len(paquetes)}
        
    async def peso_promedio(self, fecha: datetime=None):
        peso_prom = await self.repository.peso_promedio(fecha=fecha)
        return round( 0 if peso_prom[0]['peso']==None else peso_prom[0]['peso'] , 2)
    
    async def costo_promedio(self, fecha: datetime=None):
        costo_prom = await self.repository.costo_promedio(fecha=fecha)
        return round( 0 if costo_prom[0]['costo']==None else costo_prom[0]['costo'] , 2)

    async def paquetes_estado(self, fecha: datetime=None):
        paquetes = await self.repository.paquetes_estado(fecha=fecha)
        return [] if not paquetes else paquetes
    

    async def pdf(self, no_guia: str):
        paquete = await self.repository.pdf(no_guia=no_guia)
        if not paquete:
            raise EntityNotFoundError("Paquete", no_guia)
        return paquete