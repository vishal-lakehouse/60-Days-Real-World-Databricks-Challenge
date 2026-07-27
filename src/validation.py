"""
=========================================================
Project : 60 Days Real World Databricks Challenge
Module  : validation.py
Purpose : Data Quality Validation Functions
=========================================================
"""

from pyspark.sql.functions import col


# =========================================================
# Row Count
# =========================================================

def row_count(df):
    """
    Returns total number of rows.
    """
    return df.count()


# =========================================================
# Column Count
# =========================================================

def column_count(df):
    """
    Returns total number of columns.
    """
    return len(df.columns)


# =========================================================
# Check Null Values
# =========================================================

def check_nulls(df):
    """
    Returns null count for every column.
    """
    return {
        column: df.filter(col(column).isNull()).count()
        for column in df.columns
    }


# =========================================================
# Check Duplicate Records
# =========================================================

def duplicate_count(df):
    """
    Returns duplicate row count.
    """
    return df.count() - df.dropDuplicates().count()


# =========================================================
# Validate Required Columns
# =========================================================

def validate_columns(df, required_columns):
    """
    Checks whether all required columns exist.
    """
    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    return missing_columns


# =========================================================
# Check Empty DataFrame
# =========================================================

def is_empty(df):
    """
    Returns True if DataFrame is empty.
    """
    return df.rdd.isEmpty()


# =========================================================
# Print Validation Summary
# =========================================================

def validation_summary(df):
    """
    Prints basic validation report.
    """

    print("=" * 60)
    print("DATA VALIDATION REPORT")
    print("=" * 60)

    print(f"Rows       : {row_count(df)}")
    print(f"Columns    : {column_count(df)}")
    print(f"Duplicates : {duplicate_count(df)}")

    print("\nNull Values")

    for column, count in check_nulls(df).items():
        print(f"{column:<35} {count}")

    print("=" * 60)
