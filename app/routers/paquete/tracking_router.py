from fastapi import APIRouter
from app.controllers.paquete.tracking_controller import TrackingController
router = APIRouter(
    prefix="/tracking",
    tags=['Tracking']
)

tracking_controller = TrackingController()

router.add_api_route("/", tracking_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", tracking_controller.get_by_id, methods=["GET"])
router.add_api_route("/", tracking_controller.create, methods=["POST"])
router.add_api_route("/{id}", tracking_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", tracking_controller.delete, methods=["DELETE"])
