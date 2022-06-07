from typing import Tuple

from .bases import *


class Operator(Base):
    LTR = True
    parenthesis = True

    def __init__(self, operator, first, second=None, parenthesis=None, constant=False) -> None:
        """
        :operator: Operator value can not be [None, 0]
        :first: First value can not be [None, Empty string, 0]
        """
        from .statements import SELECT

        if isinstance(second, SELECT):
            second.parenthesis = True

        if parenthesis!=None: self.parenthesis =parenthesis
        self.operator = operator
        self.first = first
        self.second = second if not constant else CONSTANT(second)

    def __str__(self) -> str:
        ln = [self.first==None, self.second==None].count(False)
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


class Two_Values(Operator):
    sign = ""

    def __init__(self, first, second, **kwargs) -> None:
        super().__init__(self.sign, first, second=second, **kwargs)


class MINUS(Two_Values):
    sign = "-"


class PLUS(Two_Values):
    sign = "+"


class MULTIPLY(Two_Values):
    sign = "*"


class DIVIDE(Two_Values):
    sign = "/"


class MODULO(Two_Values):
    sign = "%"


class EQUAL(Two_Values):
    sign = "="


class EQUAL_TO_STRING(EQUAL):
    def __init__(self, first, second, **kwargs) -> None:
        super().__init__(first, CONSTANT(second), **kwargs)


class NOT_EQUAL(Two_Values):
    OPERATORS = ["!=", "<>"]
    sign = "<>"


class GREATER_THAN(Two_Values):
    sign = ">"


class LESS_THAN(Two_Values):
    sign = "<"


class NOT_GREATER_THAN(Two_Values):
    sign = "!>"


class NOT_LESS_THAN(Two_Values):
    sign = "!<"


class GREATER_THAN_EQUAL(Two_Values):
    sign = ">="


class LESS_THAN_EQUAL(Two_Values):
    sign = "<="


# ---------------------------------------------------


class Name_Operator(Operator):
    def __init__(self, first, second=None) -> None:
        super().__init__(self.name.replace("_", " "), first, second=second)


class TOP(Name_Operator):
    def __init__(self, first) -> None:
        super().__init__(first)


class AS(Name_Operator):
    def __init__(self, first, second, hide=False) -> None:
        super().__init__(first, second=second)
        if hide:
            self.operator = ""
            self.parenthesis = False

    def __str__(self) -> str:
        return super().__str__().replace("  ", " ")


class TO(AS):
    ...


class BETWEEN(Name_Operator):
    def __init__(self, first, second, third) -> None:
        assert (
            type(first) == type(second) == type(third)
        ), "second and third value must be of same data_type"
        super().__init__(first, second=second)
        self.third = third
        self.parenthesis = False

    def __str__(self) -> str:
        text = super().__str__()
        return f"{text} AND {self.third}"


class ESCAPE(Name_Operator):
    def __init__(self, first) -> None:
        assert isinstance(first, str) and (
            len(first) == 1
        ), "ESCAPE character must be a a char like [s, t, etc]"

        # first = f"'{first}'"
        from .datatypes import CONSTANT

        first = CONSTANT(first)

        super().__init__(first)


class LIMIT(Name_Operator):
    def __init__(self, first) -> None:

        super().__init__(first)


class LIKE(Name_Operator):
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


class IN(Name_Operator):
    def __init__(self, first, second: Tuple) -> None:
        from .statements import SELECT

        assert isinstance(second, (tuple, SELECT))
        super().__init__(first, second=second)


class EXISTS(IN):
    ...


class AND(Name_Operator):
    def __init__(self, first, second) -> None:
        super().__init__(first, second=second)


class NOT(Name_Operator):
    parenthesis = False

    def __init__(self, first) -> None:
        super().__init__(first)


class INTO(NOT):
    ...


class OR(Name_Operator):
    def __init__(self, first, second) -> None:
        super().__init__(first, second=second)


class DISTINCT(Name_Operator):
    def __init__(self, first) -> None:
        assert isinstance(first, (str, Columns))
        super().__init__(first)


class COLLATE(Name_Operator):
    parenthesis = False

    def __init__(self, first, second) -> None:
        super().__init__(first, second)


class Name_Operators_F(Name_Operator):
    LTR = False
    parenthesis = False


class IS_NULL(Name_Operators_F):
    def __init__(self, first) -> None:
        super().__init__(first)


class IS_NOT_NULL(Name_Operators_F):
    def __init__(self, first) -> None:
        super().__init__(first)


class ASC(Name_Operators_F):
    def __init__(self, first) -> None:
        super().__init__(first)


class DESC(Name_Operators_F):
    def __init__(self, first) -> None:
        super().__init__(first)


class ON(Name_Operators_F):
    def __init__(self, first, second, third) -> None:
        super().__init__(first, second=second)
        assert isinstance(third, (tuple, Columns))
        if isinstance(third, Columns):
            third.parenthesis = True
        self.third = third

    def __str__(self) -> str:
        text = super().__str__()
        return f"{text} {self.third}"


class _SET(Name_Operator):
    parenthesis = False

    def __init__(self, first, second) -> None:
        super().__init__(first, second=second)


class UNION(_SET):
    def __init__(self, first, second) -> None:
        if isinstance(first, UNION) and not isinstance(second, UNION):
            first, second = second, first

        for u in (first, second):
            if isinstance(u, UNION):
                u.parenthesis = True
        super().__init__(first, second)


class UNION_ALL(UNION):
    ...


class INTERSET(_SET):
    ...


class EXCEPT(_SET):
    "Also called MINUS"
    ...


class JOIN(Statement, _SET):
    @property
    def string(self) -> str:
        return _SET.__str__(self)


class INNER_JOIN(JOIN):
    ...


class LEFT_JOIN(JOIN):
    ...


class RIGHT_JOIN(JOIN):
    ...


class FULL_JOIN(JOIN):
    ...


class FULL_OUTER_JOIN(FULL_JOIN):
    ...


class CROSS_JOIN(JOIN):
    ...


class NATURAL_JOIN(JOIN):
    ...
