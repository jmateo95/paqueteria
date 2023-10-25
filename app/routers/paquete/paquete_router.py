from fastapi import APIRouter
from app.controllers.paquete.paquete_controller import PaqueteController
router = APIRouter(
    prefix="/paquete",
    tags=['Paquete']
)

paquete_controller = PaqueteController()

router.add_api_route("/", paquete_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", paquete_controller.get_by_id, methods=["GET"])
router.add_api_route("/", paquete_controller.create, methods=["POST"])
router.add_api_route("/{id}", paquete_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", paquete_controller.delete, methods=["DELETE"])
