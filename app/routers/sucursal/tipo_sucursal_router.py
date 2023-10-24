from fastapi import APIRouter
from app.controllers.sucursal.tipo_sucursal_controller import tipo_sucursal_controller
router = APIRouter(
    prefix="/tipo-sucursal",
    tags=['Tipo-Sucursal']
)

router.add_api_route("/", tipo_sucursal_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", tipo_sucursal_controller.get_by_id, methods=["GET"])
router.add_api_route("/", tipo_sucursal_controller.create, methods=["POST"])
router.add_api_route("/{id}", tipo_sucursal_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", tipo_sucursal_controller.delete, methods=["DELETE"])