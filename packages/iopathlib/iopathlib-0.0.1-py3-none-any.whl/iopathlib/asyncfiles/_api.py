"""Handle files using a thread pool executor."""

import asyncio
import sys
from functools import partial, singledispatch
from io import (
    BufferedIOBase,
    BufferedRandom,
    BufferedReader,
    BufferedWriter,
    FileIO,
    TextIOBase,
)

from .base import AiofilesContextManager
from .binary import (
    AsyncBufferedIOBase,
    AsyncBufferedReader,
    AsyncFileIO,
    AsyncIndirectBufferedIOBase,
)
from .text import AsyncTextIndirectIOWrapper, AsyncTextIOWrapper

sync_open = open

__all__ = (
    "open",
    "stderr",
    "stderr_bytes",
    "stdin",
    "stdin_bytes",
    "stdout",
    "stdout_bytes",
)


def open(
    file,
    mode="r",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
    *,
    loop=None,
    executor=None,
):
    """Parameters
    ----------
    file :

    mode :
         (Default value = "r")
    buffering :
         (Default value = -1)
    encoding :
         (Default value = None)
    errors :
         (Default value = None)
    newline :
         (Default value = None)
    closefd :
         (Default value = True)
    opener :
         (Default value = None)
    * :

    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AiofilesContextManager(
        _open(
            file,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            newline=newline,
            closefd=closefd,
            opener=opener,
            loop=loop,
            executor=executor,
        ),
    )


async def _open(
    file,
    mode="r",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
    *,
    loop=None,
    executor=None,
):
    """Open an asyncio file."""
    if loop is None:
        loop = asyncio.get_running_loop()
    cb = partial(
        sync_open,
        file,
        mode=mode,
        buffering=buffering,
        encoding=encoding,
        errors=errors,
        newline=newline,
        closefd=closefd,
        opener=opener,
    )
    f = await loop.run_in_executor(executor, cb)

    return wrap(f, loop=loop, executor=executor)


@singledispatch
def wrap(file, *, loop=None, executor=None):
    """Parameters
    ----------
    file :

    * :

    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    msg = f"Unsupported io type: {file}."
    raise TypeError(msg)


@wrap.register(TextIOBase)
def _(file, *, loop=None, executor=None):
    """Parameters
    ----------
    file :

    * :

    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AsyncTextIOWrapper(file, loop=loop, executor=executor)


@wrap.register(BufferedWriter)
@wrap.register(BufferedIOBase)
def _(file, *, loop=None, executor=None):
    """Parameters
    ----------
    file :

    * :

    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AsyncBufferedIOBase(file, loop=loop, executor=executor)


@wrap.register(BufferedReader)
@wrap.register(BufferedRandom)
def _(file, *, loop=None, executor=None):
    """Parameters
    ----------
    file :

    * :

    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AsyncBufferedReader(file, loop=loop, executor=executor)


@wrap.register(FileIO)
def _(file, *, loop=None, executor=None):
    """Parameters
    ----------
    file :

    * :

    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AsyncFileIO(file, loop=loop, executor=executor)


stdin = AsyncTextIndirectIOWrapper("sys.stdin", None, None, indirect=lambda: sys.stdin)
stdout = AsyncTextIndirectIOWrapper(
    "sys.stdout", None, None, indirect=lambda: sys.stdout,
)
stderr = AsyncTextIndirectIOWrapper(
    "sys.stderr", None, None, indirect=lambda: sys.stderr,
)
stdin_bytes = AsyncIndirectBufferedIOBase(
    "sys.stdin.buffer", None, None, indirect=lambda: sys.stdin.buffer,
)
stdout_bytes = AsyncIndirectBufferedIOBase(
    "sys.stdout.buffer", None, None, indirect=lambda: sys.stdout.buffer,
)
stderr_bytes = AsyncIndirectBufferedIOBase(
    "sys.stderr.buffer", None, None, indirect=lambda: sys.stderr.buffer,
)
