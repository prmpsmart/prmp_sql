from typing import List
from ..bases import BASE


class STATEMENT(BASE):
    DESCRIPTION = ""
    KEYWORDS = []

    def __init__(self, keywords: List, desc: str) -> None:
        self.KEYWORDS = keywords
        self.DESCRIPTION = desc
        super().__init__(str(self))

    def __str__(self):
        return " ".join(self.KEYWORDS)
