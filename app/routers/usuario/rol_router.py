from fastapi import APIRouter
from app.controllers.usuario.rol_controller import RolController
router = APIRouter(
    prefix="/rol",
    tags=['Rol']
)

rol_controller = RolController()

router.add_api_route("/", rol_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", rol_controller.get_by_id, methods=["GET"])
router.add_api_route("/", rol_controller.create, methods=["POST"])
router.add_api_route("/{id}", rol_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", rol_controller.delete, methods=["DELETE"])
