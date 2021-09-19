from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import config, routers


settings: config.Settings = config.get_settings()
app = FastAPI(
    title=settings.title, description=settings.description, version=settings.version,
    docs_url=settings.swagger, redoc_url=settings.redoc)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routers.home.router)
app.include_router(routers.report.router)
