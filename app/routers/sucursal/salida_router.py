from fastapi import APIRouter
from app.controllers.sucursal.salida_controller import SalidaController
router = APIRouter(
    prefix="/salida",
    tags=['Salida']
)

salida_controller = SalidaController()

router.add_api_route("/", salida_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", salida_controller.get_by_id, methods=["GET"])
router.add_api_route("/", salida_controller.create, methods=["POST"])
router.add_api_route("/{id}", salida_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", salida_controller.delete, methods=["DELETE"])