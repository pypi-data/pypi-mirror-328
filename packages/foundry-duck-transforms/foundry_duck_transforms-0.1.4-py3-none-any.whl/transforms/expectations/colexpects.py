from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    import _operator

    from pyspark.sql import Column, DataFrame
    from pyspark.sql import functions as F
import operator as op
from collections.abc import Mapping
from dataclasses import dataclass

from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.types import DataType

from transforms.expectations.base import Expectation


@dataclass
class SchemaExpectation(Expectation):
    expected_schema: Mapping[str, "DataType"] | DataType

    def run(self, dataframe_to_verify: "DataFrame"):
        if isinstance(self.expected_schema, DataType):
            res = self.expected_schema == dataframe_to_verify.schema
            if not res:
                raise AssertionError(
                    f"Schema of the dataframe is not as expected. Expected: [{self.expected_schema}] Actual: [{dataframe_to_verify.schema}]"
                )
        else:
            diff = set(dataframe_to_verify.columns).difference(self.expected_schema)
            if len(diff) > 0:
                raise AssertionError(
                    f"Schema of the dataframe is not as expected. Missing columns: {diff}"
                )


@dataclass
class SchemaBuilder:
    equals = SchemaExpectation


class PrimaryKeyExpectation(Expectation):
    def __init__(self, *pk: str):
        self.pk = pk

    def run(self, dataframe_to_verify: "DataFrame"):
        from pyspark.sql import functions as F

        res = dataframe_to_verify.select(
            (F.count_distinct(*self.pk) != F.count("*")).alias("result"),
        ).collect()
        if not res[0][0]:
            raise AssertionError("Primary key is not unique")


@dataclass
class ColExpectationIsIn(Expectation):
    col: str
    values_arr: list[str]

    def run(self, dataframe_to_verify: "DataFrame"):
        from pyspark.sql import functions as F

        cnt = dataframe_to_verify.filter(~F.col(self.col).isin(self.values_arr)).count()
        if cnt > 0:
            raise AssertionError(f"Column {self.col} is not in {self.values_arr}")


@dataclass
class ColExpectation(Expectation):
    col: str
    operation: "Callable[[DataFrame], DataFrame]"

    def run(self, dataframe_to_verify: "DataFrame"):
        result = self.operation(dataframe_to_verify)
        res = result.filter(result["result"] == False).limit(10).collect()
        if len(res) > 0:
            raise AssertionError(
                f"Column {self.col} failed to meet expectations, example issues: {res}"
            )


@dataclass
class OpComparisonExpectation(Expectation):
    colname: str
    operator: "Callable[[_operator._SupportsComparison, _operator._SupportsComparison], Column]"
    value: int | float

    def run(self, dataframe_to_verify: "DataFrame"):
        result = dataframe_to_verify.withColumn(
            "result", self.operator(F.col(self.colname), self.value)
        )
        res = result.filter(result["result"] == False).limit(10).collect()
        if len(res) > 0:
            raise AssertionError(
                f"Column {self.colname} failed to meet expectations, example issues: {res}"
            )


@dataclass
class ColExpectationBuilder:
    col: str

    def is_in(self, *values_arr: str) -> Expectation:
        return ColExpectationIsIn(self.col, list(values_arr))

    def rlike(self, pattern: str) -> Expectation:
        def operation(df: DataFrame) -> DataFrame:
            return df.withColumn("result", F.col(self.col).rlike(pattern))

        return ColExpectation(col=self.col, operation=operation)

    def gt(self, other: int | float) -> Expectation:
        return OpComparisonExpectation(colname=self.col, value=other, operator=op.gt)

    def gte(self, other: int | float) -> Expectation:
        return OpComparisonExpectation(colname=self.col, value=other, operator=op.ge)

    def lt(self, other: int | float) -> Expectation:
        return OpComparisonExpectation(colname=self.col, value=other, operator=op.lt)

    def lte(self, other: int | float) -> Expectation:
        return OpComparisonExpectation(colname=self.col, value=other, operator=op.le)

    def equals(self, other: int | float) -> Expectation:
        return OpComparisonExpectation(colname=self.col, value=other, operator=op.eq)
    def non_null(self) -> Expectation:
        def operation(df: DataFrame) -> DataFrame:
            return df.withColumn("result", F.col(self.col).isNotNull())
        return ColExpectation(col=self.col, operation=operation)

class AllExpectationBuilder(Expectation):
    def __init__(self, *expectations: Expectation):
        self.expectations = expectations

    def run(self, dataframe_to_verify: "DataFrame") -> None:
        for expectation in self.expectations:
            expectation.run(dataframe_to_verify)


class AnyExpectationBuilder(Expectation):
    def __init__(self, *expectations: Expectation):
        self.expectations = expectations

    def run(self, dataframe_to_verify: "DataFrame") -> None:
        num_nonfailures = 0
        for expectation in self.expectations:
            try:
                expectation.run(dataframe_to_verify)
                num_nonfailures += 1
                return
            except AssertionError:
                pass
        if num_nonfailures == 0:
            raise AssertionError("No expectations passed")


any = AnyExpectationBuilder
all = AllExpectationBuilder
schema = SchemaBuilder
primary_key = PrimaryKeyExpectation
col = ColExpectationBuilder
