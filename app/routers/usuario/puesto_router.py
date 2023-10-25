from fastapi import APIRouter
from app.controllers.usuario.puesto_controller import puesto_controller
router = APIRouter(
    prefix="/puesto",
    tags=['Puesto']
)

router.add_api_route("/", puesto_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", puesto_controller.get_by_id, methods=["GET"])
router.add_api_route("/", puesto_controller.create, methods=["POST"])
router.add_api_route("/{id}", puesto_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", puesto_controller.delete, methods=["DELETE"])