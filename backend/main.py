from fastapi import FastAPI
from backend import config, routers


settings: config.Settings = config.get_settings()
app = FastAPI(
    title=settings.title, description=settings.description, version=settings.version,
    docs_url=settings.swagger, redoc_url=settings.redoc)
app.include_router(routers.home.router)
