"""
IOPathlib.
=========

This is the standalone version of the `unipercept.fileio` module. It was refactored
such that it can be installed independently of the `unipercept` package.

"""

from . import cli, lock, manager
from ._default import *
from ._file import *
from ._path import *
from ._types import *


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
