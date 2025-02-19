import contextlib
import logging
import os
import shutil
from collections.abc import Callable
from urllib import request


def download(
    url: str, dir: str, *, filename: str | None = None, progress: bool = True,
) -> str:
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
    os.makedirs(dir, exist_ok=True)
    if filename is None:
        filename = url.split("/")[-1]
        if os.name == "nt" and "?" in filename:  # for windows
            filename = filename[: filename.index("?")]
        assert len(filename), f"Cannot obtain filename from url {url}"
    fpath = os.path.join(dir, filename)
    logger = logging.getLogger(__name__)

    if os.path.isfile(fpath):
        logger.info(f"File {filename} exists! Skipping download.")
        return fpath

    tmp = fpath + ".tmp"  # download to a tmp file first, to be more atomic.
    try:
        logger.info(f"Downloading from {url} ...")
        if progress:
            import tqdm

            def hook(t: tqdm.tqdm) -> Callable[[int, int, int | None], None]:
                last_b: list[int] = [0]

                def inner(b: int, bsize: int, tsize: int | None = None) -> None:
                    if tsize is not None:
                        t.total = tsize
                    t.update((b - last_b[0]) * bsize)  # type: ignore
                    last_b[0] = b

                return inner

            with tqdm.tqdm(  # type: ignore
                unit="B", unit_scale=True, miniters=1, desc=filename, leave=True,
            ) as t:
                tmp, _ = request.urlretrieve(url, filename=tmp, reporthook=hook(t))

        else:
            tmp, _ = request.urlretrieve(url, filename=tmp)
        statinfo = os.stat(tmp)
        size = statinfo.st_size
        if size == 0:
            msg = f"Downloaded an empty file from {url}!"
            raise OSError(msg)
        # download to tmp first and move to fpath, to make this function more
        # atomic.
        shutil.move(tmp, fpath)
    except OSError:
        logger.exception(f"Failed to download {url}")
        raise
    finally:
        with contextlib.suppress(OSError):
            os.unlink(tmp)

    logger.info("Successfully downloaded " + fpath + ". " + str(size) + " bytes.")
    return fpath
