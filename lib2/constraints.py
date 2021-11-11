from .bases import Base


class Constraint(Base):
    def __init__(self, value) -> None:
        self.value = value

    @property
    def name(self):
        return super().name.replace("_", " ")

    def __str__(self) -> str:
        return f"{self.value} {self.name}"


class NOT_NULL(Constraint):
    ...


class PRIMARY_KEY(Constraint):
    ...


class UNIQUE(Constraint):
    ...


class FOREIGN_KEY(Constraint):
    ...


class CHECK(Constraint):
    ...


class DEFERRABLE(Constraint):
    ...


class NOT_DEFERRABLE(Constraint):
    ...


class INITIALLY_IMMEDIATE(Constraint):
    ...


class INITIALLY_DEFERRED(Constraint):
    ...
