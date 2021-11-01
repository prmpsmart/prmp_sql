"Data Definition"

from keywords.non_reserved import DOMAIN, INDEX, SCHEMA, VIEW
from keywords.reserved import ALTER, CREATE, DROP, TABLE
from . import STATEMENT


class Data_Definition(STATEMENT):
    ...


class CREATE_TABLE(Data_Definition):
    def __init__(self):
        super().__init__([CREATE, TABLE], "Adds a new table to the database")


class DROP_TABLE(Data_Definition):
    def __init__(self):
        super().__init__([DROP, TABLE], "Removes a table from the database")


class ALTER_TABLE(Data_Definition):
    def __init__(self):
        super().__init__([ALTER, TABLE], "Changes the structure of an existing table")


class CREATE_VIEW(Data_Definition):
    def __init__(self):
        super().__init__([CREATE, VIEW], "Adds a new view to the database")


class DROP_VIEW(Data_Definition):
    def __init__(self):
        super().__init__([DROP, VIEW], "Removes a view from the database")


class CREATE_INDEX(Data_Definition):
    def __init__(self):
        super().__init__([CREATE, INDEX], "Builds an index for a column")


class DROP_INDEX(Data_Definition):
    def __init__(self):
        super().__init__([DROP, INDEX], "Removes the index for a column")


class CREATE_SCHEMA(Data_Definition):
    def __init__(self):
        super().__init__([CREATE, SCHEMA], "Adds a new schema to the database")


class DROP_SCHEMA(Data_Definition):
    def __init__(self):
        super().__init__([DROP, SCHEMA], "Removes a schema from the database")


class CREATE_DOMAIN(Data_Definition):
    def __init__(self):
        super().__init__([CREATE, DOMAIN], "Adds a new data value domain")


class ALTER_DOMAIN(Data_Definition):
    def __init__(self):
        super().__init__([ALTER, DOMAIN], "Changes a domain definition")


class DROP_DOMAIN(Data_Definition):
    def __init__(self):
        super().__init__([DROP, DOMAIN], "Removes a domain from the database")
