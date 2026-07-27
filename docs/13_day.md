# Day 13 — Sprint 2

# 🚀 JIRA ID: OLIST-204

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Products** dataset from the Bronze layer into the Silver layer,

so that business users can consume clean, standardized, and validated product master data for analytics and reporting.

---

# 🎯 Objective

Today you will transform the **Products** dataset into the Silver layer by applying data quality rules and validating product metadata.

By the end of today's assignment, you will learn how to:

- Read Delta tables
- Validate product master data
- Handle missing values
- Standardize product attributes
- Validate product categories
- Build trusted Silver tables
- Create data quality reports

---

# 🏢 Business Scenario

The Products dataset contains the master information for every product sold on the Olist marketplace.

This dataset is referenced by Order Items and plays a critical role in product analytics.

Before product data can be used by analysts, dashboards, and machine learning models, it must be validated and standardized.

Your responsibility is to build the **Silver Products** table.

---

# 📂 Source Table

```
bronze.products
```

---

# 🏗 Target Table

```
silver.products
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

✅ Bronze Products table read successfully

✅ Duplicate Product IDs removed

✅ Product metadata validated

✅ NULL values analysed

✅ Product categories validated

✅ Product dimensions validated

✅ Silver Delta table created

✅ Bronze vs Silver comparison completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-204_Transform_Products_Silver
```

---

## Task 2

Read

```
bronze.products
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Review the following columns:

```
product_id

product_category_name

product_name_length

product_description_length

product_photos_qty

product_weight_g

product_length_cm

product_height_cm

product_width_cm
```

---

## Task 4

Count total records.

Compare the result with the Bronze table.

---

## Task 5

Validate Product IDs.

Remove duplicate Product IDs if found.

---

## Task 6

Analyse NULL values.

Pay special attention to:

```
product_category_name

product_name_length

product_description_length

product_photos_qty
```

Document which NULL values are acceptable and which require investigation.

---

## Task 7

Validate business rules.

Examples:

- Product weight should be greater than zero.
- Product dimensions should be positive values.
- Photo quantity should not be negative.
- Name length should not be negative.
- Description length should not be negative.

Identify records that violate these rules.

---

## Task 8

Validate category relationships.

Verify every product category exists in:

```
bronze.product_category_translation
```

Identify:

- Products without category mappings
- Translation records not used by any product

Use:

```
LEFT JOIN

LEFT ANTI JOIN
```

---

## Task 9

Standardize product information.

Examples:

- Trim whitespace
- Standardize category names
- Ensure numeric columns use correct data types

Do not change business values.

---

## Task 10

Write the transformed DataFrame as

```
silver.products
```

using Delta format.

---

## Task 11

Validate the Silver table.

Compare:

- Bronze record count
- Silver record count
- Duplicate records removed
- Invalid records identified

---

## Task 12 ⭐

Create a Product Data Quality Report.

Include:

- Bronze Record Count
- Silver Record Count
- Duplicate Products Removed
- NULL Values Found
- Invalid Product Dimensions
- Invalid Product Weights
- Missing Category Mappings
- Transformations Applied

---

# 📚 Concepts Covered

- Master Data Management
- Data Standardization
- Business Rule Validation
- Data Quality Framework
- Delta Lake
- Spark SQL
- Lookup Table Validation

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many unique product categories exist?

2. Which category contains the highest number of products?

3. How many products do not have a category?

4. What is the average product weight?

5. Which product has the largest volume (Length × Width × Height)?

---

# 🧠 Real Interview Questions

### Q1

Why is the Products table considered master data?

---

### Q2

Why are lookup tables validated in the Silver layer?

---

### Q3

How would you identify products with invalid dimensions?

---

### Q4

Why shouldn't missing categories be filled with default values in the Silver layer without business approval?

---

### Q5

How would you ensure the Products table is reliable for downstream analytics?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Products Notebook Created

✓ Bronze Products Table Read Successfully

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Business Rule Validation Completed

✓ Category Validation Completed

✓ Silver Products Table Created

✓ Product Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 13, your Lakehouse will contain:

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
└── products
```

You now have a trusted Product Master dataset that supports order analytics, inventory reporting, product performance, and category-based insights.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 | Transform Customers | ✅ Complete |
| Sprint 2 | OLIST-202 | Transform Orders | ✅ Complete |
| Sprint 2 | OLIST-203 | Transform Order Items | ✅ Complete |
| **Sprint 2** | **OLIST-204** | **Transform Products** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 14)

## 🚀 JIRA ID: OLIST-205

Transform the **Sellers** dataset from the Bronze layer into the Silver layer by validating seller information, standardizing location data, checking for duplicate sellers, and preparing trusted seller master data for downstream analytics.
