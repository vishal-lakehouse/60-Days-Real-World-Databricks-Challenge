# Day 18 — Sprint 2

# 🚀 JIRA ID: OLIST-209

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Product Category Translation** dataset from the Bronze layer into the Silver layer,

so that product categories are standardized and ready for business reporting and analytics.

---

# 🎯 Objective

Today you will build the final Silver table and complete the entire **Silver Layer**.

By the end of today's assignment, you will learn how to:

- Validate lookup tables
- Standardize category names
- Validate one-to-one mappings
- Detect duplicate mappings
- Validate relationships with Products
- Build production-ready lookup tables
- Generate a Data Quality Report

---

# 🏢 Business Scenario

The Olist platform stores product categories in Portuguese.

To support international reporting and analytics, these categories must be translated into English using a lookup table.

This lookup table is referenced throughout the reporting layer and must therefore be accurate, complete, and standardized.

Your responsibility is to create a trusted **Silver Product Category Translation** table.

---

# 📂 Source Table

```
bronze.product_category_translation
```

---

# 🏗 Target Table

```
silver.product_category_translation
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

✅ Bronze Translation table read successfully

✅ Duplicate category mappings analysed

✅ NULL values analysed

✅ Category names standardized

✅ Relationship with Products validated

✅ Silver Delta table created

✅ Data Quality Report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-209_Transform_Product_Category_Translation_Silver
```

---

## Task 2

Read

```
bronze.product_category_translation
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Review the following columns:

```
product_category_name

product_category_name_english
```

---

## Task 4

Count total records.

Compare the result with the Bronze table.

---

## Task 5

Validate duplicate mappings.

Questions:

- Are Portuguese category names unique?
- Are English translations duplicated?
- Are there conflicting translations for the same category?

Document your findings.

---

## Task 6

Analyse NULL values.

Check every column.

Document all observations.

---

## Task 7

Validate business rules.

Examples:

- Portuguese category name should not be NULL.
- English category name should not be NULL.
- One Portuguese category should map to only one English category.
- Category names should not contain unnecessary whitespace.

Identify all records violating these rules.

---

## Task 8

Standardize category information.

Examples:

- Trim leading and trailing spaces.
- Convert category names to lowercase.
- Ensure consistent naming format.

Do not change the actual translation.

---

## Task 9

Validate relationships.

Verify that every category used in

```
silver.products
```

has a matching translation.

Also identify:

- Categories used by Products but missing in the translation table.
- Translation records that are never referenced by any Product.

Use:

```
LEFT JOIN

LEFT ANTI JOIN
```

---

## Task 10

Write the transformed DataFrame as

```
silver.product_category_translation
```

using Delta format.

---

## Task 11

Validate the Silver table.

Compare:

- Bronze Record Count
- Silver Record Count
- Duplicate Records Removed
- Invalid Records Found

---

## Task 12 ⭐

Create a Category Translation Data Quality Report.

Include:

- Bronze Record Count
- Silver Record Count
- Duplicate Mappings Removed
- NULL Values Found
- Missing Product Categories
- Unused Translation Records
- Standardization Rules Applied
- Transformations Applied

---

# 📚 Concepts Covered

- Lookup Tables
- Reference Data
- One-to-One Mapping Validation
- Data Standardization
- LEFT JOIN
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many product categories exist?

2. How many categories are missing English translations?

3. Are there duplicate English category names?

4. How many product categories are not used by any product?

5. Which translated category contains the highest number of products?

---

# 🧠 Real Interview Questions

### Q1

Why are lookup tables important in a data warehouse?

---

### Q2

Why shouldn't translations be changed during ETL without business approval?

---

### Q3

How would you identify products that don't have a valid category translation?

---

### Q4

Why is relationship validation important for lookup tables?

---

### Q5

What would happen if the translation table contained duplicate mappings?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Category Translation Notebook Created

✓ Bronze Translation Table Read Successfully

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Business Rule Validation Completed

✓ Product Relationship Validation Completed

✓ Silver Translation Table Created

✓ Category Translation Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 18, you will have successfully completed the **Silver Layer**.

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
├── customers
├── orders
├── order_items
├── products
├── sellers
├── order_payments
├── order_reviews
├── geolocation
└── product_category_translation
```

You now have a fully validated and standardized Silver layer that serves as the trusted foundation for business analytics, reporting, dashboards, and machine learning.

---

# 🎉 Sprint 2 Completed

## Sprint Goal

Transform all Bronze tables into clean, validated, and trusted Silver Delta tables.

### Sprint Deliverables

```
✓ 9 Silver Delta Tables Created

✓ Data Quality Rules Applied

✓ Duplicate Records Removed

✓ Business Rules Validated

✓ Foreign Key Relationships Verified

✓ Lookup Tables Standardized

✓ Data Quality Reports Generated

✓ Silver Layer Ready for Gold Transformations
```

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |

---

# 🔜 Tomorrow (Day 19)

## 🚀 Sprint 3 Begins — Build the Gold Layer

**JIRA ID: OLIST-301**

Create the **Sales Summary** Gold table by joining Customers, Orders, Order Items, Products, Sellers, and Payments to build your first business-ready fact table. You'll learn dimensional modelling, aggregations, business KPIs, and how to create analytics-ready datasets for Power BI and executive dashboards.
