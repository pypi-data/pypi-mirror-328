import importlib.metadata
import importlib.resources
import shutil
import tempfile
import typing
from pathlib import Path as _PathlibPath
from urllib.parse import urlparse

import typing_extensions as TX

from . import PathHandler


class MetadataPathHandler(PathHandler):
    """PathHandler that uses a package's metadata (entry point) to get the path.

    Parameters
    ----------
    prefix : str
        The prefix to use for this path handler.
    group : str
        The name of the entry point group to use.

    Returns
    -------

    Raises
    ------
    ValueError
        If the environment variable is not defined and no default is provided.

    Examples
    --------
    >>> import mymodel  # is some package with 'unipercept.configs' entry point metadata
    >>> handler = MetadataPathHandler("configs://", "unipercept.configs")
    >>> handler.get_local_path("configs://mymodel/cityscapes/resnet50.py")
    '/path/to/install/cityscapes/resnet50.py'
    """

    def __init__(self, prefix: str, group: str):
        self._tmp = tempfile.TemporaryDirectory()

        assert prefix.endswith("://"), f"Prefix {prefix!r} must end with '://'"

        self.PREFIX: typing.Final = prefix
        self.GROUP: typing.Final = group
        self.LOCAL = self._tmp.name

    def __del__(self):
        if self._tmp is not None:
            print(f"Removing temporary directory {self.PREFIX!r} at {self.LOCAL!r}")
            self._tmp.cleanup()

    @typing.override
    def _get_supported_prefixes(self):
        """ """
        return [self.PREFIX]

    def _get_path(self, path: str, **kwargs) -> _PathlibPath:
        """r"""Return the local path (in the temporary directory) for the given path.

        Parameters
        ----------
        path: str :
            
        **kwargs :
            

        Returns
        -------
        with importlib.resources.as_file(self._get_traversable(path)) as ph:
            if not ph.is_file():
                raise FileNotFoundError(f"File {path!r} is not a file! Got: {ph!r}")
            local_path = _PathlibPath(self.LOCAL) / path[len(self.PREFIX) :]
            local_path.parent.mkdir(parents=True, exist_ok=True)
            if local_path.exists():
                local_path.unlink()
            shutil.copy(ph, local_path)
        return local_path

    def _get_traversable(self, path: str, **kwargs) -> _PathlibPath:
        """r"""Return the `importlib.resources` traversable object for the given path.

        Parameters
        ----------
        path: str :
            
        **kwargs :
            

        Returns
        -------
        url = urlparse(path)
        assert url.scheme == self.PREFIX.rstrip("://"), (
            f"Unsupported scheme {url.scheme!r}"
        )
        pkg_available = importlib.metadata.entry_points(group=self.GROUP)
        pkg_req = url.netloc

        for pkg in pkg_available:
            if pkg.name == pkg_req:
                break
        else:
            msg = f"Package {pkg_req!r} not found in group {self.GROUP!r}. Available packages: {pkg_available}"
            raise ValueError(msg)

        pkg_files = importlib.resources.files(pkg.value).joinpath(url.path.lstrip("/"))

        return pkg_files

    @typing.override
    def _get_local_path(self, path: str, **kwargs):
        """

        Parameters
        ----------
        path: str :
            
        **kwargs :
            

        Returns
        -------

        """
        return str(self._get_path(path, **kwargs))

    @typing.override
    def _isfile(self, path: str, **kwargs: typing.Any) -> bool:
        """

        Parameters
        ----------
        path: str :
            
        **kwargs: typing.Any :
            

        Returns
        -------

        """
        return self._get_path(path, **kwargs).is_file()

    @typing.override
    def _isdir(self, path: str, **kwargs: typing.Any) -> bool:
        """

        Parameters
        ----------
        path: str :
            
        **kwargs: typing.Any :
            

        Returns
        -------

        """
        return self._get_path(path, **kwargs).is_dir()

    @typing.override
    def _ls(self, path: str, **kwargs: typing.Any) -> list[str]:
        """

        Parameters
        ----------
        path: str :
            
        **kwargs: typing.Any :
            

        Returns
        -------

        """
        msg = f"Listing directories is not supported for {self.__class__.__name__}"
        raise NotImplementedError(msg)

    @typing.override
    def _open(self, path: str, mode="r", **kwargs):
        """

        Parameters
        ----------
        path: str :
            
        mode :
             (Default value = "r")
        **kwargs :
            

        Returns
        -------

        """
        assert "w" not in mode, (
            f"Mode {mode!r} not supported for {self.__class__.__name__}"
        )
        return self._get_traversable(path).open(mode, **kwargs)
