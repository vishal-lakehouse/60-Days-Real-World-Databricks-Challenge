"""
=========================================================
Project : 60 Days Real World Databricks Challenge
Module  : constants.py
Purpose : Project-wide constant values
=========================================================
"""

# =========================================================
# Environment
# =========================================================

DEV = "Development"
TEST = "Testing"
PROD = "Production"

# =========================================================
# Medallion Layers
# =========================================================

BRONZE = "bronze"
SILVER = "silver"
GOLD = "gold"

# =========================================================
# File Formats
# =========================================================

CSV = "csv"
PARQUET = "parquet"
DELTA = "delta"
JSON = "json"

# =========================================================
# Write Modes
# =========================================================

OVERWRITE = "overwrite"
APPEND = "append"
IGNORE = "ignore"
ERROR_IF_EXISTS = "error"

# =========================================================
# Boolean Values
# =========================================================

TRUE = True
FALSE = False

# =========================================================
# Date Formats
# =========================================================

DATE_FORMAT = "yyyy-MM-dd"
TIMESTAMP_FORMAT = "yyyy-MM-dd HH:mm:ss"

# =========================================================
# Validation Status
# =========================================================

SUCCESS = "SUCCESS"
FAILED = "FAILED"
WARNING = "WARNING"

# =========================================================
# Common Column Names
# =========================================================

INGESTION_TIMESTAMP = "ingestion_timestamp"
LOAD_DATE = "load_date"
CREATED_DATE = "created_date"
UPDATED_DATE = "updated_date"

# =========================================================
# Spark Configurations
# =========================================================

DEFAULT_PARTITIONS = 8

# =========================================================
# Null Replacement
# =========================================================

UNKNOWN = "UNKNOWN"
NOT_AVAILABLE = "N/A"
