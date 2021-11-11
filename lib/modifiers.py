from .bases import Base
from .functions import Two_Value


class Modifier(Base):
    ...


class IDENTITY(Modifier, Two_Value):
    def __init__(self, value, first, second) -> None:
        Modifier.__init__(self)
        Two_Value.__init__(self, first, second)
        self.value = value

    @property
    def name(self):
        return f"{self.value} {super().name}"
