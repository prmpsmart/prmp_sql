class Base:
    DESCRIPTION = ""

    @property
    def name(self):
        return self.__class__.__name__


class Column(Base):
    def __init__(self, column) -> None:
        self.column = column

    def __str__(self) -> str:
        return self.column


class Columns(Base):
    def __init__(self, *columns) -> None:
        self.columns = columns

    def __str__(self) -> str:
        text = ""
        for column in self.columns:
            text += f"{column}, "
        text = "".join(text[:-2])

        return text
