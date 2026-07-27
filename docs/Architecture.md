# 🏗️ Architecture

## Overview

This project demonstrates how a real-world Data Engineering team builds a modern Lakehouse solution using the **Medallion Architecture** on **Databricks**.

The project uses the **Olist E-Commerce Dataset** as the source system and transforms raw operational data into analytics-ready datasets through multiple layers.

The architecture follows industry best practices for:

- Data Ingestion
- Data Quality
- Data Transformation
- Data Governance
- Analytics
- Reporting

---

# High-Level Architecture

```text
                 Olist E-Commerce Dataset
                           │
                           ▼
                  Raw CSV Files (Source)
                           │
                           ▼
               Databricks Auto Loader / PySpark
                           │
                           ▼
                Bronze Layer (Raw Delta Tables)
                           │
                           ▼
          Silver Layer (Validated & Clean Delta Tables)
                           │
                           ▼
      Gold Layer (Business Ready Data Models)
                           │
                           ▼
         Power BI • Databricks SQL • Analytics
```

---

# Architecture Diagram

> **Architecture Overview**

<p align="center">
<img src="../images/architecture.png" width="100%">
</p>

---

# Components

## 1. Source System

The project starts with raw CSV files from the Olist E-Commerce Dataset.

Source files include:

- Customers
- Orders
- Order Items
- Products
- Sellers
- Payments
- Reviews
- Geolocation
- Product Categories

These files are stored exactly as received.

```
datasets/raw/
```

---

## 2. Ingestion Layer

The ingestion layer is responsible for loading raw CSV files into Databricks.

Technology:

- PySpark
- Databricks
- Delta Lake

Main responsibilities:

- Read CSV files
- Infer schema
- Validate records
- Handle bad records
- Write Delta tables

Output:

```
Bronze Layer
```

---

## 3. Bronze Layer

The Bronze layer stores raw data without business transformations.

Characteristics

- Append-only
- Schema preserved
- Immutable
- Historical data retained
- Delta format

Example tables

```
bronze.customers

bronze.orders

bronze.order_items

bronze.products

bronze.payments

bronze.sellers

bronze.reviews

bronze.geolocation
```

---

## 4. Silver Layer

The Silver layer contains cleaned and standardized data.

Typical transformations include:

- Null handling
- Duplicate removal
- Data type corrections
- Business rule validation
- Standardized columns
- Data enrichment

Example tables

```
silver.customers

silver.orders

silver.order_items

silver.products

silver.payments

silver.sellers

silver.geolocation
```

---

## 5. Gold Layer

The Gold layer contains analytics-ready datasets.

These tables are optimized for reporting and business intelligence.

Example tables

```
gold.sales_summary

gold.customer_analytics

gold.product_performance

gold.payment_analysis

gold.order_fulfillment

gold.inventory_snapshot
```

---

# Consumption Layer

Business users consume Gold tables using:

- Power BI
- Databricks SQL
- SQL Analytics
- Data Science
- Machine Learning
- Executive Dashboards

---

# Data Flow

```
CSV Files
      │
      ▼
PySpark
      │
      ▼
Bronze
      │
      ▼
Silver
      │
      ▼
Gold
      │
      ▼
Power BI / Databricks SQL
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Cloud Platform | Azure Databricks |
| Processing | Apache Spark (PySpark) |
| Storage | Delta Lake |
| Programming | Python |
| Data Format | CSV, Delta |
| Version Control | Git & GitHub |
| Notebook Platform | Databricks |
| Reporting | Power BI |
| SQL Analytics | Databricks SQL |

---

# Governance

The architecture supports enterprise governance through:

- Unity Catalog
- Access Control
- Audit Logging
- Data Lineage
- Data Quality Validation
- Delta Lake ACID Transactions

---

# Benefits

✅ Scalable Architecture

✅ Reliable Data Pipelines

✅ High Data Quality

✅ ACID Transactions

✅ Versioned Data

✅ Easy Maintenance

✅ Analytics Ready

✅ Industry Standard Design

---

# Repository Structure

```text
datasets/raw
        │
        ▼
Databricks Ingestion
        │
        ▼
Bronze
        │
        ▼
Silver
        │
        ▼
Gold
        │
        ▼
Business Dashboards
```

---

## Conclusion

This architecture closely follows the Medallion Architecture recommended for modern Lakehouse platforms. It demonstrates how raw operational data is progressively transformed into trusted, analytics-ready datasets while maintaining scalability, governance, and performance.
