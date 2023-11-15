from fastapi import APIRouter
from app.controllers.test.test_segmento_controller import SegmentoController
router = APIRouter(
    prefix="/test/segmento",
    tags=['Test']
)

segmento_controller = SegmentoController()

router.add_api_route("/", segmento_controller.get_all, methods=["GET"])
router.add_api_route("/", segmento_controller.create, methods=["POST"])
router.add_api_route("/sucursal/{sucursal_origen_id}", segmento_controller.get_by_sucursal_origen, methods=["GET"])
router.add_api_route("/sucursal/{sucursal_origen_id}/{sucursal_destino_id}", segmento_controller.get_by_sucursales, methods=["GET"])
