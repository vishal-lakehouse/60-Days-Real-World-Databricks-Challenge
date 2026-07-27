# Day 12 — Sprint 2

# 🚀 JIRA ID: OLIST-203

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Order Items** dataset from the Bronze layer into the Silver layer,

so that downstream analytics can use clean, validated, and trustworthy order item data.

---

# 🎯 Objective

Today you will transform the **Order Items** dataset into the Silver layer by applying data quality rules and validating relationships with other datasets.

By the end of today's assignment, you will learn how to:

- Read Delta tables
- Validate Composite Primary Keys
- Remove duplicate records
- Validate business rules
- Validate foreign key relationships
- Standardize transactional data
- Generate Data Quality Reports

---

# 🏢 Business Scenario

Each customer order may contain one or more products.

Every order item represents:

- One Product
- One Seller
- One Price
- One Freight Charge

Before analysts can calculate revenue, profit, and sales KPIs, the Order Items dataset must be validated and standardized.

Your responsibility is to build a trusted Silver Order Items table.

---

# 📂 Source Table

```
bronze.order_items
```

---

# 🏗 Target Table

```
silver.order_items
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

✅ Composite Primary Key validated

✅ Duplicate records removed

✅ NULL values analysed

✅ Product references validated

✅ Seller references validated

✅ Price and freight values validated

✅ Silver Delta table created

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-203_Transform_Order_Items_Silver
```

---

## Task 2

Read

```
bronze.order_items
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Review the following columns:

```
order_id

order_item_id

product_id

seller_id

shipping_limit_date

price

freight_value
```

---

## Task 4

Count total records.

Compare with the Bronze table.

---

## Task 5

Validate the Composite Primary Key.

```
order_id

order_item_id
```

Remove duplicate combinations if found.

---

## Task 6

Analyse NULL values.

Check:

```
order_id

order_item_id

product_id

seller_id

price

freight_value
```

Document all observations.

---

## Task 7

Validate business rules.

Examples:

- Price should be greater than zero.
- Freight value should not be negative.
- Shipping limit date should not be NULL.
- Product ID should exist.
- Seller ID should exist.

Identify invalid records.

---

## Task 8

Validate relationships.

Verify that every record references valid data in:

```
silver.orders

silver.products (after Day 13)

silver.sellers (after Day 14)
```

Use:

```
LEFT ANTI JOIN
```

to identify orphan records.

---

## Task 9

Standardize the dataset.

Examples:

- Trim whitespace from string columns.
- Ensure consistent data types.
- Preserve original business values.

---

## Task 10

Write the transformed DataFrame as

```
silver.order_items
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

Create a Data Quality Report.

Include:

- Bronze Record Count
- Silver Record Count
- Duplicate Records Removed
- NULL Values Found
- Invalid Prices
- Invalid Freight Values
- Missing Product References
- Missing Seller References
- Transformations Applied

---

# 📚 Concepts Covered

- Composite Primary Keys
- Data Quality Rules
- Foreign Key Validation
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL
- Data Standardization

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. Which product appears in the highest number of orders?

2. Which seller has sold the most order items?

3. What is the average product price?

4. What is the average freight value?

5. Which order contains the highest number of products?

---

# 🧠 Real Interview Questions

### Q1

Why does the Order Items table use a Composite Primary Key instead of a single Primary Key?

---

### Q2

Why should product and seller relationships be validated in the Silver layer?

---

### Q3

How would you detect duplicate Order Items?

---

### Q4

Why should negative freight values be considered invalid?

---

### Q5

How would you ensure that every Order Item belongs to a valid Order?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Order Items Notebook Created

✓ Bronze Table Read Successfully

✓ Composite Primary Key Validated

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Business Rules Validated

✓ Foreign Key Validation Completed

✓ Silver Order Items Table Created

✓ Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 12, your Lakehouse will contain:

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
└── order_items
```

You now have a clean and validated transactional model covering customers, orders, and order items—the core foundation for revenue, sales, and product analytics.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 | Transform Customers | ✅ Complete |
| Sprint 2 | OLIST-202 | Transform Orders | ✅ Complete |
| **Sprint 2** | **OLIST-203** | **Transform Order Items** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 13)

## 🚀 JIRA ID: OLIST-204

Transform the **Products** dataset from the Bronze layer into the Silver layer by validating product metadata, handling missing category information, standardizing product attributes, and preparing trusted product master data for analytics and reporting.
