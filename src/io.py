"""
Load ACS B15003 (Educational Attainment) and B23025 (Employment Status) CSV files.
Census CSVs have two header rows; we use the first (column codes) and skip the second (labels).
"""

import pandas as pd
from pathlib import Path

from .config import B15003_DATA, B23025_DATA


def load_b15003(path: Path = B15003_DATA) -> pd.DataFrame:
    """Load ACS B15003 - Educational Attainment for Population 25 Years and Over."""
    df = pd.read_csv(path, skiprows=[1])
    # Coerce numeric columns; Census uses '-' or '*****' for suppressed
    for col in df.columns:
        if col in ("GEO_ID", "NAME"):
            continue
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def load_b23025(path: Path = B23025_DATA) -> pd.DataFrame:
    """Load ACS B23025 - Employment Status for Population 16 Years and Over."""
    df = pd.read_csv(path, skiprows=[1])
    for col in df.columns:
        if col in ("GEO_ID", "NAME"):
            continue
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df
