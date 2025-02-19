import os
import pathlib


def get_cache_dir(cache_dir: str | pathlib.Path | None = None) -> str:
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

    return str(cache_dir)
