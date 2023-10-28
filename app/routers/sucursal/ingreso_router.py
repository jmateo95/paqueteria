from fastapi import APIRouter
from app.controllers.sucursal.ingreso_controller import IngresoController
router = APIRouter(
    prefix="/ingreso",
    tags=['ingreso']
)

ingreso_controller = IngresoController()

router.add_api_route("/", ingreso_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", ingreso_controller.get_by_id, methods=["GET"])
router.add_api_route("/", ingreso_controller.create, methods=["POST"])
router.add_api_route("/{id}", ingreso_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", ingreso_controller.delete, methods=["DELETE"])
