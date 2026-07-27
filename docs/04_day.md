# Day 04 — Sprint 1

# 🚀 JIRA ID: OLIST-104

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Products** dataset into the Bronze layer,

so that product information is available for downstream analytics, reporting, and business transformations.

---

# 🎯 Objective

Today you will ingest the **Products** dataset and understand how product master data supports transactional datasets.

By the end of today's assignment, you will learn how to:

- Load master data into Databricks
- Validate product information
- Handle nullable columns
- Analyse product categories
- Create Delta tables
- Validate relationships with Order Items

---

# 🏢 Business Scenario

The Olist marketplace maintains a master catalogue of all products sold by different sellers.

This dataset contains information such as:

- Product Category
- Product Dimensions
- Product Weight
- Product Images
- Product Description Length

As a Data Engineer, your responsibility is to ingest this dataset into the Bronze layer exactly as received.

---

# 📂 Source Dataset

```
datasets/raw/olist_products_dataset.csv
```

---

# 🏗 Target Layer

```
bronze.products
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

✅ Products CSV uploaded

✅ Data read successfully

✅ Schema validated

✅ Product IDs validated

✅ NULL value analysis completed

✅ Bronze Delta table created

✅ Relationship with Order Items validated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-104_Load_Products_Bronze
```

---

## Task 2

Upload

```
olist_products_dataset.csv
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

- Product Category
- Weight
- Height
- Width
- Length

---

## Task 6

Count total products.

---

## Task 7

Check duplicate Product IDs.

---

## Task 8

Analyse NULL values in all columns.

Pay special attention to:

```
product_category_name

product_name_length

product_description_length

product_photos_qty
```

Remember:

Do **not** clean the data in the Bronze layer.

---

## Task 9

Save the DataFrame as

```
bronze.products
```

using Delta format.

---

## Task 10

Validate relationship with Order Items.

Questions:

- Does every Order Item reference a valid Product?
- Are there Product IDs that never appear in any Order?

Use:

```
LEFT ANTI JOIN

LEFT JOIN
```

---

## Task 11

Explore Product Categories.

Find:

- Total categories
- Top 10 categories with the most products
- Products without a category

---

# 📚 Concepts Covered

- Master Data
- Product Dimension
- Data Profiling
- NULL Analysis
- LEFT JOIN
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many unique product categories exist?

2. Which category contains the most products?

3. What is the heaviest product?

4. What is the average product weight?

5. Which products have missing category information?

---

# 🧠 Real Interview Questions

### Q1

Why is the Products table considered master data?

---

### Q2

Why shouldn't missing categories be fixed in the Bronze layer?

---

### Q3

Why is product metadata important for analytics?

---

### Q4

What is the purpose of a Delta table?

---

### Q5

How would you validate that every Order Item references a valid Product?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Products Notebook Created

✓ Products CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ Duplicate Check Completed

✓ NULL Analysis Completed

✓ Bronze Products Table Created

✓ Order Items Relationship Validated

✓ Product Category Analysis Completed
```

---

# 🏁 End Goal

At the end of Day 4, you will have four production-ready Bronze Delta tables:

```
bronze.customers

bronze.orders

bronze.order_items

bronze.products
```

You will also understand how **master data (Products)** connects with **transactional data (Order Items)**, enabling future product analytics.

---

# 📈 Sprint Progress

| JIRA ID | Task | Status |
|----------|------|--------|
| OLIST-101 | Load Customers | ✅ Complete |
| OLIST-102 | Load Orders | ✅ Complete |
| OLIST-103 | Load Order Items | ✅ Complete |
| **OLIST-104** | **Load Products** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 05)

**🚀 JIRA ID: OLIST-105**

Load the **Sellers** dataset into the Bronze layer and validate its relationship with the Order Items dataset. By the end of Day 5, you'll have all the core transactional and master datasets ingested into the Bronze layer.
