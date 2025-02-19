# (generated with --quick)

import hashlib
import importmap.generator
import json
import logging
import os
import tomli
from marshmallow import fields
from typing import Any

DEFAULT_CONFIG_FILENAME: str
DEFAULT_LOCK_FILENAME: str
ImportmapGenerator: type[importmap.generator.ImportmapGenerator]
Schema: Any
logger: logging.Logger

class ConfigSchema(Any):
    packages: Any

class Importmap:
    config: Any
    config_filename: Any
    lock_filename: Any
    map: Any
    map_dev: Any
    def __init__(self, config_filename = ..., lock_filename = ...) -> None: ...
    def delete_lockfile(self) -> None: ...
    def generate_map(self, *args, **kwargs) -> Any: ...
    def load(self) -> None: ...
    def load_config(self) -> Any: ...
    def load_lockfile(self) -> Any: ...
    def save_lockfile(self, lockfile) -> None: ...

class LockfileSchema(Any):
    config_hash: Any
    importmap: Any
    importmap_dev: Any

class PackageSchema(Any):
    name: Any
    source: Any

def hash_for_data(data) -> str: ...
