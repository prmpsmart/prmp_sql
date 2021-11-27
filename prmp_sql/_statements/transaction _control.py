"Transaction Control"

from ..keywords.reserved import (
    COMMIT as _COMMIT,
    ROLLBACK as _ROLLBACK,
    SET as _SET,
    START as _START,
    SAVEPOINT as _SAVEPOINT,
)
from . import STATEMENT


class Transaction_Control(STATEMENT):
    ...


COMMIT = Transaction_Control(_COMMIT, "Ends the current transaction")

ROLLBACK = Transaction_Control(_ROLLBACK, "Aborts the current transaction")


class SET(Transaction_Control):
    def __init__(self):
        super().__init__(
            _SET,
            "TRANSACTION Defines data access characteristics of the current transaction",
        )


START = Transaction_Control(_START, "TRANSACTION Explicitly starts a new transaction")

SAVEPOINT = Transaction_Control(
    _SAVEPOINT, "Establishes a recovery point for a transaction"
)
