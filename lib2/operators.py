from typing import Tuple
from .bases import *


class Operators(Base):
    parenthesis = True
    LTR = True

    def __init__(self, operator, first, second=None) -> None:
        assert operator, "Operator value can not be [None, Empty string, 0]"
        assert first, "First value can not be [None, Empty string, 0]"

        self.operator = operator
        self.first = first
        self.second = second

    def __str__(self) -> str:
        ln = [bool(self.first), bool(self.second)].count(True)
        text = ""

        if ln == 1:
            if self.LTR:
                text = f"{self.operator} {self.first}"
            else:
                text = f"{self.first} {self.operator}"
        elif ln == 2:
            text = f"{self.first} {self.operator} {self.second}"

        if self.parenthesis:
            text = f"({text})"

        return text


class MINUS(Operators):
    def __init__(self, first, second) -> None:
        super().__init__("-", first, second=second)


class PLUS(Operators):
    def __init__(self, first, second) -> None:
        super().__init__("+", first, second=second)


class MULTIPLY(Operators):
    def __init__(self, first, second) -> None:
        super().__init__("*", first, second=second)


class DIVIDE(Operators):
    def __init__(self, first, second) -> None:
        super().__init__("/", first, second=second)


class EQUAL(Operators):
    def __init__(self, first, second) -> None:
        super().__init__("=", first, second=second)


class NOT_EQUAL(Operators):
    def __init__(self, first, second) -> None:
        super().__init__("<>", first, second=second)


class GREATER_THAN(Operators):
    def __init__(self, first, second) -> None:
        super().__init__(">", first, second=second)


class LESS_THAN(Operators):
    def __init__(self, first, second) -> None:
        super().__init__("<", first, second=second)


class GREATER_THAN_EQUAL(Operators):
    def __init__(self, first, second) -> None:
        super().__init__(">=", first, second=second)


class LESS_THAN_EQUAL(Operators):
    def __init__(self, first, second) -> None:
        super().__init__("<=", first, second=second)


# ---------------------------------------------------


class Name_Operators(Operators):
    parenthesis = False

    def __init__(self, first, second=None) -> None:
        super().__init__(self.name.replace("_", " "), first, second=second)


class AS(Name_Operators):
    def __init__(self, first, second) -> None:
        super().__init__(first, second=second)


class BETWEEN(Name_Operators):
    def __init__(self, first, second, third) -> None:
        assert type(second) == type(
            third
        ), "second and third value must be of same data_type"

        super().__init__(first, second=second)
        self.third = third

    def __str__(self) -> str:
        text = super().__str__()
        return f"{text} AND {self.third}"


class ESCAPE(Name_Operators):
    def __init__(self, first) -> None:
        assert isinstance(first, str) and (
            len(first) == 1
        ), "ESCAPE character must be a a char like [s, t, etc]"
        first = f"'{first}'"

        super().__init__(first)


class LIKE(Name_Operators):
    WILDCARDS = ["%", "_", "[*...]", "[^...]", "[!...]"]

    def __init__(self, first, second, escape=None) -> None:
        assert isinstance(
            second, str
        ), "second value must be a string containing wildcards"

        super().__init__(first, second=second)
        if isinstance(escape, str):
            escape = ESCAPE(escape)
        self.escape = escape

    def __str__(self) -> str:
        text = super().__str__()
        if self.escape:
            text = f"{text} {self.escape}"
        return text


class IN(Name_Operators):
    def __init__(self, first, second: Tuple) -> None:
        assert isinstance(second, tuple)

        super().__init__(first, second=second)


class AND(Name_Operators):
    def __init__(self, first, second) -> None:
        super().__init__(first, second=second)


class OR(Name_Operators):
    def __init__(self, first, second) -> None:
        super().__init__(first, second=second)


class DISTINCT(Name_Operators):
    def __init__(self, first) -> None:
        assert isinstance(first, (str, Column, Columns))
        super().__init__(first)


class Name_Operators_F(Name_Operators):
    LTR = False


class IS_NULL(Name_Operators_F):
    def __init__(self, first) -> None:
        super().__init__(first)


class IS_NOT_NULL(Name_Operators_F):
    def __init__(self, first) -> None:
        super().__init__(first)
