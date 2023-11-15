from fastapi import APIRouter
from app.controllers.test.test_ingreso_controller import IngresoController
router = APIRouter(
    prefix="/test/ingreso",
    tags=['Test']
)

ingreso_controller = IngresoController()

router.add_api_route("/pronosticado/", ingreso_controller.get_ingresos_pronosticados_by_filters, methods=["GET"])
