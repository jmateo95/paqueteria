from fastapi import FastAPI
import uvicorn
from config.Connection import prisma_connection
from app.api import api_router

def init_app():
    app = FastAPI(
        title = "Paqueteria",
        description = "FastAPI",
        version = "1.0.0"
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