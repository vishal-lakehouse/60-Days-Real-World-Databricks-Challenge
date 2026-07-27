# Day 10 — Sprint 2

# 🚀 JIRA ID: OLIST-201

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Customers** dataset from the Bronze layer into the Silver layer,

so that downstream applications can consume clean, validated, and standardized customer data.

---

# 🎯 Objective

Today marks the beginning of the **Silver Layer**.

Unlike the Bronze layer, today's goal is **not just loading data**.

You will perform your **first real ETL transformation** by applying data quality checks while preserving business information.

By the end of today's assignment, you will learn how to:

- Read Delta tables
- Apply data quality checks
- Remove duplicate records
- Handle NULL values
- Standardize text columns
- Create Silver Delta tables
- Compare Bronze vs Silver data

---

# 🏢 Business Scenario

The Bronze layer stores raw customer data exactly as received.

Before this data can be used for reporting and analytics, it must be validated and standardized.

Your responsibility is to create a trusted **Silver Customers** table that serves as the single source of truth for customer information.

---

# 📂 Source Table

```
bronze.customers
```

---

# 🏗 Target Table

```
silver.customers
```

---

# 🛠 Technologies

- Azure Databricks
- Apache Spark
- PySpark
- Delta Lake
- Spark SQL

---

# 📋 Acceptance Criteria

✅ Bronze table read successfully

✅ Duplicate customers removed

✅ Invalid records identified

✅ Customer city standardized

✅ Customer state standardized

✅ NULL values analysed

✅ Silver Delta table created

✅ Bronze vs Silver comparison completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-201_Transform_Customers_Silver
```

---

## Task 2

Read

```
bronze.customers
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Compare it with the Bronze table.

---

## Task 4

Count total records.

---

## Task 5

Check duplicate records using

```
customer_id
```

Remove duplicates if found.

---

## Task 6

Analyse NULL values.

Check every column.

Document your findings.

---

## Task 7

Standardize customer information.

Examples:

- Trim leading and trailing spaces
- Convert city names to Proper Case
- Convert state codes to uppercase

Do **not** change the business meaning of the data.

---

## Task 8

Validate ZIP code prefixes.

Questions:

- Are ZIP code prefixes NULL?
- Are they numeric?
- Are invalid values present?

---

## Task 9

Write the cleaned DataFrame as

```
silver.customers
```

using Delta format.

---

## Task 10

Validate the Silver table.

Compare:

- Bronze record count
- Silver record count
- Duplicate count
- NULL count

---

## Task 11 ⭐

Create a simple Data Quality Report.

Include:

- Total Bronze Records
- Total Silver Records
- Duplicate Records Removed
- NULL Values Found
- Transformations Applied

---

# 📚 Concepts Covered

- Bronze vs Silver Layer
- ETL Pipeline
- Data Cleansing
- Data Standardization
- Data Quality Validation
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many unique customers exist?

2. How many duplicate customer IDs were found?

3. Which state has the highest number of customers?

4. Which city has the highest number of customers?

5. How many distinct states are present?

---

# 🧠 Real Interview Questions

### Q1

What is the purpose of the Silver layer?

---

### Q2

Why do we remove duplicates in the Silver layer instead of the Bronze layer?

---

### Q3

Why should city names be standardized?

---

### Q4

What kinds of transformations belong in the Silver layer?

---

### Q5

How would you validate that your Silver table is reliable?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Customers Notebook Created

✓ Bronze Table Read Successfully

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Customer Data Standardized

✓ Silver Customers Table Created

✓ Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 10, you will have created your **first Silver Delta table**.

Your Lakehouse will now contain:

```
Bronze
│
├── customers
├── orders
├── order_items
├── products
├── sellers
├── order_payments
├── order_reviews
├── geolocation
└── product_category_translation

Silver
│
└── customers
```

This marks the transition from **raw data ingestion** to **trusted, analytics-ready data engineering**, a key milestone in every production Lakehouse project.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| **Sprint 2** | **OLIST-201** | **Transform Customers to Silver** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 11)

## 🚀 JIRA ID: OLIST-202

Transform the **Orders** dataset from the Bronze layer into the Silver layer by validating timestamps, checking order statuses, removing duplicates, and preparing clean transactional data for downstream analytics.
