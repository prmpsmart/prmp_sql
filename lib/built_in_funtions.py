from typing import Any
from .bases import CONSTANT, Base, function
from .keywords import KEYWORDS


class Built_in_Function(Base):
    ARGS_MODIFIERS = []

    def __init__(self, *args) -> None:
        self.len = len(args)
        self.len_a = len(self.ARGS_MODIFIERS)
        self.args = args

    def __str__(self) -> str:
        name = self.name
        l = self.len
        la = self.len_a
        args = self.args
        args_m = self.ARGS_MODIFIERS

        if l:
            name += "("
            if l == 1:
                name += f"{CONSTANT(self.args[0])}"
            elif l == 2 and la == 1:
                name += f"{args[0]} {args_m[0]} {args[1]}"
            elif l == 2 and la == 2:
                name += f"{args_m[0]} {args[0]} {args_m[1]} {args[1]}"
            name += ")"
        return name


class BIT_LENGTH(Built_in_Function):
    "The number of bits in a bit string"

    def __init__(self, string):
        assert isinstance(string, str)
        super().__init__(CONSTANT(string))


class CAST(Built_in_Function):
    "The value, converted to the specified data type (e.g., a date converted to a character string)"
    ARGS_MODIFIERS = [KEYWORDS.AS]

    def __init__(self, value, data_type):
        super().__init__(value, data_type)


class CHAR_LENGTH(BIT_LENGTH):
    "The length of a character string"


class CONVERT(Built_in_Function):
    "A string converted as specified by a named conversion function"
    ARGS_MODIFIERS = [KEYWORDS.USING]

    def __init__(self, string, conv):
        super().__init__(string, conv)


class CURRENT_DATE(Built_in_Function):
    "The current date"

    def __init__(self):
        super().__init__()


class CURRENT_TIME(Built_in_Function):
    "The current time, with the specified precision"

    def __init__(self, precision):
        assert isinstance(precision, (float, int))
        super().__init__(precision)


class CURRENT_TIMESTAMP(Built_in_Function):
    "The current date and time, with the specified precision"

    def __init__(self, precision):
        assert isinstance(precision, (float, int))
        super().__init__(precision)


class EXTRACT(Built_in_Function):
    "The specified part (DAY, HOUR, etc.) from a DATETIME value"
    ARGS_MODIFIERS = [KEYWORDS.FROM]

    def __init__(self, part, source):
        super().__init__(part, source)


class LOWER(BIT_LENGTH):
    "A string converted to all lowercase letters"


class OCTET_LENGTH(BIT_LENGTH):
    "The number of 8-bit bytes in a character string"


class POSITION(Built_in_Function):
    "The position where the target string appears within the source string"
    ARGS_MODIFIERS = [KEYWORDS.IN]

    def __init__(self, target, source):
        super().__init__(target, source)


class SUBSTRING(Built_in_Function):
    "A portion of the source string, beginning at the nth character, for a length of len"
    ARGS_MODIFIERS = [KEYWORDS.FROM, KEYWORDS.FOR]

    def __init__(self, source, n, len):
        super().__init__(source, n, len)


class TRANSLATE(Built_in_Function):
    "A string translated as specified by a named translation function"
    ARGS_MODIFIERS = [KEYWORDS.USING]

    def __init__(self, string, trans):
        super().__init__(CONSTANT(string), trans)


class TRIM(Built_in_Function):
    "A string with char trimmed off"
    ARGS_MODIFIERS = [KEYWORDS.FROM]
    ADD_MODIFIERS = None

    def __init__(self, char, string) -> None:
        if self.ADD_MODIFIERS:
            self.ARGS_MODIFIERS.insert(0, self.ADD_MODIFIERS)
        super().__init__(CONSTANT(char), CONSTANT(string))

    @property
    def name(self):
        nm = super().name
        return nm.split("_")[0]

class TRIM_BOTH(TRIM):
    "A string with both leading and trailing occurrences of char trimmed off"
    ADD_MODIFIERS = KEYWORDS.BOTH


class TRIM_LEADING(TRIM):
    "A string with any leading occurrences of char trimmed off"
    ADD_MODIFIERS = KEYWORDS.LEADING


class TRIM_TRAILING(TRIM):
    "A string with any trailing occurrences of char trimmed off"
    ADD_MODIFIERS = KEYWORDS.TRAILING


class UPPER(BIT_LENGTH):
    "A string converted to all uppercase letters"
