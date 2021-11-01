def format():
    import os

    os.system("python -m black .")
    exit()


# format()

from lib2.statements import *
from lib2.clauses import *
from lib2.operators import *


# print(dir())


s = SELECT(
    Columns('NAME', 'QUOTA', 'SALES'),
    FROM("SALESREPS"),
    where=WHERE(OR(LESS_THAN('SALES', 'QOUTA'), LESS_THAN('SALES', 300000))),
)

print(s)
