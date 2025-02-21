from functools import lru_cache, partial

import pandas as pd
from genno import Key

from ixmp.report import common


def dims_for_qty(data):
    """Return the list of dimensions for *data*.

    If *data* is a :class:`pandas.DataFrame`, its columns are processed;
    otherwise it must be a list.

    :data:`.RENAME_DIMS` is used to rename dimensions.
    """
    # List of the dimensions
    dims = data.columns.tolist() if isinstance(data, pd.DataFrame) else list(data)

    # Remove columns containing values or units; dimensions are the remainder
    for col in "value", "lvl", "mrg", "unit":
        try:
            dims.remove(col)
        except ValueError:
            continue

    # Rename dimensions
    return [common.RENAME_DIMS.get(d, d) for d in dims]


def keys_for_quantity(ix_type, name, scenario):
    """Return keys for *name* in *scenario*."""
    from .operator import data_for_quantity

    # Retrieve names of the indices of the ixmp item, without loading the data
    dims = dims_for_qty(scenario.idx_names(name))

    # Column for retrieving data
    column = "value" if ix_type == "par" else "lvl"

    # A computation to retrieve the data
    result = [
        (
            Key(name, dims),
            partial(data_for_quantity, ix_type, name, column),
            "scenario",
            "config",
        )
    ]

    # Add the marginal values at full resolution, but no aggregates
    if ix_type == "equ":
        result.append(
            (
                Key(f"{name}-margin", dims),
                partial(data_for_quantity, ix_type, name, "mrg"),
                "scenario",
                "config",
            )
        )

    return result


@lru_cache(1)
def get_reversed_rename_dims():
    return {v: k for k, v in common.RENAME_DIMS.items()}


def __getattr__(name: str):
    if name == "RENAME_DIMS":
        return common.RENAME_DIMS
    else:
        raise AttributeError(name)
