"""
=========================================================
Project : 60 Days Real World Databricks Challenge
Module  : quality.py
Purpose : Data Quality Rule Engine
=========================================================
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col


# =========================================================
# Null Percentage
# =========================================================

def null_percentage(
    df: DataFrame,
    column_name: str
) -> float:
    """
    Returns null percentage for a column.
    """

    total_rows = df.count()

    if total_rows == 0:
        return 0.0

    null_rows = df.filter(
        col(column_name).isNull()
    ).count()

    return round((null_rows / total_rows) * 100, 2)


# =========================================================
# Duplicate Percentage
# =========================================================

def duplicate_percentage(
    df: DataFrame
) -> float:
    """
    Returns duplicate percentage.
    """

    total_rows = df.count()

    if total_rows == 0:
        return 0.0

    duplicate_rows = total_rows - df.dropDuplicates().count()

    return round((duplicate_rows / total_rows) * 100, 2)


# =========================================================
# Primary Key Check
# =========================================================

def primary_key_check(
    df: DataFrame,
    primary_key: str
) -> bool:
    """
    Checks whether primary key is unique.
    """

    return (
        df.select(primary_key).distinct().count()
        == df.count()
    )


# =========================================================
# Required Columns Check
# =========================================================

def required_columns_check(
    df: DataFrame,
    required_columns: list
) -> bool:
    """
    Checks all required columns exist.
    """

    return all(
        column in df.columns
        for column in required_columns
    )


# =========================================================
# Empty Data Check
# =========================================================

def empty_dataset_check(
    df: DataFrame
) -> bool:
    """
    Returns True if dataset contains records.
    """

    return df.count() > 0


# =========================================================
# Quality Report
# =========================================================

def quality_report(
    df: DataFrame,
    primary_key: str
) -> None:
    """
    Prints a simple data quality report.
    """

    print("=" * 60)
    print("DATA QUALITY REPORT")
    print("=" * 60)

    print(f"Rows                 : {df.count()}")
    print(f"Columns              : {len(df.columns)}")
    print(f"Primary Key Unique   : {primary_key_check(df, primary_key)}")
    print(f"Duplicate %          : {duplicate_percentage(df)}%")

    print("\nNull Percentage")

    for column in df.columns:
        print(
            f"{column:<35}"
            f"{null_percentage(df, column)}%"
        )

    print("=" * 60)
