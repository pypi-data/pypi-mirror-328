import tempfile
import typing

from ._base import PathHandler


class WebDAVOptions(typing.TypedDict):
    """Options to configure WebDAVPathHandler."""

    webdav_hostname: str
    webdav_login: str
    webdav_password: str


class WebDAVPathHandler(PathHandler):
    """PathHandler that uses WebDAV to access files.

    Parameters
    ----------
    webdav_options : dict

    """

    def __init__(self, webdav_options: WebDAVOptions):
        from webdav3.client import Client

        super().__init__()
        self.client = Client(webdav_options)

    @typing.override
    def _get_supported_prefixes(self) -> list[str]:
        return ["webdav://"]

    @typing.override
    def _open(
        self, path: str, mode: str = "r", buffering: int = -1, **kwargs: typing.Any,
    ) -> typing.IO[str] | typing.IO[bytes]:
        if mode not in ["r", "rb", "w", "wb"]:
            msg = f"Mode {mode} not supported for WebDAVPathHandler"
            raise ValueError(msg)

        local_path = self._download_to_local(path, mode)
        return open(local_path, mode, buffering, **kwargs)

    @typing.override
    def _exists(self, path: str, **kwargs: typing.Any) -> bool:
        return self.client.check(path)

    @typing.override
    def _isfile(self, path: str, **kwargs: typing.Any) -> bool:
        info = self.client.info(path)
        return info is not None and not info["isdir"]

    @typing.override
    def _isdir(self, path: str, **kwargs: typing.Any) -> bool:
        info = self.client.info(path)
        return info is not None and info["isdir"]

    def _listdir(self, path: str, **kwargs: typing.Any) -> list[str]:
        return [item["name"] for item in self.client.list(path)]

    def _download_to_local(self, path: str, mode: str) -> str:
        if "r" in mode:
            temp_dir = tempfile.mkdtemp()
            local_path = os.path.join(temp_dir, os.path.basename(path))
            self.client.download_file(remote_path=path, local_path=local_path)
            return local_path
        if "w" in mode:
            return os.path.join(tempfile.mkdtemp(), os.path.basename(path))
        return None

    def _upload_from_local(self, local_path: str, remote_path: str) -> None:
        self.client.upload_file(local_path=local_path, remote_path=remote_path)

    def _remove(self, path: str, **kwargs: typing.Any) -> None:
        self.client.clean(path)

    def _mkdir(self, path: str, **kwargs: typing.Any) -> None:
        self.client.mkdir(path)

