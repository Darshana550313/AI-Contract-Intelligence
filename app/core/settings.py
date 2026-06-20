"""Settings/configuration module (M3 Week 1).

Uses pydantic-settings to support environment variable overrides.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "AI-Contract-Intelligence"
    APP_VERSION: str = "0.1.0"

    # Logging
    LOG_LEVEL: str = "INFO"

    # Uploads
    UPLOAD_DIR: str = "uploads"

    # Accepted file constraints
    ALLOWED_EXTENSIONS: tuple[str, ...] = (".pdf", ".docx")
    MAX_UPLOAD_SIZE_BYTES: int = 25 * 1024 * 1024  # 25 MB


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Load and cache settings."""

    return Settings()

