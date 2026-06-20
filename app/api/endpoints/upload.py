"""Upload endpoint for PDF/DOCX files (M3 Week 1).

Implements:
    POST /upload

Behavior:
- Validates file type (PDF, DOCX)
- Saves uploaded content into ./uploads/
- Returns structured JSON responses
"""

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.core.errors import APIError, UnsupportedFileTypeError
from app.api.schemas.upload import UploadResponse
from app.services.file_service import save_upload_file

router = APIRouter()


@router.post("/upload", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_contract(file: UploadFile = File(...)) -> UploadResponse:
    """Upload a contract document.

    Expected content types:
    - application/pdf
    - application/vnd.openxmlformats-officedocument.wordprocessingml.document

    Returns:
        UploadResponse: structured JSON including saved path.
    """

    try:
        saved = await save_upload_file(file)
        return UploadResponse(**saved)
    except UnsupportedFileTypeError as e:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail=e.to_detail())
    except APIError as e:
        # Generic APIError handling
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.to_detail())
    except Exception:
        # Avoid leaking internal exception details in production.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "internal_error", "message": "Failed to process upload."},
        )

