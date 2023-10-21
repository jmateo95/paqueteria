from fastapi import FastAPI
import uvicorn
from config.Connection import prisma_connection
from app.api import api_router
from fastapi.middleware.cors import CORSMiddleware

def init_app():
    app = FastAPI(
        title="Paqueteria",
        description="FastAPI",
        version="1.0.0"
    )

    # Configuración de CORS para permitir solicitudes desde cualquier origen
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Esto permite solicitudes desde cualquier origen
        allow_credentials=True,
        allow_methods=["*"],  # Esto permite todos los métodos HTTP
        allow_headers=["*"],  # Esto permite todos los encabezados HTTP
    )

    @app.on_event("startup")
    async def startup():
        print("Iniciando El Servidor")
        await prisma_connection.Connect()

    @app.on_event("shutdown")
    async def shutdown():
        print("Deteniendo El Servidor")
        await prisma_connection.Disconnect()

    app.include_router(api_router, prefix='/api/v1')

    return app

app = init_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)