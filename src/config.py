"""
=========================================================
Project : 60 Days Real World Databricks Challenge
Module  : config.py
Purpose : Centralized project configuration
=========================================================
"""

# =========================================================
# Project Information
# =========================================================

PROJECT_NAME = "Olist Retail Analytics"
ENVIRONMENT = "Development"

# =========================================================
# Unity Catalog
# =========================================================

CATALOG_NAME = "olist_catalog"

# =========================================================
# Schemas
# =========================================================

BRONZE_SCHEMA = "bronze"
SILVER_SCHEMA = "silver"
GOLD_SCHEMA = "gold"

# =========================================================
# Volume
# =========================================================

RAW_VOLUME = "raw_files"

# =========================================================
# Dataset Location
# =========================================================

RAW_DATA_PATH = (
    "/Volumes/olist_catalog/bronze/raw_files/"
)

# =========================================================
# Dataset Names
# =========================================================

CUSTOMERS_FILE = "olist_customers_dataset.csv"

ORDERS_FILE = "olist_orders_dataset.csv"

ORDER_ITEMS_FILE = "olist_order_items_dataset.csv"

ORDER_PAYMENTS_FILE = "olist_order_payments_dataset.csv"

ORDER_REVIEWS_FILE = "olist_order_reviews_dataset.csv"

PRODUCTS_FILE = "olist_products_dataset.csv"

SELLERS_FILE = "olist_sellers_dataset.csv"

GEOLOCATION_FILE = "olist_geolocation_dataset.csv"

CATEGORY_TRANSLATION_FILE = (
    "product_category_name_translation.csv"
)

# =========================================================
# Delta Table Names
# =========================================================

CUSTOMERS_TABLE = "customers"

ORDERS_TABLE = "orders"

ORDER_ITEMS_TABLE = "order_items"

ORDER_PAYMENTS_TABLE = "order_payments"

ORDER_REVIEWS_TABLE = "order_reviews"

PRODUCTS_TABLE = "products"

SELLERS_TABLE = "sellers"

GEOLOCATION_TABLE = "geolocation"

CATEGORY_TABLE = "product_category_translation"
