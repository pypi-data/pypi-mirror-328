# (generated with --quick)

import operator
from typing import Annotated, Any, Generator, TypeVar

NON_FIELD_ERRORS: str
make_hashable: Any

_T0 = TypeVar('_T0')

class BadRequest(Exception):
    __doc__: str

class DisallowedHost(SuspiciousOperation):
    __doc__: str

class DisallowedRedirect(SuspiciousOperation):
    __doc__: str

class EmptyResultSet(Exception):
    __doc__: str

class FieldDoesNotExist(Exception):
    __doc__: str

class FieldError(Exception):
    __doc__: str

class FullResultSet(Exception):
    __doc__: str

class ImproperlyConfigured(Exception):
    __doc__: str

class MultipleObjectsReturned(Exception):
    __doc__: str

class ObjectDoesNotExist(Exception):
    __doc__: str
    silent_variable_failure: bool

class PackageRegistryNotReady(Exception):
    __doc__: str

class PermissionDenied(Exception):
    __doc__: str

class RequestAborted(Exception):
    __doc__: str

class RequestDataTooBig(SuspiciousOperation):
    __doc__: str

class SuspiciousFileOperation(SuspiciousOperation):
    __doc__: str

class SuspiciousMultipartForm(SuspiciousOperation):
    __doc__: str

class SuspiciousOperation(Exception):
    __doc__: str

class TooManyFieldsSent(SuspiciousOperation):
    __doc__: str

class TooManyFilesSent(SuspiciousOperation):
    __doc__: str

class ValidationError(Exception):
    __doc__: str
    code: Any
    error_dict: dict
    error_list: list
    message: Any
    message_dict: Annotated[dict, 'property']
    messages: Annotated[Any, 'property']
    params: Any
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, message, code = ..., params = ...) -> None: ...
    def __iter__(self) -> Generator[tuple[Any, list], Any, None]: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def update_error_dict(self, error_dict: _T0) -> _T0: ...

class ViewDoesNotExist(Exception):
    __doc__: str
