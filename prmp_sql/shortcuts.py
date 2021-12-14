from .operators import *
from .clauses import *

def WHERE_EQUAL(first, second) -> WHERE:
    return WHERE(EQUAL(first, second, constant=1))
