from fastapi import APIRouter
from app.controllers.sucursal.tarifario_controller import TarifarioController
router = APIRouter(
    prefix="/tarifario",
    tags=['Tarifario']
)

tarifario_controller = TarifarioController()

router.add_api_route("/", tarifario_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", tarifario_controller.get_by_id, methods=["GET"])
router.add_api_route("/", tarifario_controller.create, methods=["POST"])
router.add_api_route("/{id}", tarifario_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", tarifario_controller.delete, methods=["DELETE"])
