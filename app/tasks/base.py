"""Async task interface (M3 Week 1).

This file prepares for future Celery integration by providing:
- an abstract-ish task base
- a place to define task payloads

Current implementation is framework-agnostic.
"""

from __future__ import annotations

from typing import Any, Protocol


class Task(Protocol):
    """Protocol for async tasks."""

    async def run(self, payload: dict[str, Any]) -> dict[str, Any]:  # pragma: no cover
        ...

