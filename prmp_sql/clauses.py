from .operators import EQUAL, Operator
from .bases import Name_Space_Base, Columns, CONSTANT, Column


class Clause(Name_Space_Base):
    def __init__(self, expression=None) -> None:
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
    def __init__(self, search_condition: Operator) -> None:
        assert isinstance(search_condition, Operator)
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
    def __init__(self, values, columns=[]) -> None:
        """
        :values: tuple, list of length 2, or instance of EQUAL
        """
        if columns:
            values = [CONSTANT(a) if not isinstance(a, Column) else a for a in values]

            values = list(zip(columns, values))

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
                    equal = None
                    if isinstance(value, (tuple, list)):
                        assert (
                            len(value) == 2
                        ), "Tuple or List must be of len 2, (column_name1, value1) i.e column_name1 = value1"
                        equal = EQUAL(*value)
                    elif isinstance(value, (EQUAL, SET)):
                        equal = value

                    equal.parenthesis = False
                    columns.append(equal)

                expression = Columns(columns)

        super().__init__(expression)


class INDEX(Clause):
    def __init__(self, expression) -> None:
        super().__init__(expression)

    def __str__(self) -> str:
        return f"{self.name} {self.expression}"


class UNIQUE_INDEX(INDEX):
    ...
