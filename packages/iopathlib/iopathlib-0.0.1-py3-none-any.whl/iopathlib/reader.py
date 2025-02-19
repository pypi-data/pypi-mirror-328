from collections.abc import Callable
from io import IOBase
from types import TracebackType
from typing import Any

import iopathlib.asyncfiles
import iopathlib.lock

__all__ = ["NativeAsyncReader"]


class NativeAsyncReader(IOBase):
    """Reads a file asynchronously on the native file system."""

    def __init__(
        self,
        path: str,
        mode: str,
        buffering: int,
        callback_after_file_close: Callable[[None], None] | None = None,
        **kwargs: Any,
    ) -> None:
        self._path = path
        self._mode = mode
        self._buffering = buffering
        self._callback_after_file_close = callback_after_file_close
        self._kwargs: Any = kwargs

    async def read(self) -> bytes | str:
        async with iopathlib.asyncfiles.open(
            file=self._path,
            mode=self._mode,
            buffering=self._buffering,
            **self._kwargs,
        ) as fp:
            return await fp.read()

    def write(self) -> None:
        raise NotImplementedError()

    def readable(self) -> bool:
        return True

    def writable(self) -> bool:
        return False

    def __enter__(self) -> "NativeAsyncReader":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        pass
