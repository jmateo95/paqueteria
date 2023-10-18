from fastapi import APIRouter, Depends, HTTPException
from prisma import Client
from app.controllers.ciudad_controller import CiudadController
from app.schemas.ciudad_schema import CiudadCreate, CiudadUpdate
from main import get_database

router = APIRouter()

@router.get("/ciudades/{ciudad_id}", response_model=dict)
def read_ciudad(ciudad_id: int, db: Client = Depends(get_database)):  # Usa Depends para obtener la instancia de la base de datos
    ciudad = CiudadController(db).get_ciudad_by_id(ciudad_id)
    if ciudad is None:
        raise HTTPException(status_code=404, detail="Ciudad not found")
    return ciudad

@router.get("/ciudades", response_model=list)
def read_ciudades(db: Client = Depends(get_database)):  # Usa Depends para obtener la instancia de la base de datos
    return CiudadController(db).get_all_ciudades()

@router.post("/ciudades", response_model=dict)
def create_ciudad(ciudad: CiudadCreate, db: Client = Depends(get_database)):  # Usa Depends para obtener la instancia de la base de datos
    return CiudadController(db).create_ciudad(ciudad)

@router.put("/ciudades/{ciudad_id}", response_model=dict)
def update_ciudad(ciudad_id: int, ciudad: CiudadUpdate, db: Client = Depends(get_database)):  # Usa Depends para obtener la instancia de la base de datos
    return CiudadController(db).update_ciudad(ciudad_id, ciudad)

@router.delete("/ciudades/{ciudad_id}", response_model=dict)
def delete_ciudad(ciudad_id: int, db: Client = Depends(get_database)):  # Usa Depends para obtener la instancia de la base de datos
    return CiudadController(db).delete_ciudad(ciudad_id)
