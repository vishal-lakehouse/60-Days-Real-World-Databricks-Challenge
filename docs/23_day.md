# Day 23 — Sprint 3

# 🚀 JIRA ID: OLIST-305

## Epic

**Build Gold Layer**

---

# 📖 User Story

**As a Category Manager,**

I want a Category Performance Analytics table,

so that I can understand which product categories generate the highest revenue, sales volume, and customer satisfaction, allowing the business to make better merchandising and inventory decisions.

---

# 🎯 Objective

Today you will create a **Gold Category Performance Analytics** table.

By the end of today's assignment, you will learn how to:

- Build category-level analytical datasets
- Calculate business KPIs
- Perform advanced aggregations
- Apply Window Functions
- Rank product categories
- Create executive-ready business reports
- Validate analytical datasets

---

# 🏢 Business Scenario

The executive management team wants to monitor category performance across the marketplace.

They frequently ask questions like:

- Which product categories generate the highest revenue?
- Which categories sell the most products?
- Which categories receive the highest customer ratings?
- Which categories have the highest freight costs?
- Which categories have the highest average selling price?

Currently, answering these questions requires joining several datasets and writing complex SQL queries.

Your responsibility is to create a **Gold Category Performance** table that provides all important category metrics in one place.

---

# 📂 Source Tables

```
gold.sales_summary

gold.product_performance

silver.product_category_translation
```

---

# 🏗 Target Table

```
gold.category_performance
```

---

# 🛠 Technologies

- Azure Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Window Functions

---

# 📋 Acceptance Criteria

✅ Gold Sales Summary read successfully

✅ Product Performance table read successfully

✅ Category-level aggregations completed

✅ Business KPIs calculated

✅ Category rankings generated

✅ Gold Delta table created

✅ Validation report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-305_Create_Gold_Category_Performance
```

---

## Task 2

Read the following tables.

```
gold.sales_summary

gold.product_performance

silver.product_category_translation
```

---

## Task 3

Create category-level aggregations.

Group by

```
product_category_name_english
```

Calculate:

- Total Revenue
- Total Orders
- Total Products Sold
- Average Selling Price
- Average Freight Cost
- Average Review Score

---

## Task 4

Create business KPIs.

Generate the following columns.

```
product_category_name_english

total_products

total_orders

total_quantity_sold

total_revenue

average_product_price

average_review_score

average_freight

first_sale_date

last_sale_date
```

---

## Task 5

Create advanced business metrics.

Examples:

- Revenue per Product
- Revenue Contribution (%)
- Average Revenue per Order
- Average Quantity per Order
- Freight Cost Percentage
- Category Profitability Index

Document the calculation logic.

---

## Task 6

Apply Window Functions.

Generate rankings using:

```
ROW_NUMBER()

RANK()

DENSE_RANK()
```

Rank categories based on:

- Revenue
- Quantity Sold
- Average Review Score
- Average Selling Price

---

## Task 7

Create business categories.

Example:

```
Diamond Category

Gold Category

Silver Category

Bronze Category
```

Define logical business rules for assigning each category.

---

## Task 8

Perform business validation.

Verify:

- Every category exists in the translation table.
- Revenue is greater than zero.
- Review Score is between **1** and **5**.
- No duplicate category records exist.

Document all exceptions.

---

## Task 9

Write the DataFrame as

```
gold.category_performance
```

using Delta format.

---

## Task 10

Validate the Gold table.

Verify:

- Record Count
- Duplicate Categories
- NULL Values
- Revenue Totals
- Category Rankings

---

## Task 11 ⭐

Create a Category Performance Validation Report.

Include:

- Source Tables
- Total Categories
- Revenue Validation
- Ranking Validation
- KPI Validation
- Data Quality Checks
- Business Rules Applied

---

# 📚 Concepts Covered

- Category Analytics
- Business KPIs
- Aggregations
- Window Functions
- Ranking
- Executive Reporting
- Gold Layer Design
- Delta Lake

---

# 💡 Mini Challenge

Answer the following using Spark SQL.

1. Top 10 categories by revenue

2. Top 10 categories by quantity sold

3. Highest-rated product category

4. Category with the highest average selling price

5. Category with the highest freight cost

6. Revenue contribution of each category

7. Top 5 categories by average review score

8. Categories whose revenue is above the overall average

9. Categories with the largest number of products sold

10. Which category generates the highest revenue per product?

---

# 🧠 Real Interview Questions

### Q1

Why is category-level aggregation useful for business reporting?

---

### Q2

Why should category KPIs be stored in the Gold layer instead of recalculated every time?

---

### Q3

How would you calculate the revenue contribution of each category?

---

### Q4

What is the difference between product-level analytics and category-level analytics?

---

### Q5

How would you validate that category revenue matches the Sales Summary table?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Category Performance Notebook Created

✓ Category KPIs Calculated

✓ Window Functions Applied

✓ Category Rankings Generated

✓ Business Categories Created

✓ Gold Category Performance Table Created

✓ Validation Report Generated

✓ Business Metrics Verified
```

---

# 🏁 End Goal

At the end of Day 23, your Lakehouse will contain:

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
├── sales_summary
├── customer_analytics
├── seller_performance
├── product_performance
└── category_performance
```

You have successfully built a **Category Performance Analytics Gold table** that enables executives to monitor category revenue, customer satisfaction, product demand, and overall marketplace performance using a single trusted analytical dataset.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| Sprint 3 | OLIST-301 | Create Gold Sales Summary | ✅ Complete |
| Sprint 3 | OLIST-302 | Create Gold Customer Analytics | ✅ Complete |
| Sprint 3 | OLIST-303 | Create Gold Seller Performance | ✅ Complete |
| Sprint 3 | OLIST-304 | Create Gold Product Performance | ✅ Complete |
| **Sprint 3** | **OLIST-305** | **Create Gold Category Performance** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 24)

## 🚀 JIRA ID: OLIST-306

Build the **Regional Sales Analytics** Gold table by analysing sales performance across Brazilian states and cities. You'll calculate regional revenue, customer distribution, seller distribution, average order value, freight trends, and regional rankings while learning geographic analytics, dimensional modelling, and executive KPI reporting.
