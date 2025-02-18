import numpy as np
import pyarrow as pa

from spiral.expressions.base import ExprLike
from spiral.expressions.udf import RefUDF


def read(
    expr: ExprLike,
    indexes: ExprLike | int | list[int] | None = None,
    window: ExprLike | tuple[tuple[int, int], tuple[int, int]] | None = None,
    boundless: ExprLike | bool | None = None,
):
    """
    Read referenced cell in a `TIFF` format. Requires `rasterio` to be installed.

    Args:
        expr: The referenced `TIFF` bytes.
        indexes: The band indexes to read. Defaults to first band. The first dimension of the result's `shape` field
            is either 1 or the number of indexes.
        window: The window to read. In format (row_range_tuple, col_range_tuple). Defaults to full window.
        boundless: If `True`, windows that extend beyond the dataset's extent
            are permitted and partially or completely filled arrays will be returned as appropriate.

    Returns:
        An array where each element is a NumPy array represented as a struct with fields:
            bytes: Array bytes with type `pa.large_binary()`.
            shape: Array shape with type `pa.list_(pa.uint32(), 3)`.
            dtype: String representation of NumPy dtype with type `pa.string()`.

    Example:
        A way to get the i-th element in the result as NumPy array:

        ```
        array: np.ndarray = np.frombuffer(
            result["bytes"][i].as_py(),
            dtype=np.dtype(result["dtype"][i].as_py()),
        ).reshape(tuple(result["shape"][i].as_py()))
        ```
    """
    try:
        import rasterio  # noqa: F401
    except ImportError:
        raise ImportError("`rasterio` is required for tiff.read")

    return TiffReadUDF()(expr, indexes, window, boundless)


def crop(
    expr: ExprLike,
    shape: ExprLike,
):
    """
    Crop shapes out of the referenced cell in a `TIFF` format. Requires `rasterio` to be installed.

    Args:
        expr: The referenced `TIFF` bytes.
        shape: [GeoJSON-like](https://geojson.org/) shape.

    Returns:
        An array where each element is a NumPy array represented as a struct with fields:
            bytes: Array bytes with type `pa.large_binary()`.
            shape: Array shape with type `pa.list_(pa.uint32(), 3)`.
            dtype: String representation of NumPy dtype with type `pa.string()`.

    Example:
        A way to get the i-th element in the result as NumPy array:

        ```
        array: np.ndarray = np.frombuffer(
            result["bytes"][i].as_py(),
            dtype=np.dtype(result["dtype"][i].as_py()),
        ).reshape(tuple(result["shape"][i].as_py()))
        ```
    """
    try:
        import rasterio  # noqa: F401
    except ImportError:
        raise ImportError("`rasterio` is required for tiff.crop")

    return TiffCropUDF()(expr, shape)


class TiffReadUDF(RefUDF):
    RES_DTYPE: pa.DataType = pa.struct(
        [
            pa.field("bytes", pa.large_binary()),
            pa.field("shape", pa.list_(pa.uint32(), 3)),
            pa.field("dtype", pa.string()),
        ]
    )

    def __init__(self):
        super().__init__("tiff.read")

    def return_type(self, *input_types: pa.DataType) -> pa.DataType:
        return TiffReadUDF.RES_DTYPE

    def invoke(self, fp, *input_args: pa.Array) -> pa.Array:
        try:
            import rasterio
        except ImportError:
            raise ImportError("`rasterio` is required for tiff.read")

        from rasterio.windows import Window

        if len(input_args) != 4:
            raise ValueError("tiff.read expects exactly 4 arguments: expr, indexes, window, boundless")

        _, indexes, window, boundless = input_args

        indexes = indexes[0].as_py()
        if indexes is not None and not isinstance(indexes, int) and not isinstance(indexes, list):
            raise ValueError(f"tiff.read expects indexes to be None or an int or a list, got {indexes}")

        boundless = boundless[0].as_py()
        if boundless is not None and not isinstance(boundless, bool):
            raise ValueError(f"tiff.read expects boundless to be None or a bool, got {boundless}")

        window = window[0].as_py()
        if window is not None:
            if len(window) != 2:
                raise ValueError(f"tiff.read window invalid, got {window}")
            window = Window.from_slices(slice(*window[0]), slice(*window[1]), boundless=boundless or False)

        opener = _VsiOpener(fp)
        with rasterio.open("ref", opener=opener) as src:
            src: rasterio.DatasetReader
            # TODO(marko): We know the size and dtype so we should be able to preallocate the result and read into it.
            #   This matters more if we want to rewrite this function to work with multiple inputs at once, in which
            #   case we should first consider using Rust GDAL bindings - I believe rasterio uses GDAL under the hood.
            result: np.ndarray = src.read(indexes=indexes, window=window)
            return pa.array(
                [
                    {
                        "bytes": result.tobytes(),
                        "shape": list(result.shape),
                        "dtype": str(result.dtype),
                    }
                ],
                type=TiffReadUDF.RES_DTYPE,
            )


class TiffCropUDF(RefUDF):
    RES_DTYPE: pa.DataType = pa.struct(
        [
            pa.field("bytes", pa.large_binary()),
            pa.field("shape", pa.list_(pa.uint32()), 3),
            pa.field("dtype", pa.string()),
        ]
    )

    def __init__(self):
        super().__init__("tiff.crop")

    def return_type(self, *input_types: pa.DataType) -> pa.DataType:
        return TiffCropUDF.RES_DTYPE

    def invoke(self, fp, *input_args: pa.Array) -> pa.Array:
        try:
            import rasterio
        except ImportError:
            raise ImportError("`rasterio` is required for tiff.crop")

        from rasterio.mask import mask as rio_mask

        if len(input_args) != 2:
            raise ValueError("tiff.crop expects exactly 2 arguments: expr, shape")

        _, shape = input_args

        shape = shape[0].as_py()
        if shape is None:
            raise ValueError("tiff.crop expects shape to be a GeoJSON-like shape")

        opener = _VsiOpener(fp)
        with rasterio.open("ref", opener=opener) as src:
            src: rasterio.DatasetReader
            result, _ = rio_mask(src, shapes=[shape], crop=True)
            result: np.ndarray
            return pa.array(
                [
                    {
                        "bytes": result.tobytes(),
                        "shape": list(result.shape),
                        "dtype": str(result.dtype),
                    }
                ],
                type=TiffCropUDF.RES_DTYPE,
            )


class _VsiOpener:
    """
    VSI file opener which returns a constant file-like on open.

    Must match https://rasterio.readthedocs.io/en/stable/topics/vsi.html#python-file-and-filesystem-openers spec but
    only `open` is needed when going through rasterio.
    """

    def __init__(self, file_like):
        self._file_like = file_like

    def open(self, _path, mode):
        if mode not in {"r", "rb"}:
            raise ValueError(f"Unsupported mode: {mode}")
        return self._file_like

    def isdir(self, _):
        return False

    def isfile(self, _):
        return False

    def mtime(self, _):
        return 0

    def size(self, _):
        return self._file_like.size()

    def modified(self, _):
        raise NotImplementedError
