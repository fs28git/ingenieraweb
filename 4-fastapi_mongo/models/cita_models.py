from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson import ObjectId
from datetime import datetime

class PyObjectId(str):
    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return v
        raise ValueError("Not a valid ObjectId")

class Cita(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    paciente: str
    fecha: datetime
    especialista: str
    tipo: str
    estado: str

    @field_validator("id", mode="before")
    @classmethod
    def validate_object_id(cls, v):
        return PyObjectId.validate(v) if v is not None else None

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True
