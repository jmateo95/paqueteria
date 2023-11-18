from fastapi import APIRouter
from app.controllers.dashboard.dashboard_controller import DashboardController
router = APIRouter(
    prefix="/dashboard",
    tags=['Dashboard']
)

dashboard_controller = DashboardController()

router.add_api_route("/numero_paquetes",    dashboard_controller.numero_paquetes, methods=["GET"])
router.add_api_route("/peso_promedio",      dashboard_controller.peso_promedio, methods=["GET"])
router.add_api_route("/costo_promedio",     dashboard_controller.costo_promedio, methods=["GET"])
router.add_api_route("/vehiculos_tot",      dashboard_controller.vehiculos_tot, methods=["GET"])
router.add_api_route("/sucursales_tot",     dashboard_controller.sucursales_tot, methods=["GET"])
router.add_api_route("/empleados_tot",      dashboard_controller.empleados_tot, methods=["GET"])
router.add_api_route("/paquetes_estado",    dashboard_controller.paquetes_estado, methods=["GET"])
router.add_api_route("/top_sucursales",     dashboard_controller.top_sucursales, methods=["GET"])