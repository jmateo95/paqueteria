from fastapi import APIRouter
from app.controllers.sucursal.tipo_salida_controller import TipoSalidaController
router = APIRouter(
    prefix="/tipo-salida",
    tags=['TipoSalida']
)

tipo_salida_controller = TipoSalidaController()

router.add_api_route("/", tipo_salida_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", tipo_salida_controller.get_by_id, methods=["GET"])
router.add_api_route("/", tipo_salida_controller.create, methods=["POST"])
router.add_api_route("/{id}", tipo_salida_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", tipo_salida_controller.delete, methods=["DELETE"])
