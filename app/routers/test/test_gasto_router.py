from fastapi import APIRouter
from app.controllers.gasto.gasto_controller import GastoController
router = APIRouter(
    prefix="/test/gasto",
    tags=['Test']
)

gasto_controller = GastoController()

router.add_api_route("/", gasto_controller.get_gastos_by_filters, methods=["GET"])
router.add_api_route("/", gasto_controller.create, methods=["POST"])