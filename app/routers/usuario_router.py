from fastapi import APIRouter
from app.controllers.usuario_controller import usuario_controller
router = APIRouter(
    prefix="/usuario",
    tags=['Usuario']
)

router.add_api_route("/", usuario_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", usuario_controller.get_by_id, methods=["GET"])
router.add_api_route("/", usuario_controller.create, methods=["POST"])
router.add_api_route("/{id}", usuario_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", usuario_controller.delete, methods=["DELETE"])
router.add_api_route("/login", usuario_controller.login, methods=["POST"])
