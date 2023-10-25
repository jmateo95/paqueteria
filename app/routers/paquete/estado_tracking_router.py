from fastapi import APIRouter
from app.controllers.paquete.estado_tracking_controller import EstadoTrackingController
router = APIRouter(
    prefix="/estado-tracking",
    tags=['EstadoTracking']
)

estado_tracking_controller = EstadoTrackingController()

router.add_api_route("/", estado_tracking_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", estado_tracking_controller.get_by_id, methods=["GET"])
router.add_api_route("/", estado_tracking_controller.create, methods=["POST"])
router.add_api_route("/{id}", estado_tracking_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", estado_tracking_controller.delete, methods=["DELETE"])
