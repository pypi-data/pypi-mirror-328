# (generated with --quick)

import builtins
import inspect
import os
import types
from typing import Any, Generator, Optional

CONFIG_MODULE_NAME: str
ImproperlyConfigured: Any
MODELS_MODULE_NAME: str
import_string: Any
module_has_submodule: Any

class PackageConfig:
    __doc__: str
    label: Any
    migrations_module: str
    models: Any
    models_module: Optional[builtins.module]
    module: Any
    name: str
    packages: None
    path: Any
    def __init__(self, package_name, package_module) -> None: ...
    def __repr__(self) -> str: ...
    def _path_from_module(self, module) -> Any: ...
    @classmethod
    def create(cls, entry) -> Any: ...
    def get_model(self, model_name, require_ready = ...) -> Any: ...
    def get_models(self, include_auto_created = ..., include_swapped = ...) -> Generator[Any, Any, None]: ...
    def import_models(self) -> None: ...
    def ready(self) -> None: ...

def import_module(name: str, package: Optional[str] = ...) -> types.ModuleType: ...
