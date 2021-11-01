from bases import *


class Object(BASE):
    ...


class Objects(BASE):
    ...


Table = Object("Table")

Tables = Objects("Tables")


Column = Object("Column")

Columns = Objects("Columns")


User = Object("User")

Users = Objects("Users")
