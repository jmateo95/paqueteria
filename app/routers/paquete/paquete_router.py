from fastapi import APIRouter
from app.controllers.paquete.paquete_controller import PaqueteController
router = APIRouter(
    prefix="/paquete",
    tags=['Paquete']
)

paquete_controller = PaqueteController()

router.add_api_route("/", paquete_controller.get_paquetes_by_filters, methods=["GET"])
router.add_api_route("/{id}", paquete_controller.get_by_id, methods=["GET"])
router.add_api_route("/buscar/{no_guia}", paquete_controller.get_by_no_guia, methods=["GET"])
router.add_api_route("/", paquete_controller.create, methods=["POST"])
router.add_api_route("/{id}", paquete_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", paquete_controller.delete, methods=["DELETE"])
router.add_api_route("/cotizar", paquete_controller.cotizar, methods=["POST"])
router.add_api_route("/cargar/{id}", paquete_controller.cargar, methods=["PATCH"])
