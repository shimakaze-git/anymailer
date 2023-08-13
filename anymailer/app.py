import logging
from typing import Any

logger = logging.getLogger("anymailer")


class App:
    def __init__(self, settings: dict[str, Any]) -> None:
        self.settings = settings

    def start(self) -> None:
        logger.info("anymailer Starting")

    def stop(self) -> None:
        logger.info("anymailer Stopping")
