import os
import pathlib
import typing

from . import manager

__all__ = ("Path", "get_local_path", "join")

DEFAULT_MANAGER: typing.Final[manager.PathManager] = manager.PathManager()


class Path(type(pathlib.Path()) if not typing.TYPE_CHECKING else pathlib.Path):
    """Extends `pathlib.Path` to work with `iopathlib.file_io.PathManager`."""

    def __new__(
        cls,
        path: str | os.PathLike | pathlib.Path,
        *args,
        force: bool = False,
    ) -> pathlib.Path:
        if isinstance(path, pathlib.Path | pathlib.WindowsPath | pathlib.PosixPath):
            return path
        if isinstance(path, str):
            path = DEFAULT_MANAGER.get_local_path(path, force=force)
        return pathlib.Path(path, *args)

    # def __getattr__(self, name: str) -> typing.Any:
    #     """
    #     Forward all other attribute accesses to the underlying `pathlib.Path` object.
    #     """
    #     return getattr(Path, name)


def join(base: str | Path, *other: str | Path) -> str:
    """Joins paths using the path manager.

    Parameters
    ----------
    *paths : str
        The paths to join.

    Returns
    -------
    str
        The joined path.

    """
    base = str(base)
    return os.path.join(base, *map(str, other))


_exports: frozenset[str] = frozenset(
    fn_name for fn_name in dir(DEFAULT_MANAGER) if not fn_name.startswith("_")
)


def __getattr__(name: str):
    if name in _exports:
        return getattr(DEFAULT_MANAGER, name)
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)


def __dir__():
    return sorted(set(__all__) | _exports)


if __name__ == "__main__":
    # Generate the `.pyi` file if ran as main
    pass
