from .built_in_funtions import Built_in_Function


class Aggregate_Function(Built_in_Function):
    def __init__(self, name, desc) -> None:
        super().__init__(name, args=[str], desc=desc)


AVG = Aggregate_Function("AVG", desc="Average value for rows within the group")
COUNT = Aggregate_Function("COUNT", desc="Count of values for rows within the group")
MAX = Aggregate_Function("MAX", desc="Maximum value within the group")
MIN = Aggregate_Function("MIN", desc="Minimum value within the group")
SUM = Aggregate_Function("SUM", desc="Sum of values within the group")
