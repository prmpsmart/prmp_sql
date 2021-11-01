"Data Manipulation"

from ..keywords.reserved import (
    SELECT as _SELECT,
    INSERT as _INSERT,
    UPDATE as _UPDATE,
    MERGE as _MERGE,
    DELETE as _DELETE,
)
from . import STATEMENT


class Data_Manipulation(STATEMENT):
    ...


class SELECT(Data_Manipulation):
    def __init__(self):
        super().__init__([_SELECT], "Retrieves data from the database")


class INSERT(Data_Manipulation):
    def __init__(self):
        super().__init__([_INSERT], "Adds new rows of data to the database")


class UPDATE(Data_Manipulation):
    def __init__(self):
        super().__init__([_UPDATE], "Modifies existing database data")


class MERGE(Data_Manipulation):
    def __init__(self):
        super().__init__(
            [_MERGE], "Conditionally inserts/updates/deletes new and existing rows"
        )


class DELETE(Data_Manipulation):
    def __init__(self):
        super().__init__([_DELETE], "Removes rows of data from the database")
