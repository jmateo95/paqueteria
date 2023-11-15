from schema import ResponseSchema
from app.services.paquete.paquete_service import PaqueteService
from app.models.paquete.paquete_model import PaqueteCreate, PaqueteUpdate, PaqueteCotizar
from config.auth import get_current_user_with_roles
from fastapi import Depends, Query
from datetime import datetime

class PaqueteController:
    def __init__(self):
        self.service = PaqueteService()

    async def get_paquetes_by_filters(self, salida_id: int = Query(None), tipo_tracking_id: int = Query(None), estado_paquete_id: int = Query(None), sucursal_id: int = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        paquetes = await self.service.get_paquetes_by_filters(salida_id, tipo_tracking_id, estado_paquete_id, sucursal_id)
        return ResponseSchema(detail="", result=paquetes)

    async def get_by_id(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        paquete = await self.service.get_by_id(id)
        return ResponseSchema(detail="", result=paquete)
    
    async def get_by_no_guia(self, no_guia: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        paquete = await self.service.get_by_no_guia(no_guia=no_guia)
        return ResponseSchema(detail="", result=paquete)

    async def create(self, paquete: PaqueteCreate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        paquete = await self.service.create(paquete)
        return ResponseSchema(detail="Paquete creado con éxito", result=paquete)

    async def update(self, id: int, paquete: PaqueteUpdate, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        paquete = await self.service.update(id, paquete)
        return ResponseSchema(detail="Paquete actualizado con éxito", result=paquete)

    async def delete(self, id: int, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.delete(id)
        return ResponseSchema(detail="Paquete eliminado con éxito")

    async def cotizar(self, paquete: PaqueteCotizar, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        cotizacion=await self.service.cotizar(paquete)
        return ResponseSchema(detail="Paquete cotizado con éxito", result=cotizacion)
    
    async def cargar(self, id: int):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Admin"]))):
        await self.service.cargar(id)
        return ResponseSchema(detail="Se Cargo el paquete con éxito")