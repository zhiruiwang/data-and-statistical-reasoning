# Data and Statistical Reasoning: Education and Employment Across U.S. Counties

This repository contains a reproducible statistical analysis linking U.S. county-level **educational attainment** (ACS B15003) and **employment status** (ACS B23025). The project explores whether higher county-level bachelor's degree attainment is associated with lower unemployment rate using descriptive statistics, visualizations, and two hypothesis tests (Pearson correlation and one-way ANOVA by Census region). No machine learning models are trained.

## Tools and Libraries

- **Python**, **NumPy**, **Pandas**, **Matplotlib**, **Seaborn**, **SciPy**, **Jupyter**. Install with: `pip install -r requirements.txt`

## Data Sources

- **ACS B15003** — Educational Attainment for the Population 25 Years and Over (ACS 5-Year 2024).  
  Folder: `data/raw/ACSDT5Y2024.B15003/`  
  File: `ACSDT5Y2024.B15003-Data.csv`

- **ACS B23025** — Employment Status for the Population 16 Years and Over (ACS 5-Year 2024).  
  Folder: `data/raw/ACSDT5Y2024.B23025/`  
  File: `ACSDT5Y2024.B23025-Data.csv`

Source: [data.census.gov](https://data.census.gov) (ACS 5-Year Estimates, county geography).

## How to Run

1. **From project root**, create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter notebook:**
   ```bash
   jupyter notebook analysis.ipynb
   ```
   Run all cells from top to bottom (Cell → Run All).

4. **Outputs:**
   - Processed data: `data/processed/merged_education_employment.csv`
   - Figures: `outputs/figures/` (histograms, scatter, boxplot)

## Deliverables

- **analysis.ipynb** — Loads data, computes descriptive statistics (summary stats, categorical counts, distribution exploration), creates at least three visualizations (with titles and axis labels), performs two hypothesis tests (Pearson correlation and one-way ANOVA), and includes a short summary.
- **Statistical_Analysis_Report.pdf** — Statistical Analysis Report.
- **Dataset** — Original ACS data in `data/raw/ACSDT5Y2024.B15003/` and `data/raw/ACSDT5Y2024.B23025/` (CSV files as stated in Data Sources).
- **requirements.txt** — Included; generated with `pip freeze > requirements.txt` from the project environment.

## Reproducibility

- Paths are relative to the project root; run the notebook from the repository root.
- A fixed random seed is set where applicable (`config.RANDOM_SEED`).
- Census CSVs use two header rows; the code skips the second row. Suppressed values (`-`, `*****`) are coerced to NaN and excluded from analysis.

## Limitations and Bias

- **Selection bias:** Dropping counties with missing or suppressed values may underrepresent small or disadvantaged counties.
- **Ecological fallacy:** Associations at the county level do not imply the same relationship at the individual level.
- **Data quality:** ACS estimates have margins of error; interpretations should account for uncertainty.

## Repository Structure

```
Data-and-Statistical-Reasoning/
├── data/
│   ├── raw/                          # ACS B15003, B23025 folders
│   └── processed/                    # merged_education_employment.csv
├── outputs/
│   └── figures/                      # saved plots
├── src/
│   ├── config.py
│   ├── io.py
│   ├── cleaning.py
│   ├── eda.py
│   └── viz.py
├── analysis.ipynb                    # main analysis notebook
├── requirements.txt
├── README.md
└── .gitignore
```
