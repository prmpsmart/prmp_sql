import sqlite3 as SQL_ENGINE
from sqlite3.dbapi2 import *
from typing import *

from .bases import Statement


class _AggregateProtocol(Protocol):
    def step(self, value: int) -> None:
        ...

    def finalize(self) -> int:
        ...


class Wrapper:
    DataError = SQL_ENGINE.Connection.DataError
    DatabaseError = SQL_ENGINE.Connection.DatabaseError
    Error = SQL_ENGINE.Connection.Error
    IntegrityError = SQL_ENGINE.Connection.IntegrityError
    InterfaceError = SQL_ENGINE.Connection.InterfaceError
    InternalError = SQL_ENGINE.Connection.InternalError
    NotSupportedError = SQL_ENGINE.Connection.NotSupportedError
    OperationalError = SQL_ENGINE.Connection.OperationalError
    ProgrammingError = SQL_ENGINE.Connection.ProgrammingError
    Warning = SQL_ENGINE.Connection.Warning

    CONNECT = SQL_ENGINE.connect
    VALIDATE_STATEMENT = SQL_ENGINE.complete_statement

    def __init__(self, path, cursorClass: Union[type, None] = None) -> None:
        assert path, 'Path or ":memory: must be provided.'

        self.path = path
        self.__connection = None

        self.initialized = False

    def init(self):
        if self.initialized:
            return
        self.__connection = self.CONNECT(self.path)
        self.initialized = True

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__connection.cursor()

    @property
    def in_transaction(self):
        return self.__connection.in_transaction

    @property
    def isolation_level(self):
        return self.__connection.isolation_level

    @property
    def row_factory(self):
        return self.__connection.row_factory

    @property
    def text_factory(self):
        return self.__connection.text_factory

    @property
    def total_changes(self):
        return self.__connection.total_changes

    def close(self) -> None:
        return self.__connection.close()

    def commit(self) -> None:
        return self.__connection.commit()

    def create_aggregate(
        self, name: str, n_arg: int, aggregate_class: Callable[[], _AggregateProtocol]
    ) -> None:
        return self.__connection.create_aggregate(name, n_arg, aggregate_class)

    def create_collation(self, __name: str, __callback: Any) -> None:
        return self.__connection.create_collation(__name, __callback)

    def create_function(
        self, name: str, narg: int, func: Any, *, deterministic: bool = False
    ) -> None:
        return self.__connection.create_function(name, narg, func, deterministic)

    def execute(self, sql: str, parameters: Iterable[Any] = []) -> Cursor:
        return self.__connection.execute(sql, parameters)

    exec = execute

    def executemany(self, __sql: str, __parameters: Iterable[Iterable[Any]]) -> Cursor:
        return self.__connection.executemany(__sql, __parameters)

    exec_m = executemany

    def executescript(self, __sql_script: Union[bytes, str]) -> Cursor:
        return self.__connection.executescript(__sql_script)

    def interrupt(self, *args: Any, **kwargs: Any) -> None:
        return self.__connection.interrupt(*args, **kwargs)

    def iterdump(self, *args: Any, **kwargs: Any) -> Generator[str, None, None]:
        return self.__connection.iterdump(*args, **kwargs)

    def rollback(self, *args: Any, **kwargs: Any) -> None:
        return self.__connection.rollback(*args, **kwargs)


class DataBase(Wrapper):
    def __init__(self, path=":memory:") -> None:
        Wrapper.__init__(self, path)

    def execute_statement(self, statement: Statement, many=False, dry=False):
        func = self.executemany if many else self.execute
        print(statement.statement)
        try:
            if not dry:
                return func(statement.statement)
        except Exception as e:
            print(e)

    exec_s = execute_statement

    def insert(self, table_name="", map={}, where="", insert_obj=None):
        ...

    def update(self, table_name="", map={}, where="", update_obj=None):
        ...

    def delete(self, table_name="", map={}, where="", delete_obj=None):
        ...

    def select(self, table_name="", columns=[], where="", select_obj=None):
        ...

    query = select
