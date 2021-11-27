from .operators import *
from .clauses import *

class WHERE_EQUAL:

    def __init__(self, first, second) -> None:
        self.value = WHERE(EQUAL(first, second, constant=1))
    def __str__(self) -> str:
        return self.value