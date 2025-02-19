import os
from collections.abc import Callable


class LazyPath(os.PathLike):
    """A path that's lazily evaluated when it's used.

    Users should be careful to not use it like a str, because
    it behaves differently from a str.
    Path manipulation functions in Python such as `os.path.*` all accept
    PathLike objects already.

    It can be materialized to a str using `os.fspath`.
    """

    KEPT_ATTRIBUTES = ["__getstate__", "__setstate__"]

    def __init__(self, func: Callable[[], str]) -> None:
        self._func = func
        self._value: str | None = None

    def _get_value(self) -> str:
        if self._value is None:
            self._value = self._func()
        return self._value

    def __fspath__(self) -> str:
        return self._get_value()

    # behave more like a str after evaluated
    def __getattr__(self, name: str):  # type: ignore
        if name in LazyPath.KEPT_ATTRIBUTES:
            return super().__getattr__(name)
        if self._value is None:
            msg = f"Uninitialized LazyPath has no attribute: {name}."
            raise AttributeError(msg)
        return getattr(self._value, name)

    def __getitem__(self, key):  # type: ignore
        if self._value is None:
            msg = "Uninitialized LazyPath is not subscriptable."
            raise TypeError(msg)
        return self._value[key]  # type: ignore

    def __str__(self) -> str:
        if self._value is not None:
            return self._value  # type: ignore
        return super().__str__()

