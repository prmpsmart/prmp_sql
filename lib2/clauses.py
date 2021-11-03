from .operators import EQUAL
from .bases import Name_Space_Base, Columns


class Clause(Name_Space_Base):
    def __init__(self, expression) -> None:
        self.expression = expression

    def __str__(self) -> str:
        name = self.name
        if self.expression:
            name += f" {self.expression}"
        return name


class FROM(Clause):
    def __init__(self, expression) -> None:
        super().__init__(expression)


class WHERE(Clause):
    def __init__(self, search_condition) -> None:
        super().__init__(search_condition)


class GROUP_BY(Clause):
    def __init__(self, grouping_column) -> None:
        super().__init__(grouping_column)


class HAVING(Clause):
    def __init__(self, search_condition) -> None:
        super().__init__(search_condition)


class ORDER_BY(Clause):
    def __init__(self, *columns: Columns) -> None:
        if not isinstance(columns, Columns):
            columns = Columns(*columns)
        super().__init__(columns)


class SET(Clause):
    def __init__(self, first, second) -> None:
        from .datatypes import CONSTANT

        if not isinstance(second, CONSTANT):
            second = CONSTANT(second)

        expression = EQUAL(first, second)
        expression.parenthesis = False

        super().__init__(expression)
