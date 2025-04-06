from fastapi import APIRouter, HTTPException
from models.cita_models import Cita
from services.cita_service import (
    obtener_citas,
    obtener_cita_por_id,
    insertar_cita,
    actualizar_cita,
    eliminar_cita
)

router = APIRouter()

@router.get("/citas-start/")
def start_citas():
    return {"message": "Bienvenido al servicio de citas médicas"}

@router.get("/citas", response_model=list)
async def obtener_citas_endpoint():
    return obtener_citas()

@router.get("/citas/{cita_id}", response_model=Cita)
def obtener_cita(cita_id: str):
    cita = obtener_cita_por_id(cita_id)
    if cita:
        return cita
    raise HTTPException(status_code=404, detail="Cita no encontrada")

@router.post("/citas", status_code=201)
def crear_cita(cita: Cita):
    cita_id = insertar_cita(cita)
    return {"message": "Cita creada correctamente", "id": cita_id}

@router.put("/citas/{cita_id}")
def actualizar_cita_endpoint(cita_id: str, cita: Cita):
    actualizado = actualizar_cita(cita_id, cita)
    if actualizado:
        return {"message": "Cita actualizada correctamente"}
    raise HTTPException(status_code=404, detail="Cita no encontrada")

@router.delete("/citas/{cita_id}")
def eliminar_cita_endpoint(cita_id: str):
    eliminado = eliminar_cita(cita_id)
    if eliminado:
        return {"message": "Cita eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Cita no encontrada")