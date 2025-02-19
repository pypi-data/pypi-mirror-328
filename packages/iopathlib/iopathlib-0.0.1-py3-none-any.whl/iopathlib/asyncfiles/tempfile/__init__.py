import asyncio
from functools import partial, singledispatch
from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOBase
from tempfile import NamedTemporaryFile as syncNamedTemporaryFile
from tempfile import SpooledTemporaryFile as syncSpooledTemporaryFile
from tempfile import TemporaryDirectory as syncTemporaryDirectory
from tempfile import TemporaryFile as syncTemporaryFile
from tempfile import _TemporaryFileWrapper as syncTemporaryFileWrapper

from ..base import AiofilesContextManager
from ..binary import AsyncBufferedIOBase, AsyncBufferedReader, AsyncFileIO
from ..text import AsyncTextIOWrapper
from .wrappers import AsyncSpooledTemporaryFile, AsyncTemporaryDirectory

__all__ = [
    "NamedTemporaryFile",
    "SpooledTemporaryFile",
    "TemporaryDirectory",
    "TemporaryFile",
]


# ================================================================
# Public methods for async open and return of temp file/directory
# objects with async interface
# ================================================================
def NamedTemporaryFile(
    mode="w+b",
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    delete=True,
    delete_on_close=True,
    loop=None,
    executor=None,
):
    """Async open a named temporary file.

    Parameters
    ----------
    mode :
         (Default value = "w+b")
    buffering :
         (Default value = -1)
    encoding :
         (Default value = None)
    newline :
         (Default value = None)
    suffix :
         (Default value = None)
    prefix :
         (Default value = None)
    dir :
         (Default value = None)
    delete :
         (Default value = True)
    delete_on_close :
         (Default value = True)
    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AiofilesContextManager(
        _temporary_file(
            named=True,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            newline=newline,
            suffix=suffix,
            prefix=prefix,
            dir=dir,
            delete=delete,
            delete_on_close=delete_on_close,
            loop=loop,
            executor=executor,
        ),
    )


def TemporaryFile(
    mode="w+b",
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    loop=None,
    executor=None,
):
    """Async open an unnamed temporary file.

    Parameters
    ----------
    mode :
         (Default value = "w+b")
    buffering :
         (Default value = -1)
    encoding :
         (Default value = None)
    newline :
         (Default value = None)
    suffix :
         (Default value = None)
    prefix :
         (Default value = None)
    dir :
         (Default value = None)
    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AiofilesContextManager(
        _temporary_file(
            named=False,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            newline=newline,
            suffix=suffix,
            prefix=prefix,
            dir=dir,
            loop=loop,
            executor=executor,
        ),
    )


def SpooledTemporaryFile(
    max_size=0,
    mode="w+b",
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    loop=None,
    executor=None,
):
    """Async open a spooled temporary file.

    Parameters
    ----------
    max_size :
         (Default value = 0)
    mode :
         (Default value = "w+b")
    buffering :
         (Default value = -1)
    encoding :
         (Default value = None)
    newline :
         (Default value = None)
    suffix :
         (Default value = None)
    prefix :
         (Default value = None)
    dir :
         (Default value = None)
    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AiofilesContextManager(
        _spooled_temporary_file(
            max_size=max_size,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            newline=newline,
            suffix=suffix,
            prefix=prefix,
            dir=dir,
            loop=loop,
            executor=executor,
        ),
    )


def TemporaryDirectory(suffix=None, prefix=None, dir=None, loop=None, executor=None):
    """Async open a temporary directory.

    Parameters
    ----------
    suffix :
         (Default value = None)
    prefix :
         (Default value = None)
    dir :
         (Default value = None)
    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    return AiofilesContextManagerTempDir(
        _temporary_directory(
            suffix=suffix,
            prefix=prefix,
            dir=dir,
            loop=loop,
            executor=executor,
        ),
    )


# =========================================================
# Internal coroutines to open new temp files/directories
# =========================================================
async def _temporary_file(
    named=True,
    mode="w+b",
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    delete=True,
    delete_on_close=True,
    loop=None,
    executor=None,
    max_size=0,
):
    """Async method to open a temporary file with async interface."""
    if loop is None:
        loop = asyncio.get_running_loop()

    if named:
        cb = partial(
            syncNamedTemporaryFile,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            newline=newline,
            suffix=suffix,
            prefix=prefix,
            dir=dir,
            delete=delete,
            delete_on_close=delete_on_close,
        )
    else:
        cb = partial(
            syncTemporaryFile,
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            newline=newline,
            suffix=suffix,
            prefix=prefix,
            dir=dir,
        )

    f = await loop.run_in_executor(executor, cb)

    # Wrap based on type of underlying IO object
    if type(f) is syncTemporaryFileWrapper:
        # _TemporaryFileWrapper was used (named files)
        result = wrap(f.file, f, loop=loop, executor=executor)
        result._closer = f._closer
        return result
    # IO object was returned directly without wrapper
    return wrap(f, f, loop=loop, executor=executor)


async def _spooled_temporary_file(
    max_size=0,
    mode="w+b",
    buffering=-1,
    encoding=None,
    newline=None,
    suffix=None,
    prefix=None,
    dir=None,
    loop=None,
    executor=None,
):
    """Open a spooled temporary file with async interface."""
    if loop is None:
        loop = asyncio.get_running_loop()

    cb = partial(
        syncSpooledTemporaryFile,
        max_size=max_size,
        mode=mode,
        buffering=buffering,
        encoding=encoding,
        newline=newline,
        suffix=suffix,
        prefix=prefix,
        dir=dir,
    )

    f = await loop.run_in_executor(executor, cb)

    # Single interface provided by SpooledTemporaryFile for all modes
    return AsyncSpooledTemporaryFile(f, loop=loop, executor=executor)


async def _temporary_directory(
    suffix=None,
    prefix=None,
    dir=None,
    loop=None,
    executor=None,
):
    """Async method to open a temporary directory with async interface."""
    if loop is None:
        loop = asyncio.get_running_loop()

    cb = partial(syncTemporaryDirectory, suffix, prefix, dir)
    f = await loop.run_in_executor(executor, cb)

    return AsyncTemporaryDirectory(f, loop=loop, executor=executor)


class AiofilesContextManagerTempDir(AiofilesContextManager):
    """With returns the directory location, not the object (matching sync lib)."""

    async def __aenter__(self):
        self._obj = await self._coro
        return self._obj.name


@singledispatch
def wrap(base_io_obj, file, *, loop=None, executor=None):
    """Wrap the object with interface based on type of underlying IO.

    Parameters
    ----------
    base_io_obj :

    file :

    * :

    loop :
         (Default value = None)
    executor :
         (Default value = None)

    Returns
    -------

    """
    msg = f"Unsupported IO type: {base_io_obj}"
    raise TypeError(msg)


@wrap.register(TextIOBase)
def _(base_io_obj, file, *, loop=None, executor=None):
    """Parameters
    ----------
    base_io_obj :

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
def _(base_io_obj, file, *, loop=None, executor=None):
    """Parameters
    ----------
    base_io_obj :

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
def _(base_io_obj, file, *, loop=None, executor=None):
    """Parameters
    ----------
    base_io_obj :

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
def _(base_io_obj, file, *, loop=None, executor=None):
    """Parameters
    ----------
    base_io_obj :

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
