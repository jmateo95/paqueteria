from fastapi import APIRouter
from app.controllers.test.test_usuario_controller import usuario_controller
router = APIRouter(
    prefix="/test/usuario",
    tags=['Test']
)

router.add_api_route("/", usuario_controller.get_users_by_filters, methods=["GET"])
router.add_api_route("/", usuario_controller.create, methods=["POST"])


router.add_api_route("/{id}", usuario_controller.get_by_id, methods=["GET"])
router.add_api_route("/{id}", usuario_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", usuario_controller.delete, methods=["DELETE"])