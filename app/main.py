from fastapi import FastAPI
from app.database import engine, Base
from app.api.routers import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Teste-Template", openapi_url=f"/v1/openapi.json"
)

app.include_router(api_router)