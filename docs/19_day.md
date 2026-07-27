# Day 19 — Sprint 3

# 🚀 JIRA ID: OLIST-301

## Epic

**Build Gold Layer**

---

# 📖 User Story

**As a Business Intelligence Analyst,**

I want a consolidated Sales Summary table,

so that I can analyse revenue, orders, customers, products, and sellers without joining multiple tables every time.

---

# 🎯 Objective

Today you will create your **first Gold Layer table**.

By the end of today's assignment, you will learn how to:

- Design a Gold table
- Join multiple Silver tables
- Create business-ready datasets
- Build analytical fact tables
- Apply aggregation techniques
- Write production-ready Spark SQL
- Validate business KPIs

---

# 🏢 Business Scenario

The Sales Team currently receives data from multiple tables.

Whenever they need answers like:

- Total Sales
- Number of Orders
- Best Selling Products
- Revenue by State
- Revenue by Seller

they must manually join several datasets.

This process is slow, error-prone, and inefficient.

As a Data Engineer, your responsibility is to build a **Gold Sales Summary** table that provides a single source of truth for business reporting.

---

# 📂 Source Tables

```
silver.orders

silver.order_items

silver.order_payments

silver.customers

silver.products

silver.sellers

silver.product_category_translation
```

---

# 🏗 Target Table

```
gold.sales_summary
```

---

# 🛠 Technologies

- Azure Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake

---

# 📋 Acceptance Criteria

✅ All required Silver tables read successfully

✅ Business joins completed

✅ Duplicate orders avoided

✅ Gold Sales Summary created

✅ Revenue calculations validated

✅ Gold Delta table created

✅ Business metrics verified

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-301_Create_Gold_Sales_Summary
```

---

## Task 2

Read the following Silver tables:

```
silver.orders

silver.order_items

silver.order_payments

silver.customers

silver.products

silver.sellers

silver.product_category_translation
```

---

## Task 3

Understand the relationships between the tables.

Identify the join keys.

Example:

```
orders
      │
      ├── order_id
      │
order_items
      │
      ├── product_id
      ├── seller_id
      │
products
      │
      ├── product_category_name
      │
category_translation

orders
      │
      ├── customer_id
      │
customers

orders
      │
      ├── order_id
      │
payments
```

Document the relationship diagram inside your notebook.

---

## Task 4

Create the business joins.

Use appropriate joins to combine all required datasets into one DataFrame.

Ensure no unnecessary duplicate rows are introduced.

---

## Task 5

Select business columns.

Examples:

```
order_id

customer_id

seller_id

product_id

order_purchase_timestamp

customer_city

customer_state

seller_city

seller_state

product_category_name_english

payment_type

payment_value

price

freight_value
```

Only include columns useful for analytics.

---

## Task 6

Validate business rules.

Examples:

- Every order should have a customer.
- Every order item should belong to an order.
- Every payment should belong to an order.
- Product category should have an English translation.
- Payment Value should be greater than zero.

Document any exceptions.

---

## Task 7

Validate duplicates.

Verify that:

```
order_id

product_id

seller_id
```

do not create unintended duplicate business records.

---

## Task 8

Write the DataFrame as

```
gold.sales_summary
```

using Delta format.

---

## Task 9

Validate the Gold table.

Verify:

- Record Count
- NULL values
- Revenue totals
- Duplicate Orders
- Duplicate Products

---

## Task 10 ⭐

Create a Gold Validation Report.

Include:

- Source Tables Used
- Record Count
- Revenue Validation
- Duplicate Check
- Join Validation
- Missing Records
- Business Rules Applied

---

# 📚 Concepts Covered

- Gold Layer
- Fact Tables
- Business Joins
- Star Schema Foundation
- Spark SQL Joins
- Delta Lake
- Data Validation

---

# 💡 Mini Challenge

Answer the following using Spark SQL.

1. Total Revenue

2. Total Orders

3. Total Customers

4. Total Sellers

5. Total Products Sold

6. Average Order Value

7. Top 10 Selling Categories

8. Top 10 States by Revenue

9. Most Used Payment Type

10. Top 10 Sellers by Revenue

---

# 🧠 Real Interview Questions

### Q1

Why is the Gold layer created instead of querying Silver tables directly?

---

### Q2

What is the difference between a Fact table and a Dimension table?

---

### Q3

Why should business users access Gold tables instead of Bronze tables?

---

### Q4

How would you validate that revenue has not changed after joining multiple tables?

---

### Q5

What techniques would you use to avoid duplicate records after joining several datasets?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Gold Sales Summary Notebook Created

✓ Silver Tables Read Successfully

✓ Business Relationships Verified

✓ Business Joins Completed

✓ Gold Sales Summary Created

✓ Revenue Validated

✓ Duplicate Validation Completed

✓ Gold Delta Table Created

✓ Gold Validation Report Generated
```

---

# 🏁 End Goal

At the end of Day 19, your Lakehouse will contain:

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

Gold
│
└── sales_summary
```

You have successfully built your first **business-ready Gold table**, providing a single source of truth for sales analytics and reporting.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| **Sprint 3** | **OLIST-301** | **Create Gold Sales Summary** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 20)

## 🚀 JIRA ID: OLIST-302

Build the **Customer Analytics** Gold table by aggregating customer purchase history, total spending, average order value, purchase frequency, and lifetime value (LTV). You'll learn advanced aggregations, window functions, customer segmentation, and how to create analytics-ready dimension tables for marketing and customer insights.
