from .functions import Function
from .clauses import FROM, GROUP_BY, HAVING, ORDER_BY, WHERE, Clause
from .bases import Base, Column, Columns
from .operators import AS, TO


class SELECT(Base):

    DESCRIPTION = ""
    parenthesis = False

    def __init__(
        self,
        columns,
        from_,
        where=None,
        group=None,
        having=None,
        order=None,
        into=None,
        distinct=False,
        all=False,
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
            assert isinstance(from_, FROM)
        if where:
            assert isinstance(where, WHERE)
        if group:
            assert isinstance(group, GROUP_BY)
        if having:
            assert isinstance(having, HAVING)
        if order:
            assert isinstance(order, ORDER_BY)
        # assert isinstance(into, (str, INTO_TABLE))

        self.columns = columns
        self.from_ = from_
        self.where = where
        self.group = group
        self.having = having
        self.order = order
        self.into = into

        self.distinct = distinct
        self.all = all

        super()

    def __str__(self):
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


class INSERT(Base):
    def __init__(self, into, values, columns="", where=None) -> None:
        self.into = into
        self.values = values
        self.columns = columns
        self.where = where

    def __str__(self) -> str:
        text = f"{self.name} {self.into}"
        if self.columns:
            text += f" {self.columns}"
        text += f" {self.values}"
        if self.where:
            text += f" {self.where}"

        return text


class UPDATE(Base):
    def __init__(self, table, set, where=None) -> None:
        self.table = table
        self.set = set
        self.where = where

    def __str__(self) -> str:
        text = f"{self.name} {self.table} {self.set}"
        if self.where:
            text += f" {self.where}"
        return text


class DELETE(Base):
    def __init__(self, table, where=None) -> None:
        self.table = table
        self.where = where

    def __str__(self) -> str:
        text = f"{self.name} FROM {self.table}"
        if self.where:
            text += f" {self.where}"
        return text


class One_Line(Clause):
    def __init__(self, expression) -> None:
        self.expression = expression

    def __str__(self) -> str:
        return f"{self.name} {self.expression}"


class TRUNCATE(One_Line):
    ...


class New_Column:
    def __init__(self, name, tags=[]) -> None:
        self.name = name
        self.tags = tags

    def __str__(self) -> str:
        text = self.name

        for a in self.tags:
            text += f" {a}"

        return text


NC = New_Column


class New_Columns(Columns):
    def __init__(self, *args) -> None:
        """
        :args: instances of New_Column or tuples containing the parameters of a New_Column class
        """
        columns = []
        for arg in args:
            val = None
            if isinstance(arg, (str, New_Column)):
                val = arg
            elif isinstance(arg, tuple):
                val = New_Column(arg[0], arg[1])
            else:
                raise "args must be instances of New_Column or tuples containing the parameters of a New_Column class"

            if val:
                columns.append(val)

        super().__init__(*columns, parenthesis=True)


NCs = New_Columns


class CREATE(One_Line):
    def __init__(self, expression) -> None:
        super().__init__(expression)


class CREATE_TABLE(CREATE):
    def __init__(self, table, new_columns) -> None:
        assert isinstance(new_columns, New_Columns)
        expression = f"{table} {new_columns}"
        super().__init__(expression)


class CREATE_DATABASE(CREATE):
    ...


class CREATE_VIEW(CREATE):
    def __init__(self, view, select) -> None:
        assert isinstance(select, SELECT), f"select must be an instance of {SELECT}"
        expression = AS(view, select)
        super().__init__(expression)


class Modifier(Base):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return super().__str__()


class ADD_COLUMN(One_Line):
    def __init__(self, *values) -> None:
        """
        :values: value in values can be a [str, Column, tuple, list].
        when value is a tuple or list, it must be of length 2, (column_name, datatype)
        """
        expression = None

        l = len(values)
        if l:
            ll = [type(value) for value in values]
            if Columns in ll:
                assert l == 1, "Only one Columns object should be parsed."
                expression = values[0]
        else:
            columns = []
            for value in values:
                col = None
                if isinstance(value, (str, Column)):
                    col = value

                elif isinstance(value, (tuple, list)):
                    assert len(value) == 2, "Length of Tuple or List must be 2."
                    col = New_Column(value[0], tags=[value[1]])

                else:
                    raise Exception("Value not supported.")

                columns.append(col)

                expression = New_Columns(*columns)

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

class RENAME(One_Line):...

class RENAME_TABLE(RENAME):

    def __init__(self, expression) -> None:
        assert isinstance(expression, TO)
        super().__init__(expression)

...