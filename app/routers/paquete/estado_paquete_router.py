from fastapi import APIRouter
from app.controllers.paquete.estado_paquete_controller import EstadoPaqueteController
router = APIRouter(
    prefix="/estado-paquete",
    tags=['EstadoPaquete']
)

estado_paquete_controller = EstadoPaqueteController()

router.add_api_route("/", estado_paquete_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", estado_paquete_controller.get_by_id, methods=["GET"])
router.add_api_route("/", estado_paquete_controller.create, methods=["POST"])
router.add_api_route("/{id}", estado_paquete_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", estado_paquete_controller.delete, methods=["DELETE"])
