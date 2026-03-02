"""
Configuration and paths for the Education and Employment statistical analysis project.
Paths are relative to the project root; run the notebook from the repository root.
"""

from pathlib import Path

# Project root (parent of src/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data paths
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS_FIGURES = PROJECT_ROOT / "outputs" / "figures"

# ACS table folders and files
B15003_DIR = DATA_RAW / "ACSDT5Y2024.B15003"
B23025_DIR = DATA_RAW / "ACSDT5Y2024.B23025"
B15003_DATA = B15003_DIR / "ACSDT5Y2024.B15003-Data.csv"
B23025_DATA = B23025_DIR / "ACSDT5Y2024.B23025-Data.csv"

# Processed output
MERGED_CSV = DATA_PROCESSED / "merged_education_employment.csv"

# Reproducibility
RANDOM_SEED = 42
