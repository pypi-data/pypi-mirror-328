# (generated with --quick)

import os
import pathlib
from typing import Annotated, Any, TypeVar

SuspiciousFileOperation: Any

_T0 = TypeVar('_T0')

class FileProxyMixin:
    __doc__: str
    closed: Annotated[Any, 'property']
    encoding: Annotated[Any, 'property']
    fileno: Annotated[Any, 'property']
    flush: Annotated[Any, 'property']
    isatty: Annotated[Any, 'property']
    newlines: Annotated[Any, 'property']
    read: Annotated[Any, 'property']
    readinto: Annotated[Any, 'property']
    readline: Annotated[Any, 'property']
    readlines: Annotated[Any, 'property']
    seek: Annotated[Any, 'property']
    tell: Annotated[Any, 'property']
    truncate: Annotated[Any, 'property']
    write: Annotated[Any, 'property']
    writelines: Annotated[Any, 'property']
    def __iter__(self) -> Any: ...
    def readable(self) -> Any: ...
    def seekable(self) -> Any: ...
    def writable(self) -> Any: ...

def validate_file_name(name: _T0, allow_relative_path = ...) -> _T0: ...
