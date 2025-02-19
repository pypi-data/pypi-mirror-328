# (generated with --quick)

import logging
import requests
from typing import Any, TypeVar

logger: logging.Logger

_TImportmapGenerator = TypeVar('_TImportmapGenerator', bound=ImportmapGenerator)

class ImportmapGenerator:
    development: Any
    provider: Any
    targets: Any
    def __init__(self, targets, development = ..., provider = ...) -> None: ...
    @classmethod
    def from_config(cls: type[_TImportmapGenerator], config, *args, **kwargs) -> _TImportmapGenerator: ...
    def generate(self) -> Any: ...
    def get_env(self) -> list[str]: ...

class ImportmapGeneratorError(Exception): ...
