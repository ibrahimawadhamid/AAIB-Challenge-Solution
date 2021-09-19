from fastapi import APIRouter, Depends
from ..config import get_settings, Settings

router = APIRouter(tags=["home"])


@router.get("/")
def home(settings: Settings = Depends(get_settings)):
    """Returns information about the service,
    also can be used to validate if the service is working."""
    service_info = {
        "name": settings.name,
        "title": settings.title,
        "description": settings.description,
        "swagger": settings.swagger,
        "redoc": settings.redoc
    }
    return service_info
