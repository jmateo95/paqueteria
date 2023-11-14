from fastapi import APIRouter
from app.controllers.test.test_sucursal_controller import sucursal_controller
router = APIRouter(
    prefix="/test/sucursal",
    tags=['Test']
)

router.add_api_route("/", sucursal_controller.get_all, methods=["GET"])
router.add_api_route("/", sucursal_controller.create, methods=["POST"])