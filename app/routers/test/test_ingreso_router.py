from fastapi import APIRouter
from app.controllers.test.test_ingreso_controller import IngresoController
router = APIRouter(
    prefix="/test/ingreso",
    tags=['Test']
)

ingreso_controller = IngresoController()

router.add_api_route("/pronosticado/", ingreso_controller.get_ingresos_pronosticados_by_filters, methods=["GET"])


router.add_api_route("/", ingreso_controller.get_ingresos_by_filters, methods=["GET"])
router.add_api_route("/{id}", ingreso_controller.get_by_id, methods=["GET"])
router.add_api_route("/", ingreso_controller.create, methods=["POST"])
router.add_api_route("/{id}", ingreso_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", ingreso_controller.delete, methods=["DELETE"])
