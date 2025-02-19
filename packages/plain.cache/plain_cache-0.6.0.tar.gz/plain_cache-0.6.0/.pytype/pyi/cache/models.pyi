# (generated with --quick)

from plain import models
from plain.utils import timezone
from typing import Any

class CachedItem(Any):
    created_at: Any
    expires_at: Any
    key: Any
    objects: Any
    updated_at: Any
    value: Any
    def __str__(self) -> str: ...

class CachedItemQuerySet(Any):
    def expired(self) -> Any: ...
    def forever(self) -> Any: ...
    def unexpired(self) -> Any: ...
