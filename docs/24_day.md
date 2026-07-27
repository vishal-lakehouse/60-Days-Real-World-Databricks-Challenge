# Day 24 — Sprint 3

# 🚀 JIRA ID: OLIST-306

## Epic

**Build Gold Layer**

---

# 📖 User Story

**As a Sales Director,**

I want a Regional Sales Analytics table,

so that I can compare sales performance across Brazilian states and cities, identify growth opportunities, and make strategic business decisions.

---

# 🎯 Objective

Today you will create a **Gold Regional Sales Analytics** table.

By the end of today's assignment, you will learn how to:

- Build region-level analytical datasets
- Calculate geographic business KPIs
- Perform multi-level aggregations
- Apply Window Functions
- Rank states and cities
- Create executive-ready dashboards
- Validate regional business metrics

---

# 🏢 Business Scenario

The executive leadership team wants to understand regional business performance.

They frequently ask questions like:

- Which states generate the highest revenue?
- Which cities have the most customers?
- Which regions have the highest average order value?
- Which states have the highest freight cost?
- Which regions have the largest seller network?

Currently, answering these questions requires joining several datasets.

Your responsibility is to build a **Regional Sales Analytics Gold** table that provides trusted regional KPIs for business reporting.

---

# 📂 Source Tables

```
gold.sales_summary

silver.customers

silver.sellers

silver.geolocation
```

---

# 🏗 Target Table

```
gold.regional_sales
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

✅ Customer and Seller locations validated

✅ Regional aggregations completed

✅ Business KPIs calculated

✅ Regional rankings generated

✅ Gold Delta table created

✅ Validation report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-306_Create_Gold_Regional_Sales
```

---

## Task 2

Read the following tables.

```
gold.sales_summary

silver.customers

silver.sellers

silver.geolocation
```

---

## Task 3

Create regional aggregations.

Group by

```
customer_state

customer_city
```

Calculate:

- Total Revenue
- Total Orders
- Total Customers
- Total Sellers
- Total Products Sold
- Average Order Value
- Average Freight Cost

---

## Task 4

Create regional KPIs.

Generate the following columns.

```
customer_state

customer_city

total_orders

total_customers

total_sellers

total_products_sold

total_revenue

average_order_value

average_freight

first_order_date

last_order_date
```

---

## Task 5

Create advanced business metrics.

Examples:

- Revenue per Customer
- Revenue per Seller
- Orders per Customer
- Freight Percentage
- Customer Density
- Seller Density
- Revenue Contribution (%)

Document the calculation logic.

---

## Task 6

Apply Window Functions.

Generate rankings using

```
ROW_NUMBER()

RANK()

DENSE_RANK()
```

Rank regions based on:

- Revenue
- Total Orders
- Total Customers
- Average Order Value

---

## Task 7

Create regional performance categories.

Example:

```
Tier 1 Region

Tier 2 Region

Tier 3 Region

Emerging Region
```

Define business rules for assigning each category.

---

## Task 8

Perform business validation.

Verify:

- Every customer location exists in Geolocation.
- Revenue is greater than zero.
- Customer count is not zero.
- No duplicate regional records exist.

Document all exceptions.

---

## Task 9

Write the DataFrame as

```
gold.regional_sales
```

using Delta format.

---

## Task 10

Validate the Gold table.

Verify:

- Record Count
- Duplicate Regions
- NULL Values
- Revenue Totals
- Regional Rankings

---

## Task 11 ⭐

Create a Regional Sales Validation Report.

Include:

- Source Tables
- Total States
- Total Cities
- Revenue Validation
- Ranking Validation
- KPI Validation
- Data Quality Checks
- Business Rules Applied

---

# 📚 Concepts Covered

- Geographic Analytics
- Regional KPIs
- Aggregations
- Window Functions
- Ranking
- Business Intelligence
- Gold Layer Design
- Delta Lake

---

# 💡 Mini Challenge

Answer the following using Spark SQL.

1. Top 10 states by revenue

2. Top 10 cities by revenue

3. State with the highest average order value

4. City with the highest number of customers

5. Revenue contribution of each state

6. Average freight cost by state

7. Top 5 states by number of sellers

8. Top 10 cities by products sold

9. States whose revenue is above the national average

10. Which region has the highest revenue per customer?

---

# 🧠 Real Interview Questions

### Q1

Why is regional analytics important for business decision-making?

---

### Q2

How would you calculate revenue contribution for each state?

---

### Q3

What is the benefit of using Window Functions for regional ranking?

---

### Q4

How would you identify underperforming regions?

---

### Q5

How would you validate that regional revenue matches the Sales Summary table?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Regional Sales Notebook Created

✓ Regional KPIs Calculated

✓ Window Functions Applied

✓ Regional Rankings Generated

✓ Performance Categories Created

✓ Gold Regional Sales Table Created

✓ Validation Report Generated

✓ Business Metrics Verified
```

---

# 🏁 End Goal

At the end of Day 24, your Lakehouse will contain:

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
├── category_performance
└── regional_sales
```

You have successfully built a **Regional Sales Analytics Gold table** that enables executives to analyse sales performance across cities and states, identify high-growth regions, optimise logistics, and support strategic expansion decisions.

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
| Sprint 3 | OLIST-305 | Create Gold Category Performance | ✅ Complete |
| **Sprint 3** | **OLIST-306** | **Create Gold Regional Sales** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 25)

## 🚀 JIRA ID: OLIST-307

Build the **Executive Business KPI Dashboard** Gold table by combining sales, customer, seller, product, and regional metrics into a single executive-ready dataset. You'll calculate business KPIs, month-over-month growth, top performers, operational metrics, and create a centralized data model designed for Power BI and executive reporting.
