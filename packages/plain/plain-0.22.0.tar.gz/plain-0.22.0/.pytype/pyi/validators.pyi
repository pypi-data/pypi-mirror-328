# (generated with --quick)

import ipaddress
import math
import pathlib
import re
import urllib.parse
from typing import Any, Callable, Iterable, Literal, Optional, TypeVar, Union, overload

BaseValidator: Any
DecimalValidator: Any
EMPTY_VALUES: tuple[None, str, list[nothing], tuple[()], dict[nothing, nothing]]
EmailValidator: Any
FileExtensionValidator: Any
MaxLengthValidator: Any
MaxValueValidator: Any
MinLengthValidator: Any
MinValueValidator: Any
Path: type[pathlib.Path]
ProhibitNullCharactersValidator: Any
RegexValidator: Any
StepValueValidator: Any
URLValidator: Any
ValidationError: Any
_lazy_re_compile: Any
deconstructible: Any
integer_validator: Any
ip_address_validator_map: dict[str, tuple[list[Callable[[Any], Any]], str]]
is_valid_ipv6_address: Any
pluralize_lazy: Any
punycode: Any
slug_re: Any
slug_unicode_re: Any
validate_comma_separated_integer_list: Any
validate_email: Any
validate_slug: Any
validate_unicode_slug: Any

AnyStr = TypeVar('AnyStr', str, bytes)

def get_available_image_extensions() -> list[str]: ...
def int_list_validator(sep = ..., message = ..., code = ..., allow_negative = ...) -> Any: ...
def ip_address_validators(protocol, unpack_ipv4) -> tuple[list[Callable[[Any], Any]], str]: ...
@overload
def urlsplit(url: str, scheme: str = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResult: ...
@overload
def urlsplit(url: Optional[bytes], scheme: Optional[Union[bytes, Literal['']]] = ..., allow_fragments: bool = ...) -> urllib.parse.SplitResultBytes: ...
@overload
def urlunsplit(components: Iterable[None]) -> Literal[b'']: ...
@overload
def urlunsplit(components: Iterable[Optional[AnyStr]]) -> AnyStr: ...
def validate_image_file_extension(value) -> Any: ...
def validate_integer(value) -> Any: ...
def validate_ipv46_address(value) -> None: ...
def validate_ipv4_address(value) -> None: ...
def validate_ipv6_address(value) -> None: ...
