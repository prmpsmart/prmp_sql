from lib2.functions import *
from lib2.statements import *
from lib2.clauses import *
from lib2.operators import *

print(
    LEFT_JOIN(
        SELECT(
            Columns(
                Column("city", "name"),
                Column("country", "name"),
            ),
            FROM("city"),
        ),
        Table("country"),
    ),
)