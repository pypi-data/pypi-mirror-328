from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TypeVar, cast

from cachetools.func import ttl_cache

from utilities.datetime import datetime_duration_to_float
from utilities.functions import identity
from utilities.functools import lru_cache

if TYPE_CHECKING:
    from utilities.types import Duration

_F = TypeVar("_F", bound=Callable[..., Any])


def cache(
    *, max_size: int | None = None, max_duration: Duration | None = None
) -> Callable[[_F], _F]:
    """Decorate a function with `max_size` and/or `ttl` settings."""
    if max_duration is not None:
        return ttl_cache(maxsize=max_size, ttl=datetime_duration_to_float(max_duration))
    if max_size is not None:
        return cast(Any, lru_cache(max_size=max_size))
    return identity


__all__ = ["cache"]
