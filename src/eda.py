"""
Descriptive statistics and distribution exploration for the merged county dataset.
"""

from typing import List, Optional

import pandas as pd


def summary_stats(df: pd.DataFrame, numeric_cols: Optional[List[str]] = None) -> pd.DataFrame:
    """Summary statistics for key numeric variables."""
    if numeric_cols is None:
        numeric_cols = ["percent_bachelors_plus", "unemployment_rate"]
    return df[numeric_cols].describe()


def summary_by_region(
    df: pd.DataFrame,
    group_col: str = "region",
    value_cols: Optional[List[str]] = None,
) -> pd.DataFrame:
    """
    Summary by region: count and mean of key variables per group.
    Supports ANOVA interpretation (sample size and mean differences per region).
    """
    if value_cols is None:
        value_cols = ["percent_bachelors_plus", "unemployment_rate"]
    order = ["Northeast", "Midwest", "South", "West"]
    means = df.groupby(group_col)[value_cols].mean()
    means.columns = [f"mean_{c}" for c in means.columns]
    counts = df.groupby(group_col).size().rename("count")
    summary = means.join(counts).reindex(order).reset_index()
    return summary


def correlation_matrix(df: pd.DataFrame, numeric_cols: Optional[List[str]] = None) -> pd.DataFrame:
    """Pearson correlation matrix for numeric columns."""
    if numeric_cols is None:
        numeric_cols = ["percent_bachelors_plus", "unemployment_rate"]
    return df[numeric_cols].corr(method="pearson")
