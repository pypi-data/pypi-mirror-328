import logging
import os
import typing
from collections import OrderedDict
from collections.abc import Callable, MutableMapping
from io import IOBase
from typing import Any, overload

from . import handlers


class PathManager:
    """A class to open or translate paths."""

    def __init__(self) -> None:
        self._path_handlers: MutableMapping[str, handlers.PathHandler] = OrderedDict()
        """
        Dict from path prefix to handler.
        """

        self._native_path_handler: handlers.PathHandler = handlers.OSPathHandler()
        """
        A OSPathHandler that works on posix paths. This is used as the fallback.
        """

        self._cwd: str | None = None
        """
        Keeps track of the single cwd (if set).
        NOTE: Only one handlers.PathHandler can have a cwd set at a time.
        """

        self._async_handlers: set[handlers.PathHandler] = set()
        """
        Keeps track of the handlers.PathHandler subclasses where `opena` was used so
        all of the threads can be properly joined when calling
        `PathManager.join`.
        """

        self._enable_logging = True
        """
        Flag for enabling / disabling telemetry.
        """

    def __get_path_handler(self, path: str | os.PathLike) -> handlers.PathHandler:
        """Find a handler for the provided path.

        Parameters
        ----------
        path : str or os.PathLike
            URI path to resource

        Returns
        -------
        handlers.PathHandler
            Handler for this path

        """
        path = os.fspath(path)
        for p, handler in self._path_handlers.items():
            if path.startswith(p):
                return handler
        return self._native_path_handler

    @overload
    def open(
        self,
        path: str,
        mode: typing.Literal["rb", "wb", "ab", "xb", "r+b", "w+b", "a+b", "x+b"] = ...,
        buffering: int = ...,
        **kwargs: Any,
    ) -> typing.IO[bytes]: ...

    @overload
    def open(
        self,
        path: str,
        mode: typing.Literal[
            "r", "w", "a", "x", "r+", "w+", "a+", "x+", "rt", "wt",
        ] = ...,
        buffering: int = ...,
        **kwargs: Any,
    ) -> typing.IO[str]: ...

    def open(
        self,
        path: str,
        mode: str = "r",
        buffering: int = -1,
        **kwargs: Any,
    ) -> typing.IO[str] | typing.IO[bytes]:
        handler = self.__get_path_handler(path)
        return handler._open(path, mode, buffering=buffering, **kwargs)  # type: ignore

    def opena(
        self,
        path: str,
        mode: str = "r",
        buffering: int = -1,
        callback_after_file_close: Callable[[None], None] | None = None,
        **kwargs: Any,
    ) -> IOBase:
        """Open a file asynchronously.

        Parameters
        ----------
        path : str

        mode : str

        buffering : int

        callback_after_file_close : Optional[Callable]
            Called after close, if in write mode
        path: str :

        mode: str :
             (Default value = "r")
        buffering: int :
             (Default value = -1)
        callback_after_file_close: Optional[Callable[[None] :

        None]] :
             (Default value = None)
        **kwargs: Any :


        Returns
        -------


        """
        if "w" in mode:
            kwargs["callback_after_file_close"] = callback_after_file_close
            kwargs["buffering"] = buffering
        non_blocking_io = self.__get_path_handler(path)._opena(
            path,
            mode,
            **kwargs,
        )
        if "w" in mode:
            # Keep track of the path handlers where `opena` is used so that all of the
            # threads can be properly joined on `PathManager.join`.
            self._async_handlers.add(self.__get_path_handler(path))
        return non_blocking_io

    def async_join(self, *paths: str, **kwargs: Any) -> bool:
        """Wait for asynchronous writes to finish.

        Parameters
        ----------
        *paths : str
            File paths to wait on
        *paths: str :

        **kwargs: Any :


        Returns
        -------


        """
        success = True
        if not paths:  # Join all.
            for handler in self._async_handlers:
                success = handler._async_join(**kwargs) and success
        else:  # Join specific paths.
            for path in paths:
                success = (
                    self.__get_path_handler(path)._async_join(path, **kwargs)
                    and success
                )
        return success

    def async_close(self, **kwargs: Any) -> bool:
        """Close all asynchronous I
        O threads.

        Parameters
        ----------
        **kwargs: Any :


        Returns
        -------


        """
        success = self.async_join(**kwargs)
        for handler in self._async_handlers:
            success = handler._async_close(**kwargs) and success
        self._async_handlers.clear()
        return success

    def copy(
        self,
        src_path: str,
        dst_path: str,
        overwrite: bool = False,
        **kwargs: Any,
    ) -> bool:
        """Copy a file from source to destination.

        Parameters
        ----------
        src_path : str

        dst_path : str

        overwrite : bool

        src_path: str :

        dst_path: str :

        overwrite: bool :
             (Default value = False)
        **kwargs: Any :


        Returns
        -------


        """
        if self.__get_path_handler(src_path) != self.__get_path_handler(  # type: ignore
            dst_path,
        ):
            return self._copy_across_handlers(src_path, dst_path, overwrite, **kwargs)

        handler = self.__get_path_handler(src_path)
        return handler._copy(src_path, dst_path, overwrite, **kwargs)

    def mv(self, src_path: str, dst_path: str, **kwargs: Any) -> bool:
        """Move
        rename) a source path to a destination.

        Parameters
        ----------
        src_path : str

        dst_path : str

        src_path: str :

        dst_path: str :

        **kwargs: Any :


        Returns
        -------


        """
        # Moving across handlers is not supported.
        assert self.__get_path_handler(  # type: ignore
            src_path,
        ) == self.__get_path_handler(dst_path), (
            "Src and dest paths must be supported by the same path handler."
        )
        handler = self.__get_path_handler(src_path)
        return handler._mv(src_path, dst_path, **kwargs)

    def get_local_path(self, path: str, force: bool = False, **kwargs: Any) -> str:
        """Get a local file path.

        Parameters
        ----------
        path : str

        force : bool

        path: str :

        force: bool :
             (Default value = False)
        **kwargs: Any :


        Returns
        -------


        """
        path = os.fspath(path)
        handler = self.__get_path_handler(path)  # type: ignore
        try:
            bret = handler._get_local_path(path, force=force, **kwargs)
        except TypeError:
            bret = handler._get_local_path(path, **kwargs)
        return bret

    def copy_from_local(
        self,
        local_path: str,
        dst_path: str,
        overwrite: bool = False,
        **kwargs: Any,
    ) -> bool:
        """Copy a local file to a destination URI.

        Parameters
        ----------
        local_path : str

        dst_path : str

        overwrite : bool

        local_path: str :

        dst_path: str :

        overwrite: bool :
             (Default value = False)
        **kwargs: Any :


        Returns
        -------


        """
        assert os.path.exists(local_path), f"local_path = {local_path}"
        handler = self.__get_path_handler(dst_path)

        return handler._copy_from_local(
            local_path=local_path,
            dst_path=dst_path,
            overwrite=overwrite,
            **kwargs,
        )

    def exists(self, path: str, **kwargs: Any) -> bool:
        """Check if a resource exists at the given URI.

        Parameters
        ----------
        path : str

        path: str :

        **kwargs: Any :


        Returns
        -------


        """
        handler = self.__get_path_handler(path)
        return handler._exists(path, **kwargs)  # type: ignore

    def isfile(self, path: str, **kwargs: Any) -> bool:
        """Check if the resource at the given URI is a file.

        Parameters
        ----------
        path : str

        path: str :

        **kwargs: Any :


        Returns
        -------


        """
        handler = self.__get_path_handler(path)
        return handler._isfile(path, **kwargs)  # type: ignore

    def isdir(self, path: str, **kwargs: Any) -> bool:
        """Check if the resource at the given URI is a directory."""
        handler = self.__get_path_handler(path)
        return handler._isdir(path, **kwargs)  # type: ignore

    def ls(self, path: str, **kwargs: Any) -> list[str]:
        """List the contents of a directory."""
        return self.__get_path_handler(path)._ls(path, **kwargs)

    def mkdirs(self, path: str, **kwargs: Any) -> None:
        """Create directories recursively."""
        handler = self.__get_path_handler(path)
        return handler._mkdirs(path, **kwargs)  # type: ignore

    def rm(self, path: str, **kwargs: Any) -> None:
        """Remove a file."""
        handler = self.__get_path_handler(path)
        return handler._rm(path, **kwargs)  # type: ignore

    def symlink(self, src_path: str, dst_path: str, **kwargs: Any) -> bool:
        """Create a symlink from src_path to dst_path."""
        # Copying across handlers is not supported.
        assert self.__get_path_handler(  # type: ignore
            src_path,
        ) == self.__get_path_handler(dst_path)
        handler = self.__get_path_handler(src_path)
        return handler._symlink(src_path, dst_path, **kwargs)  # type: ignore

    def set_cwd(self, path: str | None, **kwargs: Any) -> bool:
        """Set the current working directory."""
        if path is None and self._cwd is None:
            return True
        if self.__get_path_handler(path or self._cwd)._set_cwd(path, **kwargs):  # type: ignore
            self._cwd = path
            bret = True
        else:
            bret = False
        return bret

    def register_handler(
        self,
        handler: handlers.PathHandler,
        allow_override: bool = True,
    ) -> None:
        """Register a path handler."""
        logger = logging.getLogger(__name__)
        assert isinstance(handler, handlers.PathHandler), handler

        # Allow override of `OSPathHandler` which is automatically
        # instantiated by `PathManager`.
        if isinstance(handler, OSPathHandler):
            if allow_override:
                self._native_path_handler = handler
            else:
                msg = (
                    "`OSPathHandler` is registered by default. Use the "
                    "`allow_override=True` kwarg to override it."
                )
                raise ValueError(
                    msg,
                )
            return

        for prefix in handler._get_supported_prefixes():
            if prefix not in self._path_handlers:
                self._path_handlers[prefix] = handler
                continue

            old_handler_type = type(self._path_handlers[prefix])
            if allow_override:
                # if using the global PathManager, show the warnings
                global g_pathmgr
                if self == g_pathmgr:
                    logger.warning(
                        f"[PathManager] Attempting to register prefix '{prefix}' from "
                        "the following call stack:\n"
                        + "".join(traceback.format_stack(limit=5)),
                        # show the most recent callstack
                    )
                    logger.warning(
                        f"[PathManager] Prefix '{prefix}' is already registered "
                        f"by {old_handler_type}. We will override the old handler. "
                        "To avoid such conflicts, create a project-specific PathManager "
                        "instead.",
                    )
                self._path_handlers[prefix] = handler
            else:
                msg = f"[PathManager] Prefix '{prefix}' already registered by {old_handler_type}!"
                raise KeyError(
                    msg,
                )

        # Sort path handlers in reverse order so longer prefixes take priority,
        # eg: http://foo/bar before http://foo
        self._path_handlers = OrderedDict(
            sorted(self._path_handlers.items(), key=lambda t: t[0], reverse=True),
        )

    def set_strict_kwargs_checking(self, enable: bool) -> None:
        """Toggle strict kwargs checking.

        Parameters
        ----------
        enable: bool :


        Returns
        -------


        """
        self._native_path_handler._strict_kwargs_check = enable
        for handler in self._path_handlers.values():
            handler._strict_kwargs_check = enable

    def set_logging(self, enable_logging=True):
        """Parameters
        ----------
        enable_logging :
             (Default value = True)

        Returns
        -------

        """
        self._enable_logging = enable_logging

    def _copy_across_handlers(
        self,
        src_path: str,
        dst_path: str,
        overwrite: bool,
        **kwargs: Any,
    ) -> bool:
        src_handler = self.__get_path_handler(src_path)
        assert src_handler._get_local_path is not None
        dst_handler = self.__get_path_handler(dst_path)
        assert dst_handler._copy_from_local is not None

        local_file = src_handler._get_local_path(src_path, **kwargs)

        return dst_handler._copy_from_local(
            local_file,
            dst_path,
            overwrite=overwrite,
            **kwargs,
        )
