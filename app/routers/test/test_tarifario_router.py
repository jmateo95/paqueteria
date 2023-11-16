from fastapi import APIRouter
from app.controllers.test.test_tarifario_controller import TarifarioController
router = APIRouter(
    prefix="/test/tarifario",
    tags=['Test']
)

tarifario_controller = TarifarioController()

router.add_api_route("/", tarifario_controller.get_tarifarios_by_filters, methods=["GET"])
router.add_api_route("/", tarifario_controller.create, methods=["POST"])


router.add_api_route("/{id}", tarifario_controller.get_by_id, methods=["GET"])
router.add_api_route("/{id}", tarifario_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", tarifario_controller.delete, methods=["DELETE"])