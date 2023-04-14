from .operators import LIMIT
from .bases import sqlite3
from .statements import *
from .functions import *


class _AggregateProtocol(Protocol):
    def step(self, value: int) -> None:
        ...

    def finalize(self) -> int:
        ...


class Wrapper:
    DataError = sqlite3.Connection.DataError
    DatabaseError = sqlite3.Connection.DatabaseError
    Error = sqlite3.Connection.Error
    IntegrityError = sqlite3.Connection.IntegrityError
    InterfaceError = sqlite3.Connection.InterfaceError
    InternalError = sqlite3.Connection.InternalError
    NotSupportedError = sqlite3.Connection.NotSupportedError
    OperationalError = sqlite3.Connection.OperationalError
    ProgrammingError = sqlite3.Connection.ProgrammingError
    Warning = sqlite3.Connection.Warning

    CONNECT = sqlite3.connect
    VALIDATE_STATEMENT = sqlite3.complete_statement

    def __init__(
        self, path, cursorClass: Union[type, None] = None, init: bool = False, **kwargs
    ) -> None:
        assert path, 'Path or ":memory: must be provided.'

        self.path = path
        self.kwargs = kwargs
        self.__connection = None
        self.initialized = False

        if init:
            self.init()

    def init(self):
        if self.initialized:
            return
        self.__connection = self.CONNECT(self.path, **self.kwargs)
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
        if self.__connection:
            self.initialized = False
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

    def execute(self, sql: str, parameters: Iterable[Any] = []) -> sqlite3.Cursor:
        "returns a cursor object, which can be used to retrieve the values in case of SELECT statement."
        return self.__connection.execute(str(sql), parameters)

    def executemany(
        self, __sql: str, __parameters: Iterable[Iterable[Any]] = []
    ) -> sqlite3.Cursor:
        return self.__connection.executemany(str(__sql), __parameters)

    def executescript(self, __sql_script: Union[bytes, str]) -> sqlite3.Cursor:
        return self.__connection.executescript(__sql_script)

    def interrupt(self, *args: Any, **kwargs: Any) -> None:
        return self.__connection.interrupt(*args, **kwargs)

    def iterdump(self, *args: Any, **kwargs: Any) -> Generator[str, None, None]:
        return self.__connection.iterdump(*args, **kwargs)

    def rollback(self, *args: Any, **kwargs: Any) -> None:
        return self.__connection.rollback(*args, **kwargs)


class Database(Wrapper):

    SAVE = False
    DEBUG = False

    def __init__(self, path=":memory:", **kwargs) -> None:
        Wrapper.__init__(self, path, **kwargs)

    def execute_statement(
        self,
        statement: Statement,
        parameters: list = [],
        many: bool = False,
        dry: bool = False,
        quiet: bool = False,
        quietError: bool = False,
    ):
        if not self.initialized:
            print("Not Initialised")
            return

        func = self.executemany if many else self.execute
        if not quiet:
            print(statement)
        try:
            if not dry:
                assert isinstance(parameters, list)
                res = func(str(statement), parameters)
                return list(res)
        except Exception as e:
            if not quietError:
                raise e
            return e

    def exec(self, statement: Statement, query=False, debug=False) -> sqlite3.Cursor:
        statement_ = str(statement)
        if debug or self.DEBUG:
            print(f"EXECUTE: {statement_}")

        if self.initialized:
            result = self.execute(statement_)
            if self.SAVE and not query:
                self.commit()
            return result

    def query(self, statement: Statement, debug=False) -> List[Dict[str, Any]]:
        statement_ = str(statement)

        if debug or self.DEBUG:
            print(f"QUERY: {statement_}")
        result = list(self.exec(statement, query=True) or [])
        if debug or self.DEBUG:
            print(f"QUERY_RESULT: {result}")

        return result

    def check_if_exists(self, table: str, where: WHERE) -> bool:
        count_1 = COUNT(1)
        select = SELECT(
            count_1,
            table,
            where=where,
            limit=LIMIT(1),
        )

        result = self.query(select)
        value = False
        if result:
            value = result[0][0] != 0

        return value

    def REMOVE(self, table: str, where: WHERE):
        self.exec(DELETE(table, where=where))
