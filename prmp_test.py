from lib2.datatypes import CONSTANT
from lib2.functions import *
from lib2.statements import *
from lib2.clauses import *
from lib2.operators import *

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
a = INSERT(
    INTO(Table("Albums")),
    MULTI_VALUES(("DEFAULT", "parenthesis"), ("Ziltoid the Omniscient", "12")),
    columns=Columns("AlbumName", "ArtistId", parenthesis=1),
)
a = UPDATE(
    "Atrists",
    SET("ArtistName", "The Artist Formerly Known as Prince"),
    WHERE(EQUAL("ArtistName", CONSTANT("Prince"))),
)
a = DELETE(Table('Artists'), WHERE (EQUAL('ArtistId', CONSTANT('6'))))
print(a)

# import os
# f = r'C:\Users\Administrator\Downloads\PRMP SQL'
# os.chdir(f)
# for a in os.listdir(f):
#     os.rename(a, a.replace('.html', '.mhtml'))
