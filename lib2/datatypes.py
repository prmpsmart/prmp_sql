from .bases import Name_Space_Base, Base


class Data_Type(Name_Space_Base):
    ABBRS = []
    DESCRIPTION = ""
    MODIFIERS = []

    def __init__(self, column, first=None, second=None) -> None:
        if second:
            assert first, "first must be provided to use second"
        for a in [first, second]:
            if a:
                assert isinstance(a, (int, float)), "Must be type [int, float]"

        self.column = column
        self.first = first
        self.second = second

    def __str__(self):
        text = f"{self.column} {self.name}"
        if self.first:
            text += f"({self.first}"
            if self.second:
                text += f", {self.second}"
            text += ")"
        return text


class CHARACTER(Data_Type):
    ABBRS = ["CHAR"]
    DESCRIPTION = "Fixed-length character strings"


class CHARACTER_VARYING(Data_Type):
    ABBRS = ["CHAR VARYING", "VARCHAR"]
    DESCRIPTION = "Variable-length character strings"


class CHARACTER_LARGE_OBJECT(Data_Type):
    ABBRS = ["CLOB"]
    DESCRIPTION = "Large fixed-length character strings"


class NATIONAL_CHARACTER(Data_Type):
    ABBRS = "NATIONAL CHAR", "NCHAR"
    DESCRIPTION = "Fixed-length national character strings"


class NATIONAL_CHARACTER_VARYING(Data_Type):
    ABBRS = "NATIONAL CHAR VARYING", "NCHAR"
    DESCRIPTION = "Variable-length national character strings"


class NATIONAL_CHARACTER_LARGE_OBJECT(Data_Type):
    ABBRS = ["NCLOB"]
    DESCRIPTION = "Large variable-length national character strings"


class BIT(Data_Type):
    DESCRIPTION = "Fixed-length bit strings"


class BIT_VARYING(Data_Type):
    DESCRIPTION = "Variable-length bit strings"


class INTEGER(Data_Type):
    ABBRS = ["INT"]
    DESCRIPTION = "Integers"


class SMALLINT(Data_Type):
    DESCRIPTION = "Small integers"


class NUMERIC(Data_Type):
    FUNCTIONAL_ARGS = [float, int]
    DESCRIPTION = "Decimal numbers"


class DECIMAL(Data_Type):
    ABBRS = ["DEC"]
    FUNCTIONAL_ARGS = [float, int]
    DESCRIPTION = "Decimal numbers"


class FLOAT(Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Floating point numbers"


class REAL(Data_Type):
    DESCRIPTION = "Low-precision floating point numbers"


class DOUBLE_PRECISION(Data_Type):
    DESCRIPTION = "High-precision floating point numbers"


class DATE(Data_Type):
    DESCRIPTION = "Calendar dates"


class TIME(Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Clock times"


class TIME_WITH_TIME_ZONE(Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Clock times with time zones"


class TIMESTAMP(Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Dates and times"


class TIMESTAMP_WITH_TIME_ZONE(Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Dates and times with time zones"


class INTERVAL(Data_Type):
    DESCRIPTION = "Time intervals"


class XML(Data_Type):
    # (type modifier [secondary type modifier]) :
    DESCRIPTION = "Character data formatted as Extensible Markup Language (XML)"


class CONSTANT(Base):
    def __init__(self, value) -> None:
        valid = (str, int, float)
        assert isinstance(value, valid), f"value must be of type {valid}"
        if isinstance(value, (int, float)):
            self.value = value
        elif isinstance(value, str):
            self.value = f"'{value}'"

    def __str__(self) -> str:
        return self.value
