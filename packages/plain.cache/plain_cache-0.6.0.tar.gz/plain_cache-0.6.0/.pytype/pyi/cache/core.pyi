# (generated with --quick)

import datetime as _datetime
import functools
from plain.utils import timezone
from typing import Annotated, Any, Optional, Union

IntegrityError: Any
cached_property: type[functools.cached_property]
datetime: type[_datetime.datetime]
timedelta: type[_datetime.timedelta]

class Cached:
    __doc__: str
    _model_class: type
    _model_instance: Annotated[Any, 'property']
    key: str
    value: Annotated[Any, 'property']
    def __init__(self, key: str) -> None: ...
    def _is_expired(self) -> Any: ...
    def delete(self) -> bool: ...
    def exists(self) -> bool: ...
    def reload(self) -> None: ...
    def set(self, value, expiration: Optional[Union[float, _datetime.datetime, _datetime.timedelta]] = ...) -> Any: ...
