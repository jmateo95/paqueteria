from fastapi import APIRouter
from app.controllers.gasto.gasto_controller import GastoController
router = APIRouter(
    prefix="/gasto",
    tags=['Gasto']
)

gasto_controller = GastoController()

router.add_api_route("/", gasto_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", gasto_controller.get_by_id, methods=["GET"])
router.add_api_route("/", gasto_controller.create, methods=["POST"])
router.add_api_route("/{id}", gasto_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", gasto_controller.delete, methods=["DELETE"])
