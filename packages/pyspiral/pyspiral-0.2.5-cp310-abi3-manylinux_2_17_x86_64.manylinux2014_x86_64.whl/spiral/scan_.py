from collections.abc import Iterator
from datetime import datetime
from typing import TYPE_CHECKING, Any

import pyarrow as pa
from opentelemetry import trace

from spiral.core.core import TableScan
from spiral.core.spec import KeyRange, Schema
from spiral.expressions.base import ExprLike

if TYPE_CHECKING:
    import dask.dataframe as dd
    import pandas as pd
    import polars as pl
    from datasets import iterable_dataset

tracer = trace.get_tracer("pyspiral.client.scan")


def scan(
    *projections: ExprLike,
    where: ExprLike | None = None,
    asof: datetime | int | str = None,
    exclude_keys: bool = False,
    # TODO(marko): Support config.
    # config: Config | None = None,
) -> "Scan":
    """Starts a read transaction on the spiral.

    Args:
        projections: a set of expressions that return struct arrays.
        where: a query expression to apply to the data.
        asof: only data written before the given timestamp will be returned, caveats around compaction.
        exclude_keys: whether to exclude the key columns in the scan result, defaults to False.
    """
    from spiral import expressions as se

    # Combine all projections into a single struct.
    projection = se.merge(*projections)
    if where is not None:
        where = se.lift(where)

    return Scan(
        TableScan(
            projection.__expr__,
            filter=where.__expr__ if where else None,
            asof=asof,
            exclude_keys=exclude_keys,
        ),
        # config=config,
    )


class Scan:
    """Scan object."""

    def __init__(
        self,
        scan: TableScan,
        # TODO(marko): Support config.
        # config: Config | None = None,
    ):
        # NOTE(ngates): this API is a little weird. e.g. if the query doesn't define an asof, it is resolved
        #  when we wrap it into a core.Scan. Should we expose a Query object in the Python API that's reusable
        #  and will re-resolve the asof? Or should we just expose a scan that fixes the asof at construction time?
        self._scan = scan

    @property
    def metrics(self) -> dict[str, Any]:
        """Returns metrics about the scan."""
        return self._scan.metrics()

    @property
    def schema(self) -> Schema:
        """Returns the schema of the scan."""
        return self._scan.schema()

    def is_empty(self) -> bool:
        """Check if the Spiral is empty for the given key range.

        **IMPORTANT**: False negatives are possible, but false positives are not,
            i.e. is_empty can return False and scan can return zero rows.
        """
        return self._scan.is_empty()

    def to_record_batches(self, key_table: pa.Table | pa.RecordBatchReader | None = None) -> pa.RecordBatchReader:
        """Read as a stream of RecordBatches.

        Args:
            key_table: a table of keys to "take" (including aux columns for cell-push-down).
        """
        if isinstance(key_table, pa.RecordBatchReader):
            raise NotImplementedError("RecordBatchReader is not supported as key_table")

        # Prefix non-key columns in the key table with # (auxiliary) to avoid conflicts with the scan schema.
        if key_table is not None:
            key_columns = list(self._scan.key_schema().to_arrow().names)
            key_table = key_table.rename_columns(
                {name: f"#{name}" if name not in key_columns else name for name in key_table.schema.names}
            )

        return self._scan.to_record_batches(aux_table=key_table)

    def to_table(self) -> pa.Table:
        """Read into a single PyArrow Table."""
        return self.to_record_batches().read_all()

    def to_dask(self) -> "dd.DataFrame":
        """Read into a Dask DataFrame.

        Requires the `dask` package to be installed.
        """
        import dask.dataframe as dd
        import pandas as pd

        def _read_key_range(key_range: KeyRange) -> pd.DataFrame:
            # TODO(ngates): we need a way to preserve the existing asofs? Should we copy CoreScan instead of Query?
            raise NotImplementedError()

        # Fetch a set of partition ranges
        return dd.from_map(_read_key_range, self.split())

    def to_pandas(self) -> "pd.DataFrame":
        """Read into a Pandas DataFrame.

        Requires the `pandas` package to be installed.
        """
        return self.to_table().to_pandas()

    def to_polars(self) -> "pl.DataFrame":
        """Read into a Polars DataFrame.

        Requires the `polars` package to be installed.
        """
        import polars as pl

        # TODO(ngates): PR PyArrow to support lazy datasets
        return pl.from_arrow(self.to_record_batches())

    def to_pytorch(self) -> "iterable_dataset.IterableDataset":
        """Returns an iterable dataset that can be used to build a `pytorch.DataLoader`.

        Requires the `datasets` package to be installed.
        """
        from datasets.iterable_dataset import ArrowExamplesIterable, IterableDataset

        def _generate_tables(**kwargs) -> Iterator[tuple[int, pa.Table]]:
            stream = self.to_record_batches()

            # This key is unused when training with IterableDataset.
            # Default implementation returns shard id, e.g. parquet row group id.
            for i, rb in enumerate(stream):
                yield i, pa.Table.from_batches([rb], stream.schema)

        # NOTE: Type annotation Callable[..., tuple[str, pa.Table]] is wrong. The return value must be iterable.
        ex_iterable = ArrowExamplesIterable(generate_tables_fn=_generate_tables, kwargs={})
        return IterableDataset(ex_iterable=ex_iterable)

    def split(self) -> list[KeyRange]:
        return self._scan.split()

    def debug(self):
        # Visualizes the scan, mainly for debugging purposes.
        # NOTE: This is not part of the API and may disappear at any moment.
        from spiral.debug import show_scan

        show_scan(self._scan)
