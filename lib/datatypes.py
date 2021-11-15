from .bases import Name_Space_Base


class Data_Type(Name_Space_Base):
    ABBRS = []
    DESCRIPTION = ""
    MODIFIERS = []

    def __init__(self, column, first=None, second=None) -> None:
        assert isinstance(
            column, str
        ), "Data_Type only accept string type as column name"
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


class Just_Name(Data_Type):
    def __init__(self, name):
        super().__init__(name)


class One_Value(Data_Type):
    def __init__(self, name, first):
        super().__init__(name, first)


class Two_Value(Data_Type):
    def __init__(self, name, first, second):
        super().__init__(name, first, second)


class TEXT(Just_Name):
    ...


class CHARACTER(One_Value):
    ABBRS = ["CHAR"]
    DESCRIPTION = "Fixed-length character strings"

    def __init__(self, name, first=255):
        super().__init__(name, first)


class CHAR(CHARACTER):
    ...


class CHARACTER_VARYING(One_Value):
    ABBRS = ["CHAR VARYING", "VARCHAR"]
    DESCRIPTION = "Variable-length character strings"

    def __init__(self, name, first=255):
        super().__init__(name, first)


class VARCHAR(CHARACTER_VARYING):
    ...


class CHARACTER_LARGE_OBJECT(One_Value):
    ABBRS = ["CLOB"]
    DESCRIPTION = "Large fixed-length character strings"


class CLOB(CHARACTER_LARGE_OBJECT):
    ...


class NATIONAL_CHARACTER(One_Value):
    ABBRS = "NATIONAL CHAR", "NCHAR"
    DESCRIPTION = "Fixed-length national character strings"


class NATIONAL_CHARACTER_VARYING(One_Value):
    ABBRS = "NATIONAL CHAR VARYING", "NCHAR"
    DESCRIPTION = "Variable-length national character strings"


class NATIONAL_CHARACTER_LARGE_OBJECT(One_Value):
    ABBRS = ["NCLOB"]
    DESCRIPTION = "Large variable-length national character strings"


class BIT(One_Value):
    DESCRIPTION = "Fixed-length bit strings"


class BIT_VARYING(One_Value):
    DESCRIPTION = "Variable-length bit strings"


class BLOB(Just_Name):
    ...


class BOOLEAN(Just_Name):
    ...


class INTEGER(Just_Name):
    ABBRS = ["INT"]
    DESCRIPTION = "Integers"


class INT(INTEGER):
    ...


class SMALLINT(Just_Name):
    DESCRIPTION = "Small integers"


class NUMERIC(Two_Value):
    FUNCTIONAL_ARGS = [float, int]
    DESCRIPTION = "Decimal numbers"


class DECIMAL(Two_Value):
    ABBRS = ["DEC"]
    FUNCTIONAL_ARGS = [float, int]
    DESCRIPTION = "Decimal numbers"


class FLOAT(One_Value):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Floating point numbers"


class REAL(Just_Name):
    DESCRIPTION = "Low-precision floating point numbers"


class DOUBLE_PRECISION(Just_Name):
    DESCRIPTION = "High-precision floating point numbers"


class DATE(Just_Name):
    DESCRIPTION = "Calendar dates"


class TIME(One_Value):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Clock times"


class TIME_WITH_TIME_ZONE(One_Value):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Clock times with time zones"


class TIMESTAMP(One_Value):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Dates and times"


class TIMESTAMP_WITH_TIME_ZONE(One_Value):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Dates and times with time zones"


class INTERVAL(Data_Type):
    DESCRIPTION = "Time intervals"


class XML(Data_Type):
    # (type modifier [secondary type modifier]) :
    DESCRIPTION = "Character data formatted as Extensible Markup Language (XML)"
