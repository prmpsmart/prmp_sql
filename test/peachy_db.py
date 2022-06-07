from prmp_sql.built_in_functions import BIT_LENGTH, POSITION, TRIM_BOTH, TRIM_LEADING
from prmp_sql.modifiers import *
from prmp_sql.constraints import *
from prmp_sql.datatypes import *
from prmp_sql.functions import *
from prmp_sql.statements import *
from prmp_sql.clauses import *
from prmp_sql.operators import *
from prmp_sql.database import DataBase as DB


class Server_Tables:

    objects = (
        "object_id",
        "name",
        "icon",
        "description",
        "object_type",
        "creator",
        "total_members",
    )
    unsent_chats = (
        "user_id",
        "recipient_id",
        "text",
        "data",
        "type",
        "datetime",
        "path",
        "recipient_type",
    )
    members = "admin", "member_id", "member_type"


class Client_Tables:

    users = "id", "name", "icon", "key", "description"
    objects = (
        "object_id",
        "name",
        "icon",
        "description",
        "object_type",
        "creator",
        "total_members",
    )
    chats = (
        "user_id",
        "recipient_id",
        "text",
        "data",
        "type",
        "datetime",
        "path",
        "sent",
        "recipient_type",
    )
    members = (
        "admin",
        "is_contact",
        "member_id",
        "name",
        "icon",
        "description",
        "member_type",
    )


st1 = CREATE_TABLE(
    "users",
    UNIQUE(VARCHAR("id")),
    VARCHAR("name"),
    BLOB("icon"),
    BLOB("key"),
    VARCHAR("description"),
)
st2 = CREATE_TABLE(
    "objects",
    UNIQUE(VARCHAR("object_id")),
    VARCHAR("name"),
    BLOB("icon"),
    VARCHAR("description"),
    VARCHAR("object_type"),
    VARCHAR("creator"),
    INT("total_members"),
)
st3 = CREATE_TABLE(
    "chats",
    VARCHAR("user_id"),
    VARCHAR("recipient_id"),
    VARCHAR("text"),
    BLOB("data"),
    VARCHAR("type"),
    VARCHAR("datetime"),
    VARCHAR("path"),
    BOOLEAN("sent"),
    VARCHAR("recipient_type"),
)
st4 = CREATE_TABLE(
    "members",
    BOOLEAN("admin"),
    BOOLEAN("is_contact"),
    VARCHAR("member_id"),
    VARCHAR("name"),
    BLOB("icon"),
    VARCHAR("description"),
    VARCHAR("member_type"),
)


st = [st1, st2, st3][:1]
# st.debug()

db = DB("peachy.db")
db.init()


# exit()
for a in st:
    print(a)
    # db.exec(a)
db.commit()
db.close()
