import contextlib
import logging
import os
import pathlib
import shutil
import typing
from collections.abc import Callable
from urllib import request

from tqdm import tqdm

__all__ = ["download", "get_cache_dir"]


def get_cache_dir(cache_dir: str | pathlib.Path | None = None) -> pathlib.Path:
    """Return the given directory or the default cache directory.

    Parameters
    ----------
    cache_dir : str or pathlib.Path or None
        The desired cache directory

    Returns
    -------
    str
        The final cache directory path

    Raises
    ------
    OSError
        If the directory is not writable

    """
    if cache_dir is None:
        cache_dir = os.getenv("IOPATHLIB_CACHE", "~/.cache/iopathlib")
    cache_dir = pathlib.Path(cache_dir).expanduser()

    pathlib.Path.mkdir(cache_dir, parents=True, exist_ok=True)

    if not os.access(cache_dir, os.W_OK):
        msg = f"Cache directory {cache_dir} is not writable"
        raise OSError(msg)

    return cache_dir


def download(
    url: str,
    dir: str | pathlib.Path | os.PathLike,
    *,
    filename: str | None = None,
    progress: bool = True,
) -> pathlib.Path:
    """Download a file from a URL to a directory.

    Parameters
    ----------
    url : str
        The URL to download
    dir : str
        Destination directory
    filename : str, optional
        Filename to save as, uses the URL's name if not provided
    progress : bool
        Whether to display a progress bar

    Returns
    -------
    str
        The path to the downloaded file

    """
    dir = pathlib.Path(dir)
    dir.mkdir(parents=True, exist_ok=True)

    if filename is None:
        filename = url.split("/")[-1]
        if os.name == "nt" and "?" in filename:  # for windows
            filename = filename[: filename.index("?")]
        assert len(filename), f"Cannot obtain filename from url {url}"

    fpath = dir / filename
    logger = logging.getLogger(__name__)

    if fpath.is_file():
        logger.info("File %s exists! Skipping download.", filename)
        return fpath
    logger.info("Downloading: %s", url)

    tmp = fpath.with_suffix(fpath.suffix + ".tmp")

    def hook(t: typing.Any) -> Callable[[int, int, int | None], None]:
        last_b: list[int] = [0]

        def inner(b: int, bsize: int, tsize: int | None = None) -> None:
            if tsize is not None:
                t.total = tsize
            t.update((b - last_b[0]) * bsize)  # type: ignore
            last_b[0] = b

        return inner

    try:
        with tqdm(  # type: ignore
            unit="B",
            unit_scale=True,
            miniters=1,
            desc=filename,
            leave=True,
            disable=not progress,
        ) as t:
            tmp_str, _ = request.urlretrieve(url, filename=tmp, reporthook=hook(t))
        tmp = pathlib.Path(tmp_str)
        statinfo = tmp.stat()
        size = statinfo.st_size
        shutil.move(tmp, fpath)
    except OSError:
        logger.exception("Failed to download %s", url)
        raise
    finally:
        with contextlib.suppress(OSError):
            tmp.unlink(missing_ok=True)

    logger.info("Successfully downloaded %s (%d bytes)", fpath, size)
    return fpath
