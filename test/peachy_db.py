import _pathy
from lib.built_in_funtions import BIT_LENGTH, POSITION, TRIM_BOTH, TRIM_LEADING
from lib.modifiers import *
from lib.constraints import *
from lib.datatypes import *
from lib.functions import *
from lib.statements import *
from lib.clauses import *
from lib.operators import *
from lib.database import DataBase as DB


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


st = CREATE_TABLE(
    "users",
    UNIQUE(VARCHAR("id"), VARCHAR("name")),
)
