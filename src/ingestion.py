"""
=========================================================
Project : 60 Days Real World Databricks Challenge
Module  : ingestion.py
Purpose : Data Ingestion Functions
=========================================================
"""

from pyspark.sql import DataFrame, SparkSession


# =========================================================
# Read CSV
# =========================================================

def read_csv(
    spark: SparkSession,
    file_path: str,
    header: bool = True,
    infer_schema: bool = True
) -> DataFrame:
    """
    Reads a CSV file.
    """

    return (
        spark.read
        .format("csv")
        .option("header", header)
        .option("inferSchema", infer_schema)
        .load(file_path)
    )


# =========================================================
# Read Parquet
# =========================================================

def read_parquet(
    spark: SparkSession,
    file_path: str
) -> DataFrame:
    """
    Reads a Parquet file.
    """

    return (
        spark.read
        .format("parquet")
        .load(file_path)
    )


# =========================================================
# Read Delta
# =========================================================

def read_delta(
    spark: SparkSession,
    file_path: str
) -> DataFrame:
    """
    Reads Delta data.
    """

    return (
        spark.read
        .format("delta")
        .load(file_path)
    )


# =========================================================
# Read JSON
# =========================================================

def read_json(
    spark: SparkSession,
    file_path: str,
    multiline: bool = False
) -> DataFrame:
    """
    Reads a JSON file.
    """

    return (
        spark.read
        .format("json")
        .option("multiline", multiline)
        .load(file_path)
    )


# =========================================================
# Read Table
# =========================================================

def read_table(
    spark: SparkSession,
    table_name: str
) -> DataFrame:
    """
    Reads a Unity Catalog or Hive table.
    """

    return spark.table(table_name)


# =========================================================
# Read Multiple CSV Files
# =========================================================

def read_csv_files(
    spark: SparkSession,
    folder_path: str
) -> DataFrame:
    """
    Reads all CSV files from a folder.
    """

    return (
        spark.read
        .format("csv")
        .option("header", True)
        .option("inferSchema", True)
        .load(folder_path)
    )
