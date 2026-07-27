# Day 15 — Sprint 2

# 🚀 JIRA ID: OLIST-206

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Order Payments** dataset from the Bronze layer into the Silver layer,

so that finance teams and business analysts can use accurate and validated payment information for reporting and analytics.

---

# 🎯 Objective

Today you will transform the **Order Payments** dataset into a trusted Silver Delta table.

By the end of today's assignment, you will learn how to:

- Validate payment transactions
- Verify composite primary keys
- Detect duplicate payment records
- Apply financial data quality rules
- Validate relationships with Orders
- Build production-ready ETL pipelines
- Generate Data Quality Reports

---

# 🏢 Business Scenario

Customers can pay for an order using one or multiple payment methods.

Each payment record contains:

- Payment Method
- Installment Count
- Payment Amount

Before this information is used for financial dashboards, fraud detection, and revenue reporting, it must be validated and standardized.

Your responsibility is to create a trusted **Silver Order Payments** table.

---

# 📂 Source Table

```
bronze.order_payments
```

---

# 🏗 Target Table

```
silver.order_payments
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

✅ Bronze Payments table read successfully

✅ Composite Primary Key validated

✅ Duplicate records removed

✅ Payment values validated

✅ Installment values validated

✅ Relationship with Orders validated

✅ Silver Delta table created

✅ Data Quality Report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-206_Transform_Order_Payments_Silver
```

---

## Task 2

Read

```
bronze.order_payments
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Review the following columns:

```
order_id

payment_sequential

payment_type

payment_installments

payment_value
```

---

## Task 4

Count total records.

Compare the result with the Bronze table.

---

## Task 5

Validate the Composite Primary Key.

```
order_id

payment_sequential
```

Remove duplicate combinations if found.

---

## Task 6

Analyse NULL values.

Check every column.

Document your findings.

---

## Task 7

Validate business rules.

Examples:

- Payment Value should be greater than zero.
- Installments should be greater than or equal to 1.
- Payment Type should not be NULL.
- Payment Sequential should start from 1.
- Payment Value should not be negative.

Identify all records violating these rules.

---

## Task 8

Standardize payment information.

Examples:

- Trim whitespace.
- Convert payment types to lowercase.
- Ensure numeric columns use appropriate data types.

Do not change business values.

---

## Task 9

Validate relationship with Orders.

Verify every payment belongs to an existing order.

Identify orphan payment records using:

```
LEFT ANTI JOIN
```

---

## Task 10

Write the transformed DataFrame as

```
silver.order_payments
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

Create a Payment Data Quality Report.

Include:

- Bronze Record Count
- Silver Record Count
- Duplicate Payments Removed
- NULL Values Found
- Invalid Payment Values
- Invalid Installment Values
- Missing Orders
- Transformations Applied

---

# 📚 Concepts Covered

- Financial Data Validation
- Composite Primary Keys
- Business Rule Validation
- Data Standardization
- Foreign Key Validation
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. Which payment method is used most frequently?

2. What is the average payment value for each payment method?

3. Which payment method generates the highest revenue?

4. What is the highest installment count?

5. How many orders have multiple payment transactions?

---

# 🧠 Real Interview Questions

### Q1

Why is the Payment table considered transactional data?

---

### Q2

Why do we validate payment amounts in the Silver layer?

---

### Q3

Why is a Composite Primary Key required for the Payments table?

---

### Q4

How would you identify payment records that do not belong to any order?

---

### Q5

Why shouldn't invalid payment records be deleted without business approval?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Order Payments Notebook Created

✓ Bronze Payments Table Read Successfully

✓ Composite Primary Key Validated

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Business Rule Validation Completed

✓ Orders Relationship Validated

✓ Payment Information Standardized

✓ Silver Order Payments Table Created

✓ Payment Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 15, your Lakehouse will contain:

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
└── order_payments
```

You now have a trusted financial dataset that supports payment analytics, revenue reporting, and financial KPIs.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 | Transform Customers | ✅ Complete |
| Sprint 2 | OLIST-202 | Transform Orders | ✅ Complete |
| Sprint 2 | OLIST-203 | Transform Order Items | ✅ Complete |
| Sprint 2 | OLIST-204 | Transform Products | ✅ Complete |
| Sprint 2 | OLIST-205 | Transform Sellers | ✅ Complete |
| **Sprint 2** | **OLIST-206** | **Transform Order Payments** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 16)

## 🚀 JIRA ID: OLIST-207

Transform the **Order Reviews** dataset from the Bronze layer into the Silver layer by validating review records, analysing customer ratings, handling missing review comments, enforcing data quality rules, and preparing trusted customer feedback data for downstream analytics and reporting.
