from typing import *
from .modifiers import Modifier
from .constraints import Constraint
from .datatypes import Data_Type
from .functions import Function, One_Value
from .clauses import FROM, GROUP_BY, HAVING, ORDER_BY, WHERE, Clause, SET
from .bases import MULTI_VALUES, VALUES, Column, New_Columns, Columns, Statement, Table
from .operators import AS, INTO, TO


class SELECT(Statement):

    DESCRIPTION = ""
    parenthesis = False

    def __init__(
        self,
        columns,
        from_,
        where: WHERE = None,
        group=None,
        having=None,
        order=None,
        into=None,
        distinct=False,
        all=False,
        limit=False,
        offset=False,
    ) -> None:
        """
        :columns: instance of Columns|Column
        :from_: instance of FROM
        :where: instance of WHERE
        :group: instance of GROUP
        :having: instance of HAVING
        :order: instance of ORDER
        :into: instance of INTO
        """
        if columns:
            assert isinstance(
                columns, (str, Columns, Function)
            ), f"type ({str}, {Columns}, {Function}) is expected not {type(columns)}."
        if from_:
            assert isinstance(from_, (str, FROM))
            if isinstance(from_, str):
                from_ = FROM(from_)
        if where:
            assert isinstance(where, WHERE)
        if group:
            assert isinstance(group, GROUP_BY)
        if having:
            assert isinstance(having, HAVING)
        if order:
            assert isinstance(order, ORDER_BY)
        if into:
            assert isinstance(into, (str, INTO))

        self.columns = columns
        self.from_ = from_
        self.where = where
        self.group = group
        self.having = having
        self.order = order
        self.into = into

        self.distinct = distinct
        self.all = all

    @property
    def string(self) -> str:
        all_dis = " ALL " if self.all else " DISTINCT " if self.distinct else " "

        default = f"{self.name}{all_dis}{self.columns}"
        if self.into:
            default += f" {self.into}"
        default += f" {self.from_}"
        if self.where:
            default += f" {self.where}"
        if self.group:
            default += f" {self.group}"
        if self.having:
            default += f" {self.having}"
        if self.order:
            default += f" {self.order}"

        if self.parenthesis:
            default = f"({default})"

        return default


class INSERT(Statement):
    def __init__(
        self,
        table: Union[str, Table],
        columns: Columns = None,
        values: Union[VALUES, MULTI_VALUES] = (),
    ) -> None:
        if columns:
            assert type(columns) == Columns
            columns.parenthesis = True
        assert isinstance(values, (VALUES, MULTI_VALUES))
        assert isinstance(table, (str, Table))
        assert table

        self.table = INTO(table)
        self.columns = columns or ""
        self.values = values

    @property
    def string(self) -> str:
        text = f"{self.name} {self.table}"
        if self.columns:
            text += f" {self.columns}"
        text += f" {self.values}"

        return text


class UPDATE(Statement):
    def __init__(self, table, set: SET, where: WHERE = None) -> None:
        self.table = table
        assert isinstance(set, SET)
        self.set = set
        assert isinstance(where, WHERE)
        self.where = where

    @property
    def string(self) -> str:
        text = f"{self.name} {self.table} {self.set}"
        if self.where:
            text += f" {self.where}"
        return text


class DELETE(Statement):
    def __init__(self, table, where: WHERE = None) -> None:
        self.table = table
        self.where = where

    @property
    def string(self) -> str:
        text = f"{self.name} FROM {self.table}"
        if self.where:
            text += f" {self.where}"
        return text


class One_Line(Statement):
    def __init__(self, expression) -> None:
        self.expression = expression

    @property
    def string(self) -> str:
        return f"{self.name} {self.expression}"


class TRUNCATE_TABLE(One_Line):
    ...


class CREATE(One_Line):
    ...


class CREATE_TABLE(CREATE):
    def __init__(
        self, table, new_columns: Union[New_Columns, list], check_exist=False
    ) -> None:
        assert new_columns

        if len(new_columns) == 1 and isinstance(new_columns[0], New_Columns):
            new_columns = new_columns[0]
        else:
            new_columns = New_Columns(new_columns)

        assert isinstance(new_columns, New_Columns)
        exist = "IF NOT EXISTS " if check_exist else ""

        expression = f"{exist}{table} {new_columns}"
        super().__init__(expression)


class CREATE_DATABASE(CREATE):
    ...


class CREATE_VIEW(CREATE):
    def __init__(self, view, select) -> None:
        assert isinstance(select, SELECT), f"select must be an instance of {SELECT}"
        expression = AS(view, select)
        super().__init__(expression)


class ALTER_TABLE(One_Line):
    # TODO
    def __init__(self, table, modifier) -> None:
        expression = f"{table} {modifier}"
        super().__init__(expression)


class ALTER_DATABASE(One_Line):
    ...


class DROP_DATABASE(One_Line):
    ...


class DROP_TABLE(One_Line):
    ...


class DROP_VIEW(One_Line):
    ...


class RENAME(One_Line):
    ...


class RENAME_TABLE(RENAME):
    def __init__(self, expression) -> None:
        assert isinstance(expression, TO)
        super().__init__(expression)


class WITH(One_Value):
    def __init__(self, first) -> None:
        super().__init__(first)
