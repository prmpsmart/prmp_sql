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


class AVG(Function):
    ...


class COUNT(Function):
    ...


class MAX(Function):
    ...


class MIN(Function):
    ...


class SUM(Function):
    ...
