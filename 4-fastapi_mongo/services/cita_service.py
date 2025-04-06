from bson import ObjectId
from bson.errors import InvalidId
from db.database import database
from models.cita_models import Cita

collection = database.get_collection("citas")

def obtener_citas():
    print("Entró a obtener_citas()")
    citas = list(collection.find())
    for c in citas:
        c["_id"] = str(c["_id"])
    return citas

def obtener_cita_por_id(cita_id: str):
    try:
        _id = ObjectId(cita_id)
    except InvalidId:
        return None
    cita = collection.find_one({"_id": _id})
    if cita:
        cita["_id"] = str(cita["_id"])
    return cita

def insertar_cita(cita: Cita):
    cita_dict = cita.model_dump(by_alias=True, exclude_none=True)
    result = collection.insert_one(cita_dict)
    return str(result.inserted_id)

def actualizar_cita(cita_id: str, datos: Cita):
    try:
        _id = ObjectId(cita_id)
    except InvalidId:
        return False
    datos_dict = datos.model_dump(by_alias=True, exclude_none=True)
    result = collection.update_one({"_id": _id}, {"$set": datos_dict})
    return result.modified_count > 0

def eliminar_cita(cita_id: str):
    try:
        _id = ObjectId(cita_id)
    except InvalidId:
        return False
    result = collection.delete_one({"_id": _id})
    return result.deleted_count > 0
