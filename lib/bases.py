from typing import ChainMap


class BASE:
    DESCRIPTION = ""

    def __init__(self, name) -> None:
        self.NAME = name
        super().__init__()

    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name.upper()
