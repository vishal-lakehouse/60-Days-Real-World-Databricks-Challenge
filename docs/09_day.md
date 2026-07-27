# Day 09 — Sprint 1

# 🚀 JIRA ID: OLIST-109

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Product Category Translation** dataset into the Bronze layer,

so that Portuguese product categories can later be translated into English during Silver layer transformations.

---

# 🎯 Objective

Today you will ingest the **Product Category Translation** dataset and complete the Bronze layer ingestion for the Olist project.

By the end of today's assignment, you will learn how to:

- Load reference datasets into Databricks
- Validate lookup tables
- Analyse category mappings
- Create Delta tables
- Validate relationships with the Products dataset
- Complete the Bronze Layer

---

# 🏢 Business Scenario

The Olist marketplace stores product categories in Portuguese.

To make reporting easier for international users, Olist provides a translation table that maps Portuguese category names to English.

This dataset acts as a **lookup table** and will later be used in the Silver layer to standardise product categories.

Your responsibility is to ingest this dataset exactly as received.

No translations.

No corrections.

No transformations.

Only ingestion and validation.

---

# 📂 Source Dataset

```
datasets/raw/product_category_name_translation.csv
```

---

# 🏗 Target Layer

```
bronze.product_category_translation
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

✅ Translation CSV uploaded

✅ Data read successfully

✅ Schema validated

✅ Duplicate categories checked

✅ NULL values analysed

✅ Bronze Delta table created

✅ Relationship with Products validated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-109_Load_Product_Category_Translation_Bronze
```

---

## Task 2

Upload

```
product_category_name_translation.csv
```

---

## Task 3

Read the CSV into a Spark DataFrame.

---

## Task 4

Display the first 10 records.

---

## Task 5

Print the schema.

Identify:

- product_category_name
- product_category_name_english

---

## Task 6

Count total records.

---

## Task 7

Check duplicate category names.

Questions:

- Are category names unique?
- Are duplicate mappings present?

---

## Task 8

Analyse NULL values.

Check every column for missing values.

Remember:

Do **not** modify missing values in the Bronze layer.

---

## Task 9

Save the DataFrame as

```
bronze.product_category_translation
```

using Delta format.

---

## Task 10

Validate relationship with Products.

Questions:

- Does every product category have an English translation?
- Are there product categories without a matching translation?
- Are there translations that are never used by any product?

Use:

```
LEFT JOIN

LEFT ANTI JOIN
```

---

## Task 11

Explore Category Translation.

Find:

- Total translated categories
- Categories without translation
- Alphabetically first category
- Alphabetically last category

---

# 📚 Concepts Covered

- Lookup Tables
- Reference Data
- LEFT JOIN
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL
- Data Validation

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many category mappings exist?

2. Are there duplicate Portuguese category names?

3. How many products do not have a matching translation?

4. Which translated category is used the most?

5. Are there translations that are never referenced by any product?

---

# 🧠 Real Interview Questions

### Q1

What is a lookup table?

---

### Q2

Why is a translation table useful in a data warehouse?

---

### Q3

Why shouldn't translations be applied in the Bronze layer?

---

### Q4

How would you identify products without a valid category translation?

---

### Q5

Why is this dataset considered reference data instead of transactional data?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Product Category Translation Notebook Created

✓ Translation CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ Duplicate Check Completed

✓ NULL Analysis Completed

✓ Bronze Translation Table Created

✓ Products Relationship Validated

✓ Category Analysis Completed
```

---

# 🏁 End Goal

At the end of Day 9, you will have successfully completed the **Bronze Layer** of the Olist Lakehouse project.

Your Bronze layer now contains:

```
bronze.customers

bronze.orders

bronze.order_items

bronze.products

bronze.sellers

bronze.order_payments

bronze.order_reviews

bronze.geolocation

bronze.product_category_translation
```

You now have all raw datasets securely stored as Delta tables and ready for cleansing, validation, and standardisation in the Silver layer.

---

# 🎉 Sprint 1 Completed

## Sprint Goal

Successfully ingest all source datasets into the Bronze layer while preserving the raw data exactly as received.

### Sprint Deliverables

```
✓ 9 Bronze Delta Tables Created

✓ Source Data Successfully Ingested

✓ Schemas Validated

✓ Primary & Composite Keys Reviewed

✓ Foreign Key Relationships Validated

✓ Basic Data Profiling Completed

✓ SQL Validation Queries Executed

✓ Bronze Layer Ready for Silver Transformations
```

---

# 📈 Sprint Progress

| JIRA ID | Task | Status |
|----------|------|--------|
| OLIST-101 | Load Customers | ✅ Complete |
| OLIST-102 | Load Orders | ✅ Complete |
| OLIST-103 | Load Order Items | ✅ Complete |
| OLIST-104 | Load Products | ✅ Complete |
| OLIST-105 | Load Sellers | ✅ Complete |
| OLIST-106 | Load Order Payments | ✅ Complete |
| OLIST-107 | Load Order Reviews | ✅ Complete |
| OLIST-108 | Load Geolocation | ✅ Complete |
| **OLIST-109** | **Load Product Category Translation** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 10)

## 🚀 Sprint 2 Begins — Build the Silver Layer

**JIRA ID: OLIST-201**

Create the **Silver Customers** pipeline by cleaning, validating, and standardising customer data from the Bronze layer. You'll perform your first real ETL transformation using PySpark and Delta Lake while preserving data quality for downstream analytics.
