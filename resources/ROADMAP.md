# 🗺️ ROADMAP.md

# 🚀 60 Days Real World Databricks Challenge

> **Project:** Retail Lakehouse Modernization  
> **Company:** Olist Technologies  
> **Role:** Junior Data Engineer  
> **Methodology:** Agile Scrum  
> **Platform:** Databricks Community Edition  
> **Primary Language:** PySpark  
> **Dataset:** Brazilian Olist E-Commerce Dataset

---

# 🎯 Challenge Goal

By the end of this challenge you will build a **production-style Retail Lakehouse** completely from scratch using Databricks Community Edition.

The project will simulate working as a **Junior Data Engineer** in a real Agile Scrum team.

You will finish with:

- ✅ Professional GitHub Portfolio
- ✅ Production-quality PySpark Code
- ✅ Delta Lake
- ✅ Spark SQL
- ✅ Bronze Layer
- ✅ Silver Layer
- ✅ Gold Layer
- ✅ Modular Project Structure
- ✅ Logging Framework
- ✅ Validation Framework
- ✅ Data Quality Framework
- ✅ Enterprise Documentation
- ✅ Interview Preparation

---

# 🏢 Company Background

Olist Technologies is an e-commerce platform that receives millions of records every day.

The Data Engineering Team has been assigned to build a modern Retail Lakehouse capable of handling analytical reporting and future machine learning workloads.

You have recently joined the company as a **Junior Data Engineer**.

Every day your Tech Lead assigns one Jira Story.

Your responsibility is to complete each story and push the changes to GitHub.

---

# 📦 Dataset

The project uses ONLY the Brazilian Olist E-Commerce Dataset.

## Files

| Dataset | Purpose |
|----------|----------|
| olist_customers_dataset.csv | Customer Information |
| olist_orders_dataset.csv | Orders |
| olist_order_items_dataset.csv | Order Items |
| olist_order_payments_dataset.csv | Payments |
| olist_order_reviews_dataset.csv | Reviews |
| olist_products_dataset.csv | Products |
| olist_sellers_dataset.csv | Sellers |
| olist_geolocation_dataset.csv | Geolocation |
| product_category_name_translation.csv | Category Translation |

---

# 🏗️ Project Structure

```text
60-Days-Real-World-Databricks-Challenge/

│
├── datasets/
│
├── docs/
│
├── images/
│
├── notebooks/
│
├── src/
│   ├── config.py
│   ├── constants.py
│   ├── ingestion.py
│   ├── logger.py
│   ├── quality.py
│   ├── transformations.py
│   ├── utils.py
│   └── validation.py
│
├── ROADMAP.md
│
├── README.md
│
└── requirements.txt
```

---

# 🏁 Sprint Plan

| Sprint | Days | Goal |
|---------|------|------|
| Sprint 01 | Day 01–07 | Foundation Setup |
| Sprint 02 | Day 08–14 | Bronze Layer |
| Sprint 03 | Day 15–21 | Silver Layer |
| Sprint 04 | Day 22–28 | Gold Layer |
| Sprint 05 | Day 29–35 | Performance Optimization |
| Sprint 06 | Day 36–42 | Spark SQL Analytics |
| Sprint 07 | Day 43–49 | Data Quality & Testing |
| Sprint 08 | Day 50–56 | Production Pipeline |
| Sprint 09 | Day 57–60 | Documentation & Interview Preparation |

---

# 🚀 Sprint 01

## Foundation Setup

### Goal

Prepare the Databricks development environment and understand the business dataset.

| Day | Story ID | Topic |
|------|----------|------------------------------|
| 01 | DE-101 | Databricks Community Environment Setup |
| 02 | DE-102 | Workspace Navigation & Repository Structure |
| 03 | DE-103 | Upload & Explore Olist Dataset |
| 04 | DE-104 | Business Understanding & Data Profiling |
| 05 | DE-105 | Reusable PySpark Framework |
| 06 | DE-106 | Logging & Validation Framework |
| 07 | DE-107 | Sprint Review, Demo & Retrospective |

---

# 🥉 Sprint 02

## Bronze Layer

### Goal

Build the Raw ➜ Bronze ingestion layer.

| Day | Story ID | Topic |
|------|----------|----------------------------|
| 08 | DE-201 | Bronze Layer Architecture |
| 09 | DE-202 | Customers Bronze Pipeline |
| 10 | DE-203 | Orders Bronze Pipeline |
| 11 | DE-204 | Products & Sellers Pipeline |
| 12 | DE-205 | Payments & Reviews Pipeline |
| 13 | DE-206 | Bronze Validation |
| 14 | DE-207 | Sprint Review |

---

# 🥈 Sprint 03

## Silver Layer

### Goal

Clean and standardize the data.

