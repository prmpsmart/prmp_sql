from .bases import Base


class Function(Base):
    def __init__(self, first, second=None) -> None:
        self.first = first
        self.second = second

    def __str__(self):
        text = self.name
        if self.first:
            text += f"({self.first}"
            if self.second:
                text += f", {self.second}"
            text += ")"
        return text


class One_Value(Function):
    def __init__(self, first) -> None:
        super().__init__(first)


class Two_Value(Function):
    def __init__(self, first, second) -> None:
        super().__init__(first, second=second)


class AVG(One_Value):
    ...


class COUNT(One_Value):
    ...


class MAX(One_Value):
    ...


class MIN(One_Value):
    ...


class SUM(One_Value):
    ...


class ROUND(Two_Value):
    def __init__(self, column, integer) -> None:
        super().__init__(column, integer)
