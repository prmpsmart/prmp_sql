from ..bases import BASE


class KEYWORD(BASE):
    def __init__(self, name, reserved=True) -> None:
        self.RESERVED = reserved
        super().__init__(name)

    def __str__(self):
        return self.NAME
