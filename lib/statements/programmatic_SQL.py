"Programmatic SQL"

from ..keywords.non_reserved import EXPLAIN as _EXPLAIN
from ..keywords.reserved import (
    DECLARE as _DECLARE,
    OPEN as _OPEN,
    FETCH as _FETCH,
    CLOSE as _CLOSE,
    PREPARE as _PREPARE,
    EXECUTE as _EXECUTE,
    DESCRIBE as _DESCRIBE,
)
from . import STATEMENT


class Programmatic_SQL(STATEMENT):
    ...


DECLARE = STATEMENT([_DECLARE], "Defines a cursor for a query")

EXPLAIN = STATEMENT([_EXPLAIN], "Describes the data access plan for a query")

OPEN = STATEMENT([_OPEN], "Opens a cursor to retrieve query results")

FETCH = STATEMENT([_FETCH], "Retrieves a row of query results")

CLOSE = STATEMENT([_CLOSE], "Closes a cursor")

PREPARE = STATEMENT([_PREPARE], "Prepares a SQL statement for dynamic execution")

EXECUTE = STATEMENT([_EXECUTE], "Executes a SQL statement dynamically")

DESCRIBE = STATEMENT([_DESCRIBE], "Describes a prepared query")
