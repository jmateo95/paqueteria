from fastapi import APIRouter
from app.controllers.sucursal.segmento_controller import SegmentoController
router = APIRouter(
    prefix="/segmento",
    tags=['Segmento']
)

segmento_controller = SegmentoController()

router.add_api_route("/", segmento_controller.get_all, methods=["GET"])
router.add_api_route("/", segmento_controller.create, methods=["POST"])
router.add_api_route("/sucursal/{sucursal_origen_id}", segmento_controller.get_by_sucursal_origen, methods=["GET"])
router.add_api_route("/sucursal/{sucursal_origen_id}/{sucursal_destino_id}", segmento_controller.get_by_sucursales, methods=["GET"])
router.add_api_route("/graficar", segmento_controller.generate_graph, methods=["GET"])


router.add_api_route("/{id}", segmento_controller.get_by_id, methods=["GET"])
router.add_api_route("/{id}", segmento_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", segmento_controller.delete, methods=["DELETE"])
