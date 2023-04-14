import sqlite3


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

    def __repr__(self):
        return self.__str__()


class CONSTANT(Base):
    def __init__(self, value) -> None:
        number = [int, float]
        string = [str, bytes]
        valid = [*number, *string]

        if isinstance(value, bool):
            self.value = str(value).lower()
        elif isinstance(value, tuple(number)):
            self.value = value
        elif isinstance(value, str):
            self.value = f"'{value}'"
        elif isinstance(value, bytes):
            self.value = memoryview(value)
        else:
            raise Exception(f"value must be of type {valid} not {type(value)}")

    def __str__(self) -> str:
        return str(self.value)


class Name_Space_Base(Base):
    @property
    def name(self):
        return super().name.replace("_", " ")


class Statement(Name_Space_Base):
    def __bool__(self):
        ret = sqlite3.complete_statement(str(self))
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

    def __str__(self) -> str:
        return self._string


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

        super().__init__(first)
        self.second = second

    def __str__(self) -> str:
        text = super().__str__()
        if self.second:
            text += f".{self.second}"
        return text


class Columns(Base):
    def __init__(self, columns: list, parenthesis=False) -> None:
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


class New_Columns(Columns):
    def __init__(self, args: list) -> None:
        """
        :args: instances of (Data_Type, Constraint, Modifier)
        """
        from .statements import Data_Type, Constraint, Modifier

        allowed = (Data_Type, Constraint, Modifier)
        columns = []
        for arg in args:
            if isinstance(arg, allowed):
                columns.append(arg)
            else:
                raise Exception(
                    f"args must be instances or subclasses of {[a.__name__ for a in allowed]}, not {type(arg).__name__}"
                )

        super().__init__(columns, parenthesis=True)


NCs = New_Columns


class VALUES(Columns):
    def __init__(self, values: list, insert=True) -> None:
        _columns = []
        if insert:
            for column in values:

                if isinstance(column, str):
                    _columns.append(CONSTANT(column))
                else:
                    _columns.append(column)

        super().__init__(_columns, parenthesis=True)

    @property
    def string(self):
        return super().__str__()

    def __str__(self) -> str:
        return f"{self.name} {self.string}"


class MULTI_VALUES:
    def __init__(self, values: list) -> None:
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
