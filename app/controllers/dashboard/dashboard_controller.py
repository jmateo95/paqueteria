from app.services.paquete.paquete_service import PaqueteService
from app.services.sucursal.sucursal_service import SucursalService
from app.services.sucursal.vehiculo_service import VehiculoService
from app.services.usuario.usuario_service import UsuarioService
from schema import ResponseSchema
from config.auth import get_current_user_with_roles
from fastapi import Depends, Query
from datetime import datetime


class DashboardController:
    def __init__(self):
        self.paquete_service  = PaqueteService()
        self.vehiculo_service = VehiculoService()
        self.sucursal_service = SucursalService()
        self.usuario_service  = UsuarioService()

    async def numero_paquetes(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.paquete_service.numero_paquetes(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def peso_promedio(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.paquete_service.peso_promedio(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def costo_promedio(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.paquete_service.costo_promedio(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def vehiculos_tot(self, test:bool=False, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.vehiculo_service.vehiculos_tot(test=test)
        return ResponseSchema(detail="", result=roles)
    
    async def sucursales_tot(self, test:bool=False, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.sucursal_service.sucursales_tot(test=test)
        return ResponseSchema(detail="", result=roles)
    
    async def empleados_tot(self, test:bool=False, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.usuario_service.usuarios_tot(test=test)
        return ResponseSchema(detail="", result=roles)
    
    async def paquetes_estado(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.paquete_service.paquetes_estado(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def top_sucursales(self, fecha: datetime = Query(None)):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.sucursal_service.top_sucursales(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
