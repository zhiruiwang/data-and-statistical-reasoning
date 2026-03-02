"""
Merge education (B15003) and employment (B23025) on GEO_ID;
derive percent bachelor's or higher and unemployment rate;
add Census region; drop rows with missing/suppressed values.
"""

import pandas as pd
import numpy as np

from .config import RANDOM_SEED

# U.S. Census Bureau state FIPS to region (Census regions)
STATE_FIPS_TO_REGION = {
    "09": "Northeast", "23": "Northeast", "25": "Northeast", "33": "Northeast",
    "44": "Northeast", "50": "Northeast", "34": "Northeast", "36": "Northeast", "42": "Northeast",
    "17": "Midwest", "18": "Midwest", "26": "Midwest", "39": "Midwest", "55": "Midwest",
    "19": "Midwest", "20": "Midwest", "27": "Midwest", "29": "Midwest", "31": "Midwest", "38": "Midwest", "46": "Midwest",
    "01": "South", "05": "South", "10": "South", "11": "South", "12": "South", "13": "South",
    "21": "South", "22": "South", "24": "South", "28": "South", "37": "South", "40": "South",
    "45": "South", "47": "South", "48": "South", "51": "South", "54": "South",
    "02": "West", "04": "West", "06": "West", "08": "West", "15": "West", "16": "West",
    "30": "West", "32": "West", "35": "West", "41": "West", "49": "West", "53": "West", "56": "West",
}


def extract_state_fips(geo_id: str) -> str:
    """Extract 2-digit state FIPS from GEO_ID (e.g. '0500000US01001' -> '01')."""
    if pd.isna(geo_id) or "US" not in str(geo_id):
        return ""
    return str(geo_id).split("US")[1][:2]


def add_region(df: pd.DataFrame, geo_col: str = "GEO_ID") -> pd.DataFrame:
    """Add Census region from GEO_ID."""
    state_fips = df[geo_col].astype(str).map(extract_state_fips)
    df = df.copy()
    df["state_fips"] = state_fips
    df["region"] = state_fips.map(STATE_FIPS_TO_REGION)
    return df


def derive_education_vars(df_edu: pd.DataFrame) -> pd.DataFrame:
    """
    From B15003: total pop 25+, bachelor's + master's + professional + doctorate.
    percent_bachelors_plus = (B15003_022E + 023 + 024 + 025) / B15003_001E * 100.
    """
    total = df_edu["B15003_001E"]
    bachelors_plus = (
        df_edu["B15003_022E"]  # Bachelor's
        + df_edu["B15003_023E"]  # Master's
        + df_edu["B15003_024E"]  # Professional
        + df_edu["B15003_025E"]  # Doctorate
    )
    df_edu = df_edu.copy()
    df_edu["percent_bachelors_plus"] = np.where(
        total > 0,
        (bachelors_plus / total) * 100,
        np.nan
    )
    return df_edu


def derive_employment_vars(df_emp: pd.DataFrame) -> pd.DataFrame:
    """
    From B23025: unemployment_rate = Unemployed / Civilian labor force * 100.
    B23025_005E = Unemployed, B23025_003E = Civilian labor force.
    """
    labor_force = df_emp["B23025_003E"]
    unemployed = df_emp["B23025_005E"]
    df_emp = df_emp.copy()
    df_emp["unemployment_rate"] = np.where(
        labor_force > 0,
        (unemployed / labor_force) * 100,
        np.nan
    )
    return df_emp


def merge_and_clean(
    df_edu: pd.DataFrame,
    df_emp: pd.DataFrame,
    drop_missing: bool = True,
) -> pd.DataFrame:
    """
    Merge education and employment on GEO_ID, add region,
    optionally drop rows with missing or invalid derived values.
    """
    # Keep only needed columns before merge
    edu_cols = ["GEO_ID", "NAME", "B15003_001E", "percent_bachelors_plus"]
    emp_cols = ["GEO_ID", "B23025_003E", "B23025_005E", "unemployment_rate"]
    df = df_edu[edu_cols].merge(
        df_emp[emp_cols],
        on="GEO_ID",
        how="inner",
    )
    df = add_region(df)
    if drop_missing:
        df = df.dropna(subset=["percent_bachelors_plus", "unemployment_rate", "region"])
        # Drop any nonsensical rates (e.g. > 100 or < 0 if any)
        df = df[
            (df["unemployment_rate"] >= 0) & (df["unemployment_rate"] <= 100)
            & (df["percent_bachelors_plus"] >= 0) & (df["percent_bachelors_plus"] <= 100)
        ]
    return df.reset_index(drop=True)
