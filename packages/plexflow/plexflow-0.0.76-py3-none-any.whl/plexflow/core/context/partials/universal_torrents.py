from plexflow.core.context.partial_context import PartialContext
from datetime import datetime as dt
from plexflow.core.torrents.results.universal import UniversalTorrent
from typing import List

class UniversalTorrents(PartialContext):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def sources(self) -> list[str]:
        keys = self.get_keys("universal/torrents/*")
        # extract the source from the key
        return [key.split("/")[-1] for key in keys]

    def from_source(self, source: str) -> List[UniversalTorrent]:
        return self.get(f"universal/torrents/{source}")

    def update(self, torrents: List[UniversalTorrent]):
        if len(torrents) == 0:
            return
        source = next(iter(torrents)).source
        self.set(f"universal/torrents/{source}", torrents)
