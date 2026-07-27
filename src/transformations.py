"""
=========================================================
Project : 60 Days Real World Databricks Challenge
Module  : transformations.py
Purpose : Reusable PySpark Transformation Functions
=========================================================
"""

from typing import List

from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    current_timestamp,
    lit,
    trim,
    upper,
    lower
)


# =========================================================
# Select Columns
# =========================================================

def select_columns(
    df: DataFrame,
    columns: List[str]
) -> DataFrame:
    """
    Select required columns.
    """

    return df.select(*columns)


# =========================================================
# Rename Columns
# =========================================================

def rename_columns(
    df: DataFrame,
    column_mapping: dict
) -> DataFrame:
    """
    Rename multiple columns.
    """

    for old_name, new_name in column_mapping.items():
        df = df.withColumnRenamed(old_name, new_name)

    return df


# =========================================================
# Drop Columns
# =========================================================

def drop_columns(
    df: DataFrame,
    columns: List[str]
) -> DataFrame:
    """
    Drop unwanted columns.
    """

    return df.drop(*columns)


# =========================================================
# Remove Duplicate Records
# =========================================================

def remove_duplicates(
    df: DataFrame
) -> DataFrame:
    """
    Remove duplicate rows.
    """

    return df.dropDuplicates()


# =========================================================
# Trim String Columns
# =========================================================

def trim_columns(
    df: DataFrame,
    columns: List[str]
) -> DataFrame:
    """
    Remove leading/trailing spaces.
    """

    for column in columns:
        df = df.withColumn(column, trim(col(column)))

    return df


# =========================================================
# Convert to Upper Case
# =========================================================

def uppercase_columns(
    df: DataFrame,
    columns: List[str]
) -> DataFrame:
    """
    Convert column values to upper case.
    """

    for column in columns:
        df = df.withColumn(column, upper(col(column)))

    return df


# =========================================================
# Convert to Lower Case
# =========================================================

def lowercase_columns(
    df: DataFrame,
    columns: List[str]
) -> DataFrame:
    """
    Convert column values to lower case.
    """

    for column in columns:
        df = df.withColumn(column, lower(col(column)))

    return df


# =========================================================
# Add Ingestion Timestamp
# =========================================================

def add_ingestion_timestamp(
    df: DataFrame
) -> DataFrame:
    """
    Add ingestion timestamp.
    """

    return df.withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )


# =========================================================
# Add Source File
# =========================================================

def add_source_file(
    df: DataFrame,
    file_name: str
) -> DataFrame:
    """
    Add source file name.
    """

    return df.withColumn(
        "source_file",
        lit(file_name)
    )


# =========================================================
# Filter Records
# =========================================================

def filter_records(
    df: DataFrame,
    condition
) -> DataFrame:
    """
    Filter DataFrame using a condition.
    """

    return df.filter(condition)


# =========================================================
# Join DataFrames
# =========================================================

def join_dataframes(
    left_df: DataFrame,
    right_df: DataFrame,
    join_column: str,
    join_type: str = "inner"
) -> DataFrame:
    """
    Join two DataFrames.
    """

    return left_df.join(
        right_df,
        join_column,
        join_type
    )
