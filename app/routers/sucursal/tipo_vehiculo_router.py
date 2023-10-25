from fastapi import APIRouter
from app.controllers.sucursal.tipo_vehiculo_controller import TipoVehiculoController
router = APIRouter(
    prefix="/tipo_vehiculo",
    tags=['TipoVehiculo']
)

tipo_vehiculo_controller = TipoVehiculoController()

router.add_api_route("/", tipo_vehiculo_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", tipo_vehiculo_controller.get_by_id, methods=["GET"])
router.add_api_route("/", tipo_vehiculo_controller.create, methods=["POST"])
router.add_api_route("/{id}", tipo_vehiculo_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", tipo_vehiculo_controller.delete, methods=["DELETE"])
