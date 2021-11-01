from .functions import Function
from .clauses import FROM, GROUP_BY, HAVING, ORDER_BY, WHERE
from .bases import Base, Columns


class SELECT(Base):

    DESCRIPTION = ""
    parenthesis = False

    def __init__(
        self,
        columns,
        from_,
        where=None,
        group=None,
        having=None,
        order=None,
        into=None,
        distinct=False,
        all=False,
    ) -> None:
        """
        :columns: instance of Columns|Column
        :from_: instance of FROM
        :where: instance of WHERE
        :group: instance of GROUP
        :having: instance of HAVING
        :order: instance of ORDER
        :into: instance of INTO_TABLE
        """
        if columns:
            assert isinstance(
                columns, (str, Columns, Function)
            ), f"type ({str}, {Columns}, {Function}) is expected not {type(columns)}."
        if from_:
            assert isinstance(from_, FROM)
        if where:
            assert isinstance(where, WHERE)
        if group:
            assert isinstance(group, GROUP_BY)
        if having:
            assert isinstance(having, HAVING)
        if order:
            assert isinstance(order, ORDER_BY)
        # assert isinstance(into, (str, INTO_TABLE))

        self.columns = columns
        self.from_ = from_
        self.where = where
        self.group = group
        self.having = having
        self.order = order
        self.into = into

        self.distinct = distinct
        self.all = all

        super()

    def __str__(self):
        all_dis = " ALL " if self.all else " DISTINCT " if self.distinct else " "

        default = f"{self.name}{all_dis}{self.columns}"
        if self.into:
            default += f" {self.into}"
        default += f" {self.from_}"
        if self.where:
            default += f" {self.where}"
        if self.group:
            default += f" {self.group}"
        if self.having:
            default += f" {self.having}"
        if self.order:
            default += f" {self.order}"

        if self.parenthesis:
            default = f"({default})"

        return default


class DELETE(Base):
    def __init__(self) -> None:
        super().__init__()
