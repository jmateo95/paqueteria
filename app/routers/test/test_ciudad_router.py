from fastapi import APIRouter
from app.controllers.test.test_ciudad_controller import ciudad_controller
router = APIRouter(
    prefix="/test/ciudad",
    tags=['Test']
)

router.add_api_route("/", ciudad_controller.get_all, methods=["GET"])
router.add_api_route("/", ciudad_controller.create, methods=["POST"])


router.add_api_route("/{id}", ciudad_controller.get_by_id, methods=["GET"])
router.add_api_route("/{id}", ciudad_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", ciudad_controller.delete, methods=["DELETE"])
