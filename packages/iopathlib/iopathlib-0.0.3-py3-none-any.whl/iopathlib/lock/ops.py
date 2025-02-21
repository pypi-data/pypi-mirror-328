r"""OS-specific file locking ops."""

import os
import sys
import typing

from .. import _types
from ._exceptions import AlreadyLocked, LockException
from ._flags import LockFlags

__all__ = ["lock", "unlock"]


class HasFileno(typing.Protocol):
    """Protocol for objects that have a `fileno` method."""

    def fileno(self) -> int: ...


LOCKER: typing.Callable[[int | HasFileno, int], typing.Any] | None = None

if os.name == "nt":  # pragma: no cover
    import msvcrt

    import pywintypes
    import win32con
    import win32file
    import winerror

    LOCKER = win32file.LockFileEx  # pyright: ignore[reportConstantRedefinition]

    __overlapped = pywintypes.OVERLAPPED()

    def lock_win32(file_: _types.IO | int, flags: LockFlags) -> None:
        # Windows locking does not support locking through `fh.fileno()` so
        # we cast it to make mypy and pyright happy
        file_ = typing.cast(_types.IO, file_)

        mode = 0
        if flags & LockFlags.NON_BLOCKING:
            mode |= win32con.LOCKFILE_FAIL_IMMEDIATELY

        if flags & LockFlags.EXCLUSIVE:
            mode |= win32con.LOCKFILE_EXCLUSIVE_LOCK

        # Save the old position so we can go back to that position but
        # still lock from the beginning of the file
        savepos = file_.tell()
        if savepos:
            file_.seek(0)

        os_fh = msvcrt.get_osfhandle(file_.fileno())  # type: ignore[attr-defined]
        try:
            win32file.LockFileEx(os_fh, mode, 0, -0x10000, __overlapped)
        except pywintypes.error as exc_value:
            # error: (33, 'LockFileEx', 'The process cannot access the file
            # because another process has locked a portion of the file.')
            if exc_value.winerror == winerror.ERROR_LOCK_VIOLATION:
                raise AlreadyLocked(
                    LockException.LOCK_FAILED,
                    exc_value.strerror,
                    fh=file_,
                ) from exc_value
            # Q:  Are there exceptions/codes we should be dealing with
            # here?
            raise
        finally:
            if savepos:
                file_.seek(savepos)

    def unlock_win32(file_: _types.IO) -> None:
        try:
            savepos = file_.tell()
            if savepos:
                file_.seek(0)

            os_fh = msvcrt.get_osfhandle(file_.fileno())  # type: ignore[attr-defined]
            try:
                win32file.UnlockFileEx(
                    os_fh,
                    0,
                    -0x10000,
                    __overlapped,
                )
            except pywintypes.error as exc:
                if exc.winerror != winerror.ERROR_NOT_LOCKED:
                    # Q:  Are there exceptions/codes we should be
                    # dealing with here?
                    raise
            finally:
                if savepos:
                    file_.seek(savepos)
        except OSError as exc:
            raise LockException(
                LockException.LOCK_FAILED,
                exc.strerror,
                fh=file_,
            ) from exc

    def lock_msvcrt(file_: typing.IO, flags: LockFlags) -> None:
        if flags & LockFlags.SHARED:
            # For shared locks use win32file.LockFileEx.
            if sys.version_info.major == 2:
                mode = (
                    win32con.LOCKFILE_FAIL_IMMEDIATELY
                    if (flags & LockFlags.NON_BLOCKING)
                    else 0
                )
            else:
                mode = (
                    msvcrt.LK_NBRLCK
                    if (flags & LockFlags.NON_BLOCKING)
                    else msvcrt.LK_RLCK
                )
            hfile = win32file._get_osfhandle(file_.fileno())
            try:
                win32file.LockFileEx(hfile, mode, 0, -0x10000, __overlapped)
            except pywintypes.error as exc_value:
                if exc_value.winerror == winerror.ERROR_LOCK_VIOLATION:
                    raise LockException(
                        LockException.LOCK_FAILED,
                        exc_value.strerror,
                        fh=file_,
                    ) from exc_value
                raise
        else:
            # For exclusive locks, use msvcrt.locking.
            mode = msvcrt.LK_NBLCK if flags & LockFlags.NON_BLOCKING else msvcrt.LK_LOCK
            try:
                savepos = file_.tell()
                if savepos:
                    file_.seek(0)
                try:
                    msvcrt.locking(file_.fileno(), mode, lock_length)  # noqa: F821
                except OSError as exc_value:
                    raise LockException(  # noqa: B904
                        LockException.LOCK_FAILED,
                        exc_value.strerror,
                        fh=file_,
                    )
                finally:
                    if savepos:
                        file_.seek(savepos)
            except OSError as exc_value:
                raise LockException(  # noqa: B904
                    LockException.LOCK_FAILED,
                    exc_value.strerror,
                    fh=file_,
                )

    def unlock_msvcrt(file_: typing.IO) -> None:
        try:
            savepos = file_.tell()
            if savepos:
                file_.seek(0)
            try:
                msvcrt.locking(file_.fileno(), LockFlags.UNBLOCK, lock_length)  # noqa: F821
            except OSError as exc:
                exception = exc
                if exc.strerror == "Permission denied":
                    hfile = win32file._get_osfhandle(file_.fileno())
                    try:
                        win32file.UnlockFileEx(hfile, 0, -0x10000, __overlapped)
                    except pywintypes.error as exc:
                        exception = exc
                        if exc.winerror == winerror.ERROR_NOT_LOCKED:
                            # Silently ignore if already unlocked.
                            pass
                        else:
                            raise
                else:
                    raise LockException(  # noqa: B904
                        LockException.LOCK_FAILED,
                        exception.strerror,
                        fh=file_,
                    )
            finally:
                if savepos:
                    file_.seek(savepos)
        except OSError as exc:
            raise LockException(  # noqa: B904
                LockException.LOCK_FAILED,
                exc.strerror,
                fh=file_,
            )

    def lock(file: _types.IO, flags: LockFlags) -> None:
        assert LOCKER is not None, "We need a locking function in `LOCKER` "
        if win32file.LockFileEx == LOCKER:
            lock_win32(file, flags)
        else:
            lock_msvcrt(file, flags)

    def unlock(file: _types.IO) -> None:
        assert LOCKER is not None, "We need a locking function in `LOCKER` "
        if win32file.LockFileEx == LOCKER:
            unlock_win32(file)
        else:
            unlock_msvcrt(file)

