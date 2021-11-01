from bases import BASE


class Data_Type(BASE):
    ABBRS = []
    DESCRIPTION = ""
    MODIFIERS = []
    FUNCTIONAL = False

    def __init__(self) -> None:
        super().__init__(self.name)

    def __str__(self):
        name = self.name
        if "_" in name:
            name = name.replace("_", " ")
        return name


class Functional_Data_Type(Data_Type):
    MODIFIERS = []
    FUNCTIONAL = True
    FUNCTIONAL_ARGS = [int]

    def __str__(self):
        return super().__str__()


class CHARACTER(Functional_Data_Type):
    ABBRS = ["CHAR"]
    DESCRIPTION = "Fixed-length character strings"


class CHARACTER_VARYING(Functional_Data_Type):
    ABBRS = ["CHAR VARYING", "VARCHAR"]
    DESCRIPTION = "Variable-length character strings"


class CHARACTER_LARGE_OBJECT(Functional_Data_Type):
    ABBRS = ["CLOB"]
    DESCRIPTION = "Large fixed-length character strings"


class NATIONAL_CHARACTER(Functional_Data_Type):
    ABBRS = "NATIONAL CHAR", "NCHAR"
    DESCRIPTION = "Fixed-length national character strings"


class NATIONAL_CHARACTER_VARYING(Functional_Data_Type):
    ABBRS = "NATIONAL CHAR VARYING", "NCHAR"
    DESCRIPTION = "Variable-length national character strings"


class NATIONAL_CHARACTER_LARGE_OBJECT(Functional_Data_Type):
    ABBRS = ["NCLOB"]
    DESCRIPTION = "Large variable-length national character strings"


class BIT(Functional_Data_Type):
    DESCRIPTION = "Fixed-length bit strings"


class BIT_VARYING(Functional_Data_Type):
    DESCRIPTION = "Variable-length bit strings"


class INTEGER(Data_Type):
    ABBRS = ["INT"]
    DESCRIPTION = "Integers"


class SMALLINT(Data_Type):
    DESCRIPTION = "Small integers"


class NUMERIC(Functional_Data_Type):
    FUNCTIONAL_ARGS = [float, int]
    DESCRIPTION = "Decimal numbers"


class DECIMAL(Functional_Data_Type):
    ABBRS = ["DEC"]
    FUNCTIONAL_ARGS = [float, int]
    DESCRIPTION = "Decimal numbers"


class FLOAT(Functional_Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Floating point numbers"


class REAL(Data_Type):
    DESCRIPTION = "Low-precision floating point numbers"


class DOUBLE_PRECISION(Data_Type):
    DESCRIPTION = "High-precision floating point numbers"


class DATE(Data_Type):
    DESCRIPTION = "Calendar dates"


class TIME(Functional_Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Clock times"


class TIME_WITH_TIME_ZONE(Functional_Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Clock times with time zones"


class TIMESTAMP(Functional_Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Dates and times"


class TIMESTAMP_WITH_TIME_ZONE(Functional_Data_Type):
    FUNCTIONAL_ARGS = [float]
    DESCRIPTION = "Dates and times with time zones"


class INTERVAL(Data_Type):
    DESCRIPTION = "Time intervals"


class XML(Functional_Data_Type):
    # (type modifier [secondary type modifier]) :
    DESCRIPTION = "Character data formatted as Extensible Markup Language (XML)"
