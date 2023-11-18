from fastapi import APIRouter
from app.routers.usuario import usuario_router, puesto_router, rol_router
from app.routers.sucursal import ciudad_router, tipo_sucursal_router, sucursal_router, tarifario_router, tipo_vehiculo_router, vehiculo_router, segmento_router, tipo_salida_router, salida_router, ingreso_router
from app.routers.gasto import tipo_gasto_router, concepto_gasto_router, gasto_router
from app.routers.paquete import estado_paquete_router, estado_tracking_router, paquete_router, tracking_router, tracking_log_router
from app.routers.dashboard import dashboard_router
from app.routers.test import test_tarifario_router, test_sucursal_router, test_usuario_router, test_segmento_router, test_salida_router, test_gasto_router

api_router = APIRouter()

#RUTAS
api_router.include_router(rol_router.router )
api_router.include_router(puesto_router.router)
api_router.include_router(usuario_router.router)

api_router.include_router(ciudad_router.router)
api_router.include_router(tipo_sucursal_router.router)
api_router.include_router(tipo_vehiculo_router.router)
api_router.include_router(sucursal_router.router)
api_router.include_router(tarifario_router.router)
api_router.include_router(vehiculo_router.router)
api_router.include_router(segmento_router.router)
api_router.include_router(tipo_salida_router.router)
api_router.include_router(salida_router.router)

api_router.include_router(ingreso_router.router)
api_router.include_router(tipo_gasto_router.router)
api_router.include_router(concepto_gasto_router.router)
api_router.include_router(gasto_router.router)

api_router.include_router(estado_paquete_router.router)
api_router.include_router(estado_tracking_router.router)
api_router.include_router(paquete_router.router)
api_router.include_router(tracking_router.router)
api_router.include_router(tracking_log_router.router)

api_router.include_router(dashboard_router.router)


api_router.include_router(test_tarifario_router.router)
api_router.include_router(test_sucursal_router.router)
api_router.include_router(test_usuario_router.router)
api_router.include_router(test_segmento_router.router)
api_router.include_router(test_salida_router.router)
api_router.include_router(test_gasto_router.router)