| Day | Story ID | Topic |
|------|----------|-----------------------------|
| 15 | DE-301 | Silver Layer Design |
| 16 | DE-302 | Customer Cleaning |
| 17 | DE-303 | Orders Cleaning |
| 18 | DE-304 | Products Standardization |
| 19 | DE-305 | Business Rules |
| 20 | DE-306 | Silver Validation |
| 21 | DE-307 | Sprint Review |

---

# 🥇 Sprint 04

## Gold Layer

### Goal

Create business-ready analytics tables.

| Day | Story ID | Topic |
|------|----------|---------------------------|
| 22 | DE-401 | Gold Layer Design |
| 23 | DE-402 | Customer Dimension |
| 24 | DE-403 | Product Dimension |
| 25 | DE-404 | Seller Dimension |
| 26 | DE-405 | Date Dimension |
| 27 | DE-406 | Sales Fact Table |
| 28 | DE-407 | Sprint Review |

---

# ⚡ Sprint 05

## Spark Performance Optimization

### Goal

Improve Spark job performance.

| Day | Story ID | Topic |
|------|----------|--------------------------|
| 29 | DE-501 | Spark Execution Plan |
| 30 | DE-502 | Cache & Persist |
| 31 | DE-503 | Partitioning |
| 32 | DE-504 | Repartition vs Coalesce |
| 33 | DE-505 | Broadcast Join |
| 34 | DE-506 | Performance Tuning |
| 35 | DE-507 | Sprint Review |

---

# 📊 Sprint 06

## Spark SQL Analytics

### Goal

Build business analytics using Spark SQL.

| Day | Story ID | Topic |
|------|----------|---------------------------|
| 36 | DE-601 | Spark SQL Fundamentals |
| 37 | DE-602 | Aggregations |
| 38 | DE-603 | Window Functions |
| 39 | DE-604 | Ranking Functions |
| 40 | DE-605 | Business KPIs |
| 41 | DE-606 | Executive Dashboard Queries |
| 42 | DE-607 | Sprint Review |

---

# 🔍 Sprint 07

## Data Quality

### Goal

Validate and monitor data quality.

| Day | Story ID | Topic |
|------|----------|-------------------------|
| 43 | DE-701 | Data Quality Framework |
| 44 | DE-702 | Null Validation |
| 45 | DE-703 | Duplicate Validation |
| 46 | DE-704 | Schema Validation |
| 47 | DE-705 | Exception Handling |
| 48 | DE-706 | Audit Tables |
| 49 | DE-707 | Sprint Review |

---

# ⚙️ Sprint 08

## Production Pipeline

### Goal

Build a reusable production-ready ETL pipeline.

| Day | Story ID | Topic |
|------|----------|-------------------------|
| 50 | DE-801 | End-to-End Pipeline |
| 51 | DE-802 | Modular ETL |
| 52 | DE-803 | Configuration Management |
| 53 | DE-804 | Production Logging |
| 54 | DE-805 | Error Recovery |
| 55 | DE-806 | Production Readiness |
| 56 | DE-807 | Sprint Review |

---

# 🎯 Sprint 09

## Project Completion

### Goal

Complete the project and prepare for interviews.

| Day | Story ID | Topic |
|------|----------|-----------------------------|
| 57 | DE-901 | Architecture Documentation |
| 58 | DE-902 | README & GitHub Documentation |
| 59 | DE-903 | Data Engineer Interview Preparation |
| 60 | DE-904 | Final Demo & Portfolio Review |

---

# 📈 Learning Progress

```text
Sprint 01  ███████░░░░░░░░░░░░░
Sprint 02  ███████░░░░░░░░░░░░░
Sprint 03  ███████░░░░░░░░░░░░░
Sprint 04  ███████░░░░░░░░░░░░░
Sprint 05  ███████░░░░░░░░░░░░░
Sprint 06  ███████░░░░░░░░░░░░░
Sprint 07  ███████░░░░░░░░░░░░░
Sprint 08  ███████░░░░░░░░░░░░░
Sprint 09  ████░░░░░░░░░░░░░░░░
```

---

# 🎯 Final Deliverables

By Day 60 your GitHub repository will include:

- ✅ End-to-End Retail Lakehouse
- ✅ Bronze, Silver & Gold Layers
- ✅ Reusable PySpark Framework
- ✅ Spark SQL Analytics
- ✅ Delta Lake Implementation
- ✅ Data Validation Framework
- ✅ Data Quality Framework
- ✅ Logging Framework
- ✅ Production ETL Pipelines
- ✅ Architecture Diagram
- ✅ ER Diagram
- ✅ Professional README
- ✅ Enterprise Documentation
- ✅ Complete Git History
- ✅ Interview-Ready Portfolio

---

# 💬 Tech Lead Note

> "Focus on understanding each Jira Story instead of rushing to complete the challenge. Every Sprint builds on the previous one, just like in a real Data Engineering project. By consistently completing one story at a time, you'll finish with a portfolio that demonstrates both technical skills and professional software development practices."
