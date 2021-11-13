import _sqlite3 as _SQL_ENGINE


class function:
    # TODO not defined in builtins!
    ...


class Base:
    DESCRIPTION = ""

    @property
    def name(self):
        return self.__class__.__name__

    def debug(self):
        print(self)

    def __add__(self, other):
        return f"{self} {other}"


class CONSTANT(Base):
    def __init__(self, value) -> None:
        valid = (str, int, float)
        assert isinstance(value, valid), f"value must be of type {valid}"
        if isinstance(value, (int, float)):
            self.value = value
        elif isinstance(value, str):
            self.value = f"'{value}'"

    def __str__(self) -> str:
        return str(self.value)


class Statement(Base):
    def __bool__(self):
        ret = _SQL_ENGINE.complete_statement(str(self))
        return ret

    @property
    def bool(self):
        return bool(self)

    def debug(self):
        print(f"({self}) [{self.bool}]")

    @property
    def string(self) -> str:
        """"""

    def __str__(self) -> str:
        return f"{self.string};"

    def __add__(self, other):
        return Statement_(f"{self} {other}")


class Statement_(Statement):
    def __init__(self, string):
        self._string = string

    @property
    def string(self) -> str:
        return self._string


class Name_Space_Base(Base):
    @property
    def name(self):
        return super().name.replace("_", " ")


class Table(Base):
    def __init__(self, first) -> None:
        self.first = first

    def __str__(self) -> str:
        return self.first


class Column(Table):
    def __init__(self, first, second="") -> None:
        """
        if 'first' and 'second' are both provided, first is assumed the table name, and the second as column name in the table

        if only first is provided it is assumed as the column name
        """

        if isinstance(first, Table):
            first = Table(first)

        if second:
            second, first = first, second

        self.second = second
        super().__init__(first)

    def __str__(self) -> str:
        text = super().__str__()
        if self.second:
            text = f"{self.second}.{text}"
        return text


class Columns(Base):
    def __init__(self, *columns, parenthesis=False) -> None:
        self.columns = columns
        self.parenthesis = parenthesis

    def __str__(self) -> str:
        text = ""
        for column in self.columns:
            text += f"{column}, "
        text = "".join(text[:-2])
        if self.parenthesis:
            text = f"({text})"

        return text


class VALUES(Columns):
    def __init__(self, *values, insert=True) -> None:
        _columns = []
        if insert:
            for column in values:
                if not isinstance(column, CONSTANT):
                    _columns.append(CONSTANT(column))

        super().__init__(*_columns, parenthesis=True)

    def __str__(self) -> str:
        return f"{self.name} {super().__str__()}"


class MULTI_VALUES:
    def __init__(self, *values) -> None:
        for val in values:
            assert isinstance(
                val, (Columns, tuple)
            ), "values must be an instance of Columns"
        self.values = values

    def __str__(self) -> str:
        text = "VALUES "
        for val in self.values:
            text += f"{val}, "

        text = "".join(text[:-2])
        return text
