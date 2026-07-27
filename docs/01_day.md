# Day 01 — Sprint 1

# 🚀 JIRA ID: OLIST-101

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Customer** dataset from the source system into the Bronze layer,

so that downstream transformations can use a trusted raw Delta table.

---

# 🎯 Objective

Today you will build your **first Databricks ETL pipeline**.

At the end of today's task, you will know how to:

- Upload files into Databricks
- Read CSV files using PySpark
- Understand Spark DataFrames
- Inspect schemas
- Validate records
- Save data as Delta Lake
- Query Delta tables using SQL

This is exactly what a Junior Data Engineer would do on their first project.

---

# 🏢 Business Scenario

The Olist e-commerce platform receives customer information from operational systems every day.

Your responsibility is to ingest this raw customer data into the Bronze layer without modifying it.

No cleaning.

No transformations.

No business logic.

Only ingestion.

---

# 📂 Source Dataset

```
datasets/raw/olist_customers_dataset.csv
```

---

# 🏗 Target Layer

```
bronze.customers
```

---

# 🛠 Technologies

- Azure Databricks
- Apache Spark
- PySpark
- Delta Lake

---

# 📋 Acceptance Criteria

✅ CSV uploaded successfully

✅ File read using PySpark

✅ Schema verified

✅ Record count validated

✅ No data transformation

✅ Bronze Delta table created

✅ SQL query executed successfully

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-101_Load_Customers_Bronze
```

---

## Task 2

Upload

```
olist_customers_dataset.csv
```

into Databricks.

---

## Task 3

Read the CSV using PySpark.

---

## Task 4

Display the first 10 records.

---

## Task 5

Print the schema.

---

## Task 6

Count total records.

---

## Task 7

Create a Bronze Delta table named

```
bronze.customers
```

---

## Task 8

Run SQL queries to validate the table.

Example validations:

- Total Records
- Distinct Customers
- Null Customer IDs

---

# 📚 Concepts Covered

- DataFrame
- Schema Inference
- CSV Reader
- Delta Lake
- Managed Table
- Spark SQL

---

# 🧠 Real Interview Questions

### Q1

Why do we create a Bronze layer?

---

### Q2

Why should we avoid cleaning data in Bronze?

---

### Q3

Difference between CSV and Delta?

---

### Q4

What is a Spark DataFrame?

---

### Q5

Why validate record counts after ingestion?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Notebook Created

✓ Customer CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ Bronze Delta Table Created

✓ SQL Validation Completed
```

---

# 🏁 End Goal

At the end of Day 1, you will have created your **first production-style Bronze ingestion pipeline** using Databricks, PySpark, and Delta Lake.

This is the foundation on which every modern Lakehouse project is built.

---

# 🔜 Tomorrow (Day 02)

**JIRA ID: OLIST-102**

Load **Orders Dataset** into the Bronze layer and establish the first relationship between Customers and Orders.
