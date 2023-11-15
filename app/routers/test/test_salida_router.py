from fastapi import APIRouter
from app.controllers.test.test_salida_controller import SalidaController
router = APIRouter(
    prefix="/test/salida",
    tags=['Test']
)

salida_controller = SalidaController()

router.add_api_route("/", salida_controller.get_salidas_by_filters, methods=["GET"])
router.add_api_route("/", salida_controller.create, methods=["POST"])