# (generated with --quick)

import re
import requests
import tomlkit
import vendor.exceptions
from typing import Any

APP_ASSETS_DIR: Any
UnknownContentTypeError: type[vendor.exceptions.UnknownContentTypeError]
VENDOR_DIR: Any
VersionMismatchError: type[vendor.exceptions.VersionMismatchError]

class Dependency:
    filename: Any
    installed: Any
    name: Any
    sourcemap: Any
    url: Any
    def __init__(self, name, **config) -> None: ...
    def __str__(self) -> str: ...
    def download(self, version) -> tuple[str, requests.models.Response]: ...
    def install(self) -> Any: ...
    @staticmethod
    def parse_version_from_url(url) -> str: ...
    def save_config(self) -> None: ...
    def update(self) -> Any: ...
    def vendor(self, response) -> Any: ...

def get_deps() -> list[Dependency]: ...
