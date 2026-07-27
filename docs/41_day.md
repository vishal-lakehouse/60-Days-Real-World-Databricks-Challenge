# Day 41 — Sprint 6

# 🚀 JIRA ID: OLIST-601

## Epic

**Enterprise Data Platform Engineering**

---

# 📖 User Story

**As a Lead Data Engineer,**

I want to build reusable and configuration-driven ETL pipelines,

so that new data sources can be onboarded quickly without modifying existing code.

---

# 🎯 Objective

Today you will build a **Metadata-Driven ETL Framework** for your Databricks Lakehouse.

By the end of today's assignment, you will learn how to:

- Build Configuration-Driven Pipelines
- Create Metadata Tables
- Parameterize Databricks Notebooks
- Execute Dynamic ETL Jobs
- Build Reusable Utility Functions
- Eliminate Hardcoded Logic
- Design Enterprise ETL Frameworks

---

# 🏢 Business Scenario

The Olist Lakehouse currently processes only one business domain.

However, the company plans to onboard several new domains:

- Finance
- Marketing
- Logistics
- Customer Support
- Inventory

Creating separate ETL notebooks for every new source would increase maintenance effort and duplicate code.

The Data Engineering team wants a **Metadata-Driven ETL Framework** where pipelines are controlled through configuration instead of hardcoded values.

Your responsibility is to build a reusable framework capable of processing multiple datasets using the same ETL logic.

---

# 📂 Source Assets

```
datasets/raw/

Bronze Tables

Silver Tables

Gold Tables
```

---

# 🏗 Target Tables

```
config.pipeline_metadata

config.source_metadata

config.column_mapping

audit.pipeline_execution_log
```

---

# 🛠 Technologies

- Azure Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Databricks Workflows
- Widgets
- Notebook Parameters

---

# 📋 Acceptance Criteria

✅ Metadata tables created

✅ Notebook parameterization implemented

✅ Dynamic ETL logic developed

✅ Utility functions created

✅ Configuration-driven execution verified

✅ Framework documentation completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-601_Metadata_Driven_ETL_Framework
```

---

## Task 2

Create a configuration schema.

```
config
```

Create the following tables.

```
pipeline_metadata

source_metadata

column_mapping
```

---

## Task 3

Populate the metadata tables.

Examples:

```
Source Name

File Path

Target Table

Load Type

Delimiter

Header

Schema Name

Primary Key

Watermark Column

Active Flag
```

Document every metadata field.

---

## Task 4

Parameterize your notebook.

Use Databricks Widgets.

Create parameters such as:

```
source_name

load_type

environment

target_table

run_date
```

Ensure the notebook runs successfully using different parameter values.

---

## Task 5

Build Dynamic File Reading.

Instead of hardcoding:

```
datasets/raw/orders.csv
```

Read the file path dynamically from:

```
config.source_metadata
```

---

## Task 6

Build Dynamic Target Loading.

Determine the destination table using metadata.

Example:

```
bronze.orders

silver.orders

gold.sales_summary
```

The notebook should load data without changing the code.

---

## Task 7

Create Reusable Utility Functions.

Examples:

```
read_source()

validate_schema()

log_pipeline()

write_delta()

archive_file()
```

Store all reusable logic in a utility notebook or module.

---

## Task 8

Execute Multiple Pipelines Dynamically.

Using the metadata table, process multiple datasets in a loop.

Example:

```
customers

orders

products

payments

reviews
```

Verify that all datasets are processed using the same notebook.

---

## Task 9

Log Pipeline Execution.

Capture:

```
Pipeline Name

Run ID

Execution Time

Status

Source Table

Target Table

Records Read

Records Written

```

Write logs into:

```
audit.pipeline_execution_log
```

---

## Task 10

Validate Framework.

Verify:

- Metadata values are read correctly.
- Dynamic paths work correctly.
- Multiple datasets execute successfully.
- Utility functions are reusable.
- No hardcoded paths remain.

---

## Task 11

Create an ETL Execution Flow Diagram.

Include:

```
Metadata Tables

↓

Notebook Parameters

↓

Dynamic Processing

↓

Reusable Functions

↓

Delta Tables

↓

Audit Logs
```

---

## Task 12 ⭐

Create Framework Documentation.

Include:

- Metadata Design
- Configuration Tables
- Parameter List
- Utility Functions
- Execution Flow
- Error Handling
- Logging Strategy
- Best Practices
- Future Enhancements

---

# 📚 Concepts Covered

- Metadata-Driven ETL
- Configuration Tables
- Notebook Parameters
- Databricks Widgets
- Dynamic ETL
- Reusable Code
- Utility Libraries
- Enterprise Framework Design

---

# 💡 Mini Challenge

Complete the following tasks.

1. Create a metadata table.

2. Read source file paths dynamically.

3. Parameterize a notebook using Widgets.

4. Build a reusable file reader.

5. Build a reusable Delta writer.

6. Execute multiple datasets using one notebook.

7. Create reusable logging functions.

8. Validate metadata consistency.

9. Remove all hardcoded values.

10. Draw the metadata-driven ETL architecture.

---

# 🧠 Real Interview Questions

### Q1

What is a Metadata-Driven ETL Framework?

---

### Q2

Why should ETL pipelines avoid hardcoded values?

---

### Q3

How do Databricks Widgets support parameterized notebooks?

---

### Q4

What are the advantages of reusable utility functions?

---

### Q5

How would you onboard a new source system without changing pipeline code?

---

### Q6

What information should be stored in a metadata table?

---

### Q7

How do configuration-driven pipelines improve scalability?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Metadata Configuration Tables Created

✓ Parameterized Notebook Developed

✓ Dynamic ETL Framework Built

✓ Reusable Utility Functions Created

✓ Multiple Datasets Processed Dynamically

✓ Pipeline Execution Logging Implemented

✓ ETL Flow Diagram Created

✓ Framework Documentation Completed
```

---

# 🏁 End Goal

At the end of Day 41, your Lakehouse will support reusable, configuration-driven ETL pipelines.

```
Metadata Tables
        │
        ▼
Notebook Parameters
        │
        ▼
Dynamic File Reader
        │
        ▼
Reusable ETL Functions
        │
        ▼
Bronze / Silver / Gold
        │
        ▼
Audit Logs
        │
        ▼
Enterprise ETL Framework
```

Instead of creating separate notebooks for every dataset, your platform can now process multiple data sources using metadata, reusable components, and dynamic configuration—an approach widely adopted in enterprise Data Engineering platforms.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| Sprint 3 | OLIST-301 → OLIST-310 | Gold Analytics Layer | ✅ Complete |
| Sprint 4 | OLIST-401 → OLIST-402 | Reporting Data Mart & Power BI | ✅ Complete |
| Sprint 5 | OLIST-501 → OLIST-510 | Production Lakehouse & Enterprise Features | ✅ Complete |
| **Sprint 6** | **OLIST-601** | **Build Metadata-Driven ETL Framework** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 42)

## 🚀 JIRA ID: OLIST-602

**Implement Automated Data Reconciliation & End-to-End Validation** by building a reconciliation framework that compares source, Bronze, Silver, and Gold datasets using row counts, checksums, aggregates, business totals, and data completeness checks. You'll learn how enterprise Data Engineering teams guarantee data accuracy before publishing datasets to downstream consumers.
