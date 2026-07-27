# Day 11 — Sprint 2

# 🚀 JIRA ID: OLIST-202

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Orders** dataset from the Bronze layer into the Silver layer,

so that downstream applications can use clean, validated, and standardized order data for analytics and reporting.

---

# 🎯 Objective

Today you will transform the **Orders** dataset into a trusted Silver Delta table.

By the end of today's assignment, you will learn how to:

- Read Delta tables
- Validate timestamp columns
- Validate business rules
- Standardize order status values
- Remove duplicate records
- Build production-ready ETL pipelines
- Perform data quality validation

---

# 🏢 Business Scenario

The Bronze Orders table contains raw transactional data received from the Olist platform.

Before this data can be consumed by analysts, dashboards, and machine learning models, it must be validated and standardized.

As a Data Engineer, your responsibility is to build a reliable Silver Orders table while preserving the business meaning of the data.

---

# 📂 Source Table

```
bronze.orders
```

---

# 🏗 Target Table

```
silver.orders
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

✅ Bronze Orders table read successfully

✅ Duplicate orders removed

✅ Timestamp columns validated

✅ Order status standardized

✅ NULL values analysed

✅ Business rules validated

✅ Silver Delta table created

✅ Bronze vs Silver comparison completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-202_Transform_Orders_Silver
```

---

## Task 2

Read

```
bronze.orders
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Review the following timestamp columns:

```
order_purchase_timestamp

order_approved_at

order_delivered_carrier_date

order_delivered_customer_date

order_estimated_delivery_date
```

---

## Task 4

Count total records.

Compare the result with the Bronze table.

---

## Task 5

Check duplicate records using

```
order_id
```

Remove duplicates if found.

---

## Task 6

Analyse NULL values.

Pay special attention to:

```
order_approved_at

order_delivered_carrier_date

order_delivered_customer_date
```

Think about whether NULL values are expected based on the order status.

---

## Task 7

Validate business rules.

Examples:

- Delivery date should not be before purchase date.
- Approval date should not be before purchase date.
- Estimated delivery date should usually be after purchase date.
- Delivered orders should have a delivery timestamp.

Identify any records that violate these rules.

---

## Task 8

Standardize order status values.

Examples:

- Remove extra spaces
- Convert to lowercase (or another consistent format)

---

## Task 9

Write the transformed DataFrame as

```
silver.orders
```

using Delta format.

---

## Task 10

Validate the Silver table.

Compare:

- Bronze record count
- Silver record count
- Duplicate records removed
- Invalid records identified

---

## Task 11 ⭐

Create a Data Quality Report.

Include:

- Total Bronze Records
- Total Silver Records
- Duplicate Records Removed
- NULL Values Found
- Invalid Timestamp Records
- Business Rule Violations
- Transformations Applied

---

# 📚 Concepts Covered

- Silver Layer
- Data Quality
- Business Rule Validation
- Timestamp Validation
- Data Standardization
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many unique order statuses exist?

2. Which order status occurs most frequently?

3. How many delivered orders exist?

4. How many cancelled orders exist?

5. Are there any orders delivered after the estimated delivery date?

---

# 🧠 Real Interview Questions

### Q1

Why are business rule validations performed in the Silver layer instead of the Bronze layer?

---

### Q2

Why can some timestamp columns legitimately contain NULL values?

---

### Q3

How would you detect orders with inconsistent timestamps?

---

### Q4

Why is it important to standardize categorical columns like `order_status`?

---

### Q5

How would you ensure the Silver Orders table is reliable for downstream analytics?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Orders Notebook Created

✓ Bronze Orders Table Read Successfully

✓ Timestamp Validation Completed

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Business Rule Validation Completed

✓ Silver Orders Table Created

✓ Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 11, your Lakehouse will contain:

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
└── orders
```

You now have clean and trusted customer and order data, forming the foundation for transactional analytics in the Silver layer.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 | Transform Customers | ✅ Complete |
| **Sprint 2** | **OLIST-202** | **Transform Orders** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 12)

## 🚀 JIRA ID: OLIST-203

Transform the **Order Items** dataset from the Bronze layer into the Silver layer by validating composite primary keys, checking product and seller references, validating pricing and freight values, and preparing clean transactional data for downstream analytics.
