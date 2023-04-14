from .bases import Column, Columns, New_Columns
from .constraints import Constraint
from .functions import Two_Value


class Modifier(Constraint):
    ...


class IDENTITY(Two_Value, Modifier):
    def __init__(self, value, first, second) -> None:
        Modifier.__init__(self, value)
        Two_Value.__init__(self, first, second)

    @property
    def name(self):
        return f"{self.value} {super().name}"


class AUTOINCREMENT(Modifier):
    ...


class TableModifier(Modifier):
    def __str__(self):
        return f"{self.name} {self.value}"


class ADD_COLUMN(TableModifier):
    def __init__(self, column: Column) -> None:
        super().__init__(column)

    @property
    def string(self) -> str:
        return f"ADD {self.value}"


class ALTER_COLUMN(TableModifier):
    def __init__(self, column: Column) -> None:
        super().__init__(column)


class DROP_COLUMN(TableModifier):
    def __init__(self, column: str) -> None:
        """
        :column: column to drop in a table
        """

        super().__init__(column)
