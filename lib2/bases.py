class Base:
    DESCRIPTION = ""

    @property
    def name(self):
        return self.__class__.__name__


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
    def __init__(self, *columns) -> None:
        self.columns = columns

    def __str__(self) -> str:
        text = ""
        for column in self.columns:
            text += f"{column}, "
        text = "".join(text[:-2])

        return text
