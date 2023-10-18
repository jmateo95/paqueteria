from fastapi import APIRouter, Path
from schema import ResponseSchema
from app.services.ciudad_service import CiudadService
from app.models.ciudad_model import CiudadCreate, CiudadUpdate

router =APIRouter(
    prefix="/ciudad",
    tags=['ciudad']
)

@router.get(path="", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all():
    result = await CiudadService.get_all()
    return ResponseSchema(detail="", result=result)


@router.get(path="/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id(ciudad_id:int=Path(..., alias="id")):
    result = await CiudadService.get_by_id(ciudad_id)
    return ResponseSchema(detail="", result=result)


@router.post(path="", response_model=ResponseSchema, response_model_exclude_none=True)
async def create(ciudad: CiudadCreate):
    await CiudadService.create(ciudad)
    return ResponseSchema(detail="")


@router.delete(path="/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete(ciudad_id:int=Path(..., alias="id")):
    await CiudadService.delete(ciudad_id)
    return ResponseSchema(detail="")


@router.patch(path="/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update(ciudad_id:int=Path(..., alias="id"),*, ciudad:CiudadUpdate):
    await CiudadService.update(ciudad_id, ciudad)
    return ResponseSchema(detail="")