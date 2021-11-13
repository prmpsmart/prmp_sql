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
