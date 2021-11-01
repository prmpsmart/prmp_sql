from lib2.functions import *
from lib2.statements import *
from lib2.clauses import *
from lib2.operators import *


# print(dir())


s = SELECT(
    Columns("name", "region", MINUS("sales", "target")),
    FROM(
        "offices",
    ),
    order=ORDER_BY(ASC("region"), DESC(3)),
)
u = UNION(s, s)
u = UNION(s, u)

print()
print(
    SELECT(
        "*",
        FROM(AS("city", "main_city", hide=True)),
        where=WHERE(
            GREATER_THAN(
                "population",
                SELECT(
                    AVG("population"),
                    FROM(AS("city", "average_city", hide=True)),
                    where=WHERE(EQUAL(Column('country_id', table='average_city'), Column('country_id', table='main_city'))),
                ),
            )
        ),
    )
)