elif os.name == "posix":  # pragma: no cover
    import errno
    import fcntl

    LOCKER = fcntl.flock  # pyright: ignore[reportConstantRedefinition]

    def lock(file: int | _types.IO, flags: LockFlags) -> None:  # type: ignore[misc]
        """Parameters
        ----------
        file: int | types.IO :

        flags: LockFlags :


        Returns
        -------

        """
        assert LOCKER is not None, "We need a locking function in `LOCKER` "
        # Locking with NON_BLOCKING without EXCLUSIVE or SHARED enabled
        # results in an error
        if (flags & LockFlags.NON_BLOCKING) and not flags & (
            LockFlags.SHARED | LockFlags.EXCLUSIVE
        ):
            msg = (
                "When locking in non-blocking mode the SHARED "
                "or EXCLUSIVE flag must be specified as well"
            )
            raise RuntimeError(
                msg,
            )

        try:
            LOCKER(file, flags)
        except OSError as exc_value:
            # Python can use one of several different exception classes to
            # represent timeout (most likely is BlockingIOError and IOError),
            # but these errors may also represent other failures. On some
            # systems, `IOError is OSError` which means checking for either
            # IOError or OSError can mask other errors.
            # The safest check is to catch OSError (from which the others
            # inherit) and check the errno (which should be EACCESS or EAGAIN
            # according to the spec).
            if exc_value.errno in (errno.EACCES, errno.EAGAIN):
                # A timeout exception, wrap this so the outer code knows to try
                # again (if it wants to).
                raise AlreadyLocked(
                    exc_value,
                    fh=file,
                ) from exc_value
            # Something else went wrong; don't wrap this so we stop
            # immediately.
            raise LockException(
                exc_value,
                fh=file,
            ) from exc_value
        except EOFError as exc_value:
            # On NFS filesystems, flock can raise an EOFError
            raise LockException(
                exc_value,
                fh=file,
            ) from exc_value

    def unlock(file: _types.IO) -> None:  # type: ignore[misc]
        """Parameters
        ----------
        file: types.IO :


        Returns
        -------

        """
        assert LOCKER is not None, "We need a locking function in `LOCKER` "
        LOCKER(file.fileno(), LockFlags.UNBLOCK)

else:  # pragma: no cover
    msg = "iopathlib.lock only defined for nt and posix platforms"
    raise RuntimeError(msg)
