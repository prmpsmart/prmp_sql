class Base:
    DESCRIPTION = ""

    @property
    def name(self):
        return self.__class__.__name__

class Table(Base):
    def __init__(self, table) -> None:
        self.table = table
    
    def __str__(self) -> str:
        self.table

class Column(Base):
    
    def __init__(self, column, table: Table=None) -> None:
        if isinstance(table, Table): table = Table(table)
        self.column = column
        self.table = table
    
    def __str__(self) -> str:
        text = self.column
        if self.table: text = f'{self.table}.{text}'
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
