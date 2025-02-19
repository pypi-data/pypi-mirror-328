# (generated with --quick)

import io
import os
from typing import Any, Never, Optional, TypeVar

BytesIO: type[io.BytesIO]
InMemoryUploadedFile: Any
TemporaryUploadedFile: Any
__all__: list[str]
import_string: Any
settings: Any

_T0 = TypeVar('_T0')

class FileUploadHandler:
    __doc__: str
    charset: Any
    chunk_size: int
    content_length: Any
    content_type: Any
    content_type_extra: Any
    field_name: Any
    file_name: Any
    request: Any
    def __init__(self, request = ...) -> None: ...
    def file_complete(self, file_size) -> Never: ...
    def handle_raw_input(self, input_data, META, content_length, boundary, encoding = ...) -> None: ...
    def new_file(self, field_name, file_name, content_type, content_length, charset = ..., content_type_extra = ...) -> None: ...
    def receive_data_chunk(self, raw_data, start) -> Never: ...
    def upload_complete(self) -> None: ...
    def upload_interrupted(self) -> None: ...

class MemoryFileUploadHandler(FileUploadHandler):
    __doc__: str
    activated: Any
    charset: None
    content_length: Any
    content_type: Any
    content_type_extra: None
    field_name: Any
    file: io.BytesIO
    file_name: Any
    request: Any
    def file_complete(self, file_size) -> Any: ...
    def handle_raw_input(self, input_data, META, content_length, boundary, encoding = ...) -> None: ...
    def new_file(self, *args, **kwargs) -> None: ...
    def receive_data_chunk(self, raw_data: _T0, start) -> Optional[_T0]: ...

class SkipFile(UploadFileException):
    __doc__: str

class StopFutureHandlers(UploadFileException):
    __doc__: str

class StopUpload(UploadFileException):
    __doc__: str
    connection_reset: Any
    def __init__(self, connection_reset = ...) -> None: ...
    def __str__(self) -> str: ...

class TemporaryFileUploadHandler(FileUploadHandler):
    __doc__: str
    charset: None
    content_length: Any
    content_type: Any
    content_type_extra: None
    field_name: Any
    file: Any
    file_name: Any
    request: Any
    def file_complete(self, file_size) -> Any: ...
    def new_file(self, *args, **kwargs) -> None: ...
    def receive_data_chunk(self, raw_data, start) -> None: ...
    def upload_interrupted(self) -> None: ...

class UploadFileException(Exception):
    __doc__: str

def load_handler(path, *args, **kwargs) -> Any: ...
