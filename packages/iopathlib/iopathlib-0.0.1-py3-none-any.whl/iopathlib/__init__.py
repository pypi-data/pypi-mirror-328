"""Lazy configuration system, inspired by and based on Detectron2 and Hydra."""

from . import _path, asyncfiles, cli, lock, manager, reader, types
from ._api import *
from ._cache import *
from ._download import *
from ._path import *


def __getattr__(name: str):
    from importlib.metadata import PackageNotFoundError, version

    match name:
        case "__version__":
            try:
                return version(__name__)
            except PackageNotFoundError:
                return "unknown"
        case _:
            pass
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)
