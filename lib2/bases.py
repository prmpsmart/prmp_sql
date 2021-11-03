class Base:
    DESCRIPTION = ""

    @property
    def name(self):
        return self.__class__.__name__


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
    def __init__(self, *args, columns=[]) -> None:
        from .datatypes import CONSTANT

        _columns = list(args)
        for column in columns:
            if isinstance(column, str):
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
