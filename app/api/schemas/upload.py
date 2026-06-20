"""Pydantic schemas for upload responses (M3 Week 1)."""

from pydantic import BaseModel, Field


class UploadResponse(BaseModel):
    """Structured JSON response for successful uploads."""

    filename: str = Field(..., description="Original filename provided by the client")
    content_type: str = Field(..., description="Detected/validated content type")
    size_bytes: int = Field(..., description="Size of uploaded file in bytes")
    saved_path: str = Field(..., description="Relative path where the file was saved")

