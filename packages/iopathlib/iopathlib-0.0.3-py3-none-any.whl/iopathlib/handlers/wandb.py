import os
import pathlib
import typing
from urllib.parse import urlparse

from .._file import get_cache_dir
from ..lock import file_lock
from ._base import PathHandler

type WandBArtifact = typing.Any


class WandBArtifactHandler(PathHandler):
    """Handles pulling artifacts from W&B using the API.

    Currently only supports reading.
    """

    def __new__(cls, **kwargs) -> None | typing.Self:
        import importlib.util

        if not importlib.util.find_spec("wandb"):
            return None

        return super().__new__(cls)

    def __init__(self, *, use_api: bool = True, use_run: bool = True):
        super().__init__()
        self.use_api = use_api
        self.use_run = use_run
        self.cache_map: dict[str, pathlib.Path] = {}

    def _parse_path(self, path: str) -> tuple[str, str | None]:
        """Format is one of the following:
        - wandb-artifact:///entity/project/name:version/file.h5
        - wandb-artifact:///entity/project/name:version
        - wandb-artifact://project/name:version/file.h5.

        Parameters
        ----------
        path: str :

            The path to the artifact.

        Returns
        -------

        tuple[str, str | None]
            A tuple containing the formatted name of the artifact and the file path if
            present.
        """
        url = urlparse(path)

        assert url.scheme == "wandb-artifact", f"Unsupported scheme {url.scheme!r}"

        # Spit by : to get name and combined version/file
        name, version_file = url.path.split(":")

        # Split by / to get version and filepath
        version, *maybe_file = version_file.split("/", 1)
        file = maybe_file[0] if len(maybe_file) > 0 else None

        if len(url.netloc) > 0:
            name = f"{url.netloc}/{name}"
        elif name.startswith("/"):
            name = name[1:]

        name = name.strip("/")
        name = name.replace("//", "/")
        name = f"{name}:{version}"

        # Name is the netloc + name, where netloc could be empty
        return name, file

    def _get_artifact(self, name: str) -> WandBArtifact:
        """Parameters
        ----------
        name: str :


        Returns
        -------

        """
        import wandb

        if self.use_run and wandb.run is not None:
            return wandb.run.use_artifact(name)
        if self.use_api:
            return wandb.Api().artifact(name)
        msg = "No W&B run or API available"
        raise RuntimeError(msg)

    @typing.override
    def _get_supported_prefixes(self) -> list[str]:
        return ["wandb-artifact://"]

    @typing.override
    def _get_local_path(
        self,
        path: str,
        mode: str = "r",
        force: bool = False,
        cache_dir: str | None = None,
        **kwargs,
    ):
        """Parameters
        ----------
        path: str :

        mode: str :
             (Default value = "r")
        force: bool :
             (Default value = False)
        cache_dir: str | None :
             (Default value = None)
        **kwargs :


        Returns
        -------

        """
        import wandb.errors

        path = os.fspath(path)

        self._check_kwargs(kwargs)

        assert mode in ("r",), f"Unsupported mode {mode!r}"

        if force or path not in self.cache_map or not self.cache_map[path].exists():
            name, file = self._parse_path(path)

            try:
                artifact = self._get_artifact(name)
            except wandb.errors.CommError as e:
                msg = f"Could not find artifact {name!r}"
                raise FileNotFoundError(msg) from e

            cache_path = get_cache_dir(cache_dir) / name
            with file_lock(cache_path):
                if not cache_path.exists() or force:
                    cache_path = artifact.download(cache_path)
                elif cache_path.is_file():
                    msg = f"A file exists at {cache_path!r}"
                    raise FileExistsError(msg)
            cache_path = cache_path / file if file is not None else cache_path

            self.cache_map[path] = cache_path
        return self.cache_map[path]

    @typing.override
    def _open(
        self,
        path: str,
        mode: str = "r",
        buffering: int = -1,
        **kwargs: typing.Any,
    ) -> typing.IO[str] | typing.IO[bytes]:
        """Open a remote HTTP path. The resource is first downloaded and cached
        locally.

        Parameters
        ----------
        path : str
            A URI supported by this PathHandler
        mode : str
            Specifies the mode in which the file is opened. It defaults
            to 'r'.
        buffering : int
            Not used for this PathHandler.
        path: str :

        mode: str :
             (Default value = "r")
        buffering: int :
             (Default value = -1)
        **kwargs: typing.Any :


        Returns
        -------
        file
            a file-like object.

        """
        self._check_kwargs(kwargs)

        if mode not in ("r",):
            msg = f"Unsupported mode {mode!r}"
            raise ValueError(msg)

        assert buffering == -1, (
            f"{self.__class__.__name__} does not support the `buffering` argument"
        )
        local_path = self._get_local_path(path, force=False)
        return open(local_path, mode)  # noqa: PTH123
