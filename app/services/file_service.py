"""File handling service (M3 Week 1).

Responsible for:
- Validating file type (extension + content_type)
- Enforcing size limits
- Saving uploads to disk

This keeps endpoint/controller logic thin.
"""

from __future__ import annotations

import os
from pathlib import Path

from app.core.errors import UnsupportedFileTypeError
from app.core.settings import get_settings

# Common content-types for supported document types
PDF_MIME = "application/pdf"
DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


async def save_upload_file(file) -> dict:
    """Validate and save an UploadFile.

    Args:
        file: FastAPI UploadFile

    Returns:
        dict shaped for UploadResponse schema.
    """

    settings = get_settings()

    # Ensure directory exists
    upload_dir = Path(settings.UPLOAD_DIR)
    upload_dir.mkdir(parents=True, exist_ok=True)

    original_filename = file.filename or "uploaded"
    ext = Path(original_filename).suffix.lower()

    if ext not in settings.ALLOWED_EXTENSIONS:
        raise UnsupportedFileTypeError(
            message=f"Unsupported file extension '{ext}'. Only PDF and DOCX are allowed."
        )

    # content_type may be missing or spoofed; still validate if present.
    content_type = (file.content_type or "").lower()
    allowed_mimes = {PDF_MIME.lower(), DOCX_MIME.lower()}

    # If content_type is provided, ensure it's allowed. If empty, fall back to extension.
    if content_type and content_type not in allowed_mimes:
        raise UnsupportedFileTypeError(
            message=f"Unsupported content_type '{file.content_type}'. Only PDF and DOCX are allowed."
        )

    # Stream read to enforce max size without loading the whole file into memory.
    max_size = settings.MAX_UPLOAD_SIZE_BYTES
    size_bytes = 0

    # Make a safe filesystem filename.
    safe_name = original_filename.replace("..", "").replace("/", "_").replace("\\", "_")
    save_path = upload_dir / safe_name

    # If file exists, append a suffix to avoid overwrite.
    if save_path.exists():
        stem = save_path.stem
        suffix = save_path.suffix
        save_path = upload_dir / f"{stem}__upload{suffix}"

    # Write to disk in chunks.
    try:
        with open(save_path, "wb") as out:
            while True:
                chunk = await file.read(1024 * 1024)  # 1MB chunks
                if not chunk:
                    break
                size_bytes += len(chunk)
                if size_bytes > max_size:
                    # Clean up partial file.
                    try:
                        out.close()
                        os.remove(save_path)
                    except OSError:
                        pass
                    raise UnsupportedFileTypeError(
                        message=f"File too large. Max allowed is {max_size} bytes."
                    )
                out.write(chunk)
    finally:
        await file.close()

    # If content_type missing, infer from extension.
    detected_content_type = file.content_type
    if not detected_content_type:
        detected_content_type = PDF_MIME if ext == ".pdf" else DOCX_MIME

    return {
        "filename": original_filename,
        "content_type": detected_content_type,
        "size_bytes": size_bytes,
        "saved_path": str(save_path.relative_to(Path.cwd())),
    }

