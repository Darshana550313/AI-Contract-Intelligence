"""FastAPI application entrypoint (M3 Week 1).

Run with:
    uvicorn app.main:app --reload

This module wires settings, logging, and API routers.
"""

from fastapi import FastAPI

from app.api.routes import api_router
from app.core.logging import configure_logging
from app.core.settings import get_settings


settings = get_settings()
configure_logging(settings.LOG_LEVEL)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Include API routes
app.include_router(api_router)

