from fastapi import APIRouter
from app.controllers.paquete.tracking_log_controller import TrackingLogController
router = APIRouter(
    prefix="/tracking_log",
    tags=['Tracking']
)

tracking_log_controller = TrackingLogController()

router.add_api_route("/", tracking_log_controller.get_tracking_log_by_filters, methods=["GET"])