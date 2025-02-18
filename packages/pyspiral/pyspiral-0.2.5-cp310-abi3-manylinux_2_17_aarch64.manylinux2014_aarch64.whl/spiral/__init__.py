"""Python client for the Spiral warehouse."""

from spiral import _lib
from spiral.catalog import Spiral
from spiral.scan_ import Scan, scan
from spiral.table import Table

# Eagerly import the Spiral library
assert _lib, "Spiral library"

__all__ = ["scan", "Scan", "Table", "Spiral"]
