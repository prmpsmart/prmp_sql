from .bases import Base


class Clause(Base):
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
    def __init__(self, sort_specification) -> None:
        super().__init__(sort_specification)
