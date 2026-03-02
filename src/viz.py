"""
Visualizations for education and employment analysis.
Each figure has a clear title and labeled axes.
"""

from typing import Optional
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def _save_fig(fig: plt.Figure, name: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_dir / name, bbox_inches="tight", dpi=150)
    # Do not close so Jupyter can display the figure in the notebook


def histograms(
    df,
    cols=None,
    output_dir: Optional[Path] = None,
    figsize=(10, 4),
):
    """Histograms for percent_bachelors_plus and unemployment_rate."""
    if cols is None:
        cols = ["percent_bachelors_plus", "unemployment_rate"]
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    for ax, col in zip(axes, cols):
        ax.hist(df[col].dropna(), bins=40, edgecolor="black", alpha=0.7)
        ax.set_title(f"Distribution of {col.replace('_', ' ').title()}")
        ax.set_xlabel(col.replace("_", " ").title())
        ax.set_ylabel("Count")
    plt.tight_layout()
    if output_dir:
        _save_fig(fig, "histograms.png", output_dir)
    else:
        plt.show()
    return fig


def scatter_education_unemployment(
    df,
    x="percent_bachelors_plus",
    y="unemployment_rate",
    output_dir: Optional[Path] = None,
    figsize=(8, 6),
):
    """Scatter plot: percent bachelor's+ vs unemployment rate."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(df[x], df[y], alpha=0.4, s=15)
    ax.set_title("County-Level: Education Attainment vs. Unemployment Rate")
    ax.set_xlabel("Percent with Bachelor's Degree or Higher")
    ax.set_ylabel("Unemployment Rate (%)")
    if output_dir:
        _save_fig(fig, "scatter_education_unemployment.png", output_dir)
    else:
        plt.show()
    return fig


def boxplot_unemployment_by_region(
    df,
    output_dir: Optional[Path] = None,
    figsize=(8, 5),
):
    """Boxplot of unemployment rate by Census region."""
    fig, ax = plt.subplots(figsize=figsize)
    order = ["Northeast", "Midwest", "South", "West"]
    plot_df = df[df["region"].isin(order)]
    sns.boxplot(data=plot_df, x="region", y="unemployment_rate", order=order, ax=ax)
    ax.set_title("Unemployment Rate by U.S. Census Region")
    ax.set_xlabel("Census Region")
    ax.set_ylabel("Unemployment Rate (%)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    if output_dir:
        _save_fig(fig, "boxplot_unemployment_by_region.png", output_dir)
    else:
        plt.show()
    return fig


def boxplot_education_by_region(
    df,
    output_dir: Optional[Path] = None,
    figsize=(8, 5),
):
    """Boxplot of percent bachelor's+ by Census region."""
    fig, ax = plt.subplots(figsize=figsize)
    order = ["Northeast", "Midwest", "South", "West"]
    plot_df = df[df["region"].isin(order)]
    sns.boxplot(data=plot_df, x="region", y="percent_bachelors_plus", order=order, ax=ax)
    ax.set_title("Percent Bachelor's Degree or Higher by U.S. Census Region")
    ax.set_xlabel("Census Region")
    ax.set_ylabel("Percent with Bachelor's Degree or Higher")
    plt.xticks(rotation=15)
    plt.tight_layout()
    if output_dir:
        _save_fig(fig, "boxplot_education_by_region.png", output_dir)
    else:
        plt.show()
    return fig
