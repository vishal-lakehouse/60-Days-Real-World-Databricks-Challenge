"""
=========================================================
Project : 60 Days Real World Databricks Challenge
Module  : utils.py
Purpose : Common utility functions
=========================================================
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp


# =========================================================
# Read CSV File
# =========================================================

def read_csv(spark: SparkSession,
             file_path: str,
             header: bool = True,
             infer_schema: bool = True):
    """
    Reads a CSV file and returns a Spark DataFrame.
    """

    return (
        spark.read
             .option("header", header)
             .option("inferSchema", infer_schema)
             .csv(file_path)
    )


# =========================================================
# Save DataFrame as Delta
# =========================================================

def write_delta(df,
                table_name: str,
                mode: str = "overwrite"):
    """
    Writes a DataFrame as a Delta table.
    """

    (
        df.write
          .format("delta")
          .mode(mode)
          .saveAsTable(table_name)
    )


# =========================================================
# Display DataFrame Information
# =========================================================

def dataframe_info(df):
    """
    Displays DataFrame summary.
    """

    print("=" * 50)
    print(f"Rows    : {df.count()}")
    print(f"Columns : {len(df.columns)}")
    print("=" * 50)

    df.printSchema()


# =========================================================
# Display Top Records
# =========================================================

def preview(df, rows: int = 5):
    """
    Displays the first N records.
    """

    df.show(rows, truncate=False)


# =========================================================
# Add Audit Timestamp
# =========================================================

def add_ingestion_timestamp(df):
    """
    Adds ingestion timestamp column.
    """

    return df.withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )


# =========================================================
# Count Null Values
# =========================================================

def count_nulls(df):
    """
    Counts null values in every column.
    """

    return {
        column: df.filter(df[column].isNull()).count()
        for column in df.columns
    }


# =========================================================
# Print Section Header
# =========================================================

def print_header(title: str):
    """
    Prints a formatted notebook section header.
    """

    print("\n" + "=" * 70)
    print(title.upper())
    print("=" * 70)
