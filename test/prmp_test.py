import _pathy
from prmp_sql.built_in_funtions import BIT_LENGTH, POSITION, TRIM_BOTH, TRIM_LEADING
from prmp_sql.modifiers import *
from prmp_sql.constraints import *
from prmp_sql.datatypes import *
from prmp_sql.functions import *
from prmp_sql.statements import *
from prmp_sql.clauses import *
from prmp_sql.operators import *
from prmp_sql.database import DataBase


a = LEFT_JOIN(
    SELECT(
        Columns(
            Column("city", "name"),
            Column("country", "name"),
        ),
        FROM("city"),
    ),
    Table("country"),
)
# a = INSERT(
#     INTO(Table("Albums")),
#     Columns("AlbumName", "ArtistId", parenthesis=1),
#     MULTI_VALUES(("DEFAULT", "parenthesis"), ("Ziltoid the Omniscient", "12")),
# )
a = UPDATE(
    "Atrists",
    SET(
        ("ArtistName", CONSTANT("The Artist Formerly Known as Prince")),
        ("Formerly", CONSTANT("Known as Prince")),
    ),
    WHERE(EQUAL("ArtistName", CONSTANT("Prince"))),
)
a = DELETE(Table("Artists"), WHERE(EQUAL("ArtistId", CONSTANT("6"))))
a = TRUNCATE_TABLE("Artists")
a = CREATE(UNIQUE_INDEX(ON("index_name", "table_name", Columns("column1", "column2"))))
a = ALTER_DATABASE(COLLATE("Movies", "utf8_unicode_ci"))
a = DROP_DATABASE("Movies")


a = CREATE_TABLE("Actors", New_Columns(NOT_NULL("love"), NOT_NULL("boys")))
a = ALTER_TABLE("table_name", SET(EQUAL("AUTO_INCREMENT", 100)))

a = SELECT("apata", "table")
a = CREATE_TABLE(
    "ile_ige",
    New_Columns(VARCHAR("rooms"), VARCHAR("pay"), INT("number")),
)
db = DataBase("test_db")
db.init()


a = """CREATE TABLE Persons (
    Personid int IDENTITY(1,1) PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);"""

a = CREATE_TABLE(
    "Persons",
    # PRIMARY_KEY(IDENTITY(INTEGER("Personid"), 1, 1)),
    AUTOINCREMENT(PRIMARY_KEY(INTEGER("Personid"))),
    NOT_NULL(VARCHAR("LastName")),
    UNIQUE(VARCHAR("FirstName")),
    INT("Age"),
)
# db.exec_s(a)

ba = """CREATE VIEW OR REPLACE ViewName AS
SELECT Column1, Column2, ..., ColumnN
FROM Persons
WHERE Condition;"""

a = INSERT(
    "Persons",
    Columns("LastName", "FirstName", "Age"),
    MULTI_VALUES(("Peter", "Miracle", 22), ("Apata", "Timi", 56)),
)
# db.exec_s(a)
# a = SELECT("*", "Persons")
# print(a + a)
# db.commit()
# db = db.exec_s(a)
# print(list(db))

a = POSITION("love", ("love", "hate", "indiff"))
a = BIT_LENGTH("love")
a = TRIM_BOTH("h", "hhdgrgssdhh")
print(BETWEEN(1, 2, 3))
