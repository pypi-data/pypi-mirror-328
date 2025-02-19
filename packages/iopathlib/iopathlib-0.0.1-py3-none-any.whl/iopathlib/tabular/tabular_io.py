from typing import Any

from iopathlib.handlers import PathHandler
from iopathlib.tabular import TabularIO


class TabularUriParser:
    """ """

    def parse_uri(self, uri: str) -> None:
"


class TabularPathHandler(PathHandler):
    """ """

    def _opent(
        self,
        path: str,
        mode: str = "r",
        buffering: int = 32,
        **kwargs: Any,
    ) -> TabularIO:
        """Parameters
        ----------
        path: str :

        mode: str :
             (Default value = "r")
        buffering: int :
             (Default value = 32)
        **kwargs: Any :


        Returns
        -------

        """
        assert mode == "r"
