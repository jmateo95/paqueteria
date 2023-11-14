from fastapi import APIRouter
from app.controllers.test.test_usuario_controller import usuario_controller
router = APIRouter(
    prefix="/test/usuario",
    tags=['Test']
)

router.add_api_route("/", usuario_controller.get_users_by_filters, methods=["GET"])
router.add_api_route("/", usuario_controller.create, methods=["POST"])