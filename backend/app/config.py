from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    name: str = "spam_protection"
    title: str = "Spam Protection"
    description: str = "The backend for the Spam Protection system"
    swagger: str = "/docs"
    redoc: str = "/redoc"


@lru_cache()
def get_settings():
    """Return module settings global settings.
    This method is cached through python's lru_cache decorator, so
    only the first request creates an object, and all other requests
    to this method returns the same object created the first time.
    """
    return Settings()
