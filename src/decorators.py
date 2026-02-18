from __future__ import annotations

import functools
import logging
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

logger = logging.getLogger(__name__)


def report_logger(func: F) -> F:
    """Декоратор для логирования вызова отчётов."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.info("Running report: %s", func.__name__)
        result = func(*args, **kwargs)
        logger.info("Finished report: %s", func.__name__)
        return result

    return wrapper  # type: ignore[return-value]
