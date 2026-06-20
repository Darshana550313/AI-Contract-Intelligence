"""Central router for the FastAPI service (M3 Week 1)."""

from fastapi import APIRouter

from app.api.endpoints.upload import router as upload_router

api_router = APIRouter()

# Upload endpoints
api_router.include_router(upload_router, tags=["upload"])

