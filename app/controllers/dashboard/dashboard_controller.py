from app.services.gasto.gasto_service import GastoService
from app.services.paquete.paquete_service import PaqueteService
from app.services.sucursal.ingreso_service import IngresoService
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
        self.gasto_service    = GastoService()
        self.ingreso_service  = IngresoService()

    async def numero_paquetes(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.paquete_service.numero_paquetes(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def peso_promedio(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.paquete_service.peso_promedio(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def costo_promedio(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.paquete_service.costo_promedio(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def vehiculos_tot(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.vehiculo_service.vehiculos_tot()
        return ResponseSchema(detail="", result=roles)
    
    async def sucursales_tot(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.sucursal_service.sucursales_tot()
        return ResponseSchema(detail="", result=roles)
    
    async def empleados_tot(self, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.usuario_service.usuarios_tot()
        return ResponseSchema(detail="", result=roles)
    
    async def paquetes_estado(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.paquete_service.paquetes_estado(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def top_sucursales(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.sucursal_service.top_sucursales(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def gasto(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.gasto_service.gasto(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def gasto_promedio(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.gasto_service.gasto_promedio(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def tipo_gasto(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.gasto_service.tipo_gasto(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def concepto_gasto(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.gasto_service.concepto_gasto(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def gasto_sucursal(self, fecha: datetime = Query(None), user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.gasto_service.gasto_sucursal(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def ingreso(self, fecha: datetime = Query(None)):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.ingreso_service.ingreso(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def ingreso_pron(self, fecha: datetime = Query(None)):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.ingreso_service.ingreso_pron(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def ingreso_real_vs_pron(self, fecha: datetime = Query(None)):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.ingreso_service.ingreso_real_vs_pron(fecha=fecha)
        return ResponseSchema(detail="", result=roles)
    
    async def ingreso_sucursal(self, fecha: datetime = Query(None)):#, user: dict = Depends(get_current_user_with_roles(allowed_roles=["Operador", "Admin"]))):
        roles = await self.ingreso_service.ingreso_sucursal(fecha=fecha)
        return ResponseSchema(detail="", result=roles)