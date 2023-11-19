from fastapi import APIRouter
from app.controllers.test.test_dashboard_controller import DashboardController
router = APIRouter(
    prefix="/test//dashboard",
    tags=['Test']
)

dashboard_controller = DashboardController()

router.add_api_route("/numero_paquetes",        dashboard_controller.numero_paquetes,       methods=["GET"])
router.add_api_route("/peso_promedio",          dashboard_controller.peso_promedio,         methods=["GET"])
router.add_api_route("/costo_promedio",         dashboard_controller.costo_promedio,        methods=["GET"])
router.add_api_route("/vehiculos_tot",          dashboard_controller.vehiculos_tot,         methods=["GET"])
router.add_api_route("/sucursales_tot",         dashboard_controller.sucursales_tot,        methods=["GET"])
router.add_api_route("/empleados_tot",          dashboard_controller.empleados_tot,         methods=["GET"])
router.add_api_route("/paquetes_estado",        dashboard_controller.paquetes_estado,       methods=["GET"])
router.add_api_route("/top_sucursales",         dashboard_controller.top_sucursales,        methods=["GET"])
router.add_api_route("/gasto",                  dashboard_controller.gasto,                 methods=["GET"])
router.add_api_route("/gasto_promedio",         dashboard_controller.gasto_promedio,        methods=["GET"])
router.add_api_route("/tipo_gasto",             dashboard_controller.tipo_gasto,            methods=["GET"])
router.add_api_route("/concepto_gasto",         dashboard_controller.concepto_gasto,        methods=["GET"])
router.add_api_route("/gasto_sucursal",         dashboard_controller.gasto_sucursal,        methods=["GET"])
router.add_api_route("/ingreso",                dashboard_controller.ingreso,               methods=["GET"])
router.add_api_route("/ingreso_pron",           dashboard_controller.ingreso_pron,          methods=["GET"])
router.add_api_route("/ingreso_real_vs_pron",   dashboard_controller.ingreso_real_vs_pron,  methods=["GET"])
router.add_api_route("/ingreso_sucursal",       dashboard_controller.ingreso_sucursal,      methods=["GET"])