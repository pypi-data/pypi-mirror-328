# (generated with --quick)

import functools
from typing import Annotated, Any

__all__: tuple[str]
cached_property: type[functools.cached_property]

class BoundField:
    __doc__: str
    _auto_id: Annotated[Any, 'property']
    _form: Any
    errors: Annotated[Any, 'property']
    field: Any
    html_id: Any
    html_name: Any
    initial: Annotated[Any, 'property']
    name: Any
    def __init__(self, form, field, name) -> None: ...
    def __repr__(self) -> str: ...
    def _has_changed(self) -> Any: ...
    def value(self) -> Any: ...
