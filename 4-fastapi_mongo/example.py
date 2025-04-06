from fastapi import FastAPI
from routes.cita_routes import router as cita_router

app = FastAPI(title="API de Citas Médicas")

app.include_router(cita_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Citas Médicas con FastAPI y MongoDB Atlas"}
