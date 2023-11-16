from fastapi import APIRouter
from app.controllers.test.test_vehiculo_controller import VehiculoController
router = APIRouter(
    prefix="/vehiculo",
    tags=['Vehiculo']
)

vehiculo_controller = VehiculoController()

router.add_api_route("/", vehiculo_controller.get_all, methods=["GET"])
router.add_api_route("/", vehiculo_controller.create, methods=["POST"])


router.add_api_route("/{id}", vehiculo_controller.get_by_id, methods=["GET"])
router.add_api_route("/{id}", vehiculo_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", vehiculo_controller.delete, methods=["DELETE"])
router.add_api_route("/sucursal/{sucursal_id}", vehiculo_controller.get_by_sucursal, methods=["GET"])
