"""Custom application error types (M3 Week 1)."""


class APIError(Exception):
    """Base class for predictable API errors."""

    def __init__(self, error: str, message: str):
        super().__init__(message)
        self.error = error
        self.message = message

    def to_detail(self) -> dict:
        return {"error": self.error, "message": self.message}


class UnsupportedFileTypeError(APIError):
    """Raised when an uploaded file is not PDF/DOCX."""

    def __init__(self, message: str = "Unsupported file type. Only PDF and DOCX are allowed."):
        super().__init__(error="unsupported_file_type", message=message)

