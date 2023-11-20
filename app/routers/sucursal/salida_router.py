from fastapi import APIRouter
from app.controllers.sucursal.salida_controller import SalidaController
router = APIRouter(
    prefix="/salida",
    tags=['Salida']
)

salida_controller = SalidaController()

router.add_api_route("/", salida_controller.get_salidas_by_filters, methods=["GET"])
router.add_api_route("/{id}", salida_controller.get_by_id, methods=["GET"])
router.add_api_route("/", salida_controller.create, methods=["POST"])
router.add_api_route("/{id}", salida_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", salida_controller.delete, methods=["DELETE"])
router.add_api_route("/dar_salida/{id}", salida_controller.dar_salida, methods=["PATCH"])
router.add_api_route("/ingresar/{id}", salida_controller.ingresar, methods=["PATCH"])