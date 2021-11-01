from .bases import Base


class SELECT(Base):
    DESCRIPTION = ""

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
        :group: instance of GROUP
        :having: instance of HAVING
        :order: instance of ORDER
        :into: instance of INTO_TABLE
        """
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

        return default


class DELETE(Base):
    def __init__(self) -> None:
        super().__init__()
