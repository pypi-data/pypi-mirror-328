from typing import Callable

type Version = str
type VersionRetriever = Callable[[], Version]