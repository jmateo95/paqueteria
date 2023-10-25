from fastapi import APIRouter
from app.controllers.gasto.tipo_gasto_controller import TipoGastoController
router = APIRouter(
    prefix="/tipo_gasto",
    tags=['TipoGasto']
)

tipo_gasto_controller = TipoGastoController()

router.add_api_route("/", tipo_gasto_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", tipo_gasto_controller.get_by_id, methods=["GET"])
router.add_api_route("/", tipo_gasto_controller.create, methods=["POST"])
router.add_api_route("/{id}", tipo_gasto_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", tipo_gasto_controller.delete, methods=["DELETE"])
