"""Logging configuration (M3 Week 1).

Configures stdlib logging in a production-friendly way.
"""

import logging


def configure_logging(level: str = "INFO") -> None:
    """Configure root logging.

    Args:
        level: Logging level string (e.g., "INFO", "DEBUG").
    """

    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

