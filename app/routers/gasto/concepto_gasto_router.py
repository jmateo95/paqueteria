from fastapi import APIRouter
from app.controllers.gasto.concepto_gasto_controller import ConceptoGastoController
router = APIRouter(
    prefix="/concepto_gasto",
    tags=['ConceptoGasto']
)

concepto_gasto_controller = ConceptoGastoController()

router.add_api_route("/", concepto_gasto_controller.get_all, methods=["GET"])
router.add_api_route("/{id}", concepto_gasto_controller.get_by_id, methods=["GET"])
router.add_api_route("/", concepto_gasto_controller.create, methods=["POST"])
router.add_api_route("/{id}", concepto_gasto_controller.update, methods=["PATCH"])
router.add_api_route("/{id}", concepto_gasto_controller.delete, methods=["DELETE"])
