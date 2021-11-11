from typing import Any, FrozenSet
from .bases import Base
from .datatypes import Data_Type
from .keywords import KEYWORDS


class Built_in_Function(Base):
    def __init__(self, name, args=[], args_ms=[], desc="") -> None:
        self.ARGS = args
        self.DESCRIPTION = desc
        self.ARGS_MODIFIERS = args_ms
        super().__init__(name=name)

    def __str__(self):
        a = len(self.ARGS)
        am = len(self.ARGS_MODIFIERS)
        name = ""
        if am == 1:
            if a == 2:
                name = f"{a[0]} {am[0]} {a[1]}"
        elif am == 2:
            ...
        else:
            if a == 1:
                name = a[0]

        if name:
            name = f"({name})"
        return f"{self.className}{name}"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)


BIT_LENGTH = (Built_in_Function)(
    "BIT_LENGTH", args=[str], desc="The number of bits in a bit string"
)

CAST = (Built_in_Function)(
    "CAST",
    args=[object, Data_Type],
    args_ms=[KEYWORDS.AS],
    desc="The value, converted to the specified data type (e.g., a date converted to a character string)",
)

CHAR_LENGTH = (Built_in_Function)(
    "CHAR_LENGTH", args=[str], desc="The length of a character string"
)

CONVERT = (Built_in_Function)(
    "CONVERT",
    args=[str, function],
    args_ms=[KEYWORDS.USING],
    desc="A string converted as specified by a named conversion function",
)

CURRENT_DATE = Built_in_Function("CURRENT_DATE", desc="The current date")

CURRENT_TIME = (Built_in_Function)(
    "CURRENT_TIME", args=[float], desc="The current time, with the specified precision"
)

CURRENT_TIMESTAMP = (Built_in_Function)(
    "CURRENT_TIMESTAMP",
    args=[float],
    desc="The current date and time, with the specified precision",
)

EXTRACT = (Built_in_Function)(
    "EXTRACT",
    args=[KEYWORDS, object],
    args_ms=[KEYWORDS.FROM],
    desc="The specified part (DAY, HOUR, etc.) from a DATETIME value",
)

LOWER = (Built_in_Function)(
    "LOWER", args=[str], desc="A string converted to all lowercase letters"
)

OCTET_LENGTH = (Built_in_Function)(
    "OCTET_LENGTH", args=[str], desc="The number of 8-bit bytes in a character string"
)

POSITION = (Built_in_Function)(
    "POSITION",
    args=[str, str],
    args_ms=[KEYWORDS.KEYWORDS.IN],
    desc="The position where the target string appears within the source string",
)

SUBSTRING = (Built_in_Function)(
    "SUBSTRING",
    args=[str, str, int],
    args_ms=[KEYWORDS.FROM, KEYWORDS.FOR],
    desc="A portion of the source string, beginning at the nth character, for a length of len",
)

TRANSLATE = (Built_in_Function)(
    "TRANSLATE",
    args=[str, function],
    args_ms=[KEYWORDS.USING],
    desc="A string translated as specified by a named translation function",
)

TRIM_BOTH = (Built_in_Function)(
    "TRIM",
    args=[str, str],
    args_ms=[KEYWORDS.BOTH, KEYWORDS.FROM],
    desc="A string with both leading and trailing occurrences of char trimmed off",
)

TRIM_LEADING = (Built_in_Function)(
    "TRIM",
    args=[str, str],
    args_ms=[KEYWORDS.LEADING, KEYWORDS.FROM],
    desc="A string with any leading occurrences of char trimmed off",
)

TRIM_TRAILING = (Built_in_Function)(
    "TRIM",
    args=[str, str],
    args_ms=[KEYWORDS.TRAILING, KEYWORDS.FROM],
    desc="A string with any trailing occurrences of char trimmed off",
)

UPPER = (Built_in_Function)(
    "UPPER", args=[str], desc="A string converted to all uppercase letters"
)
