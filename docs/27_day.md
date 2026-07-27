# Day 27 — Sprint 3

# 🚀 JIRA ID: OLIST-309

## Epic

**Build Gold Layer**

---

# 📖 User Story

**As a Business Analyst,**

I want a Monthly Sales Trend Analytics table,

so that I can analyse revenue trends, seasonality, customer growth, and business performance over time to support forecasting and executive decision-making.

---

# 🎯 Objective

Today you will build a **Gold Monthly Sales Trend Analytics** table.

By the end of today's assignment, you will learn how to:

- Build time-series analytical datasets
- Calculate monthly business KPIs
- Analyse business growth
- Create cumulative metrics
- Calculate Moving Averages
- Apply advanced Window Functions
- Build executive-ready reporting datasets

---

# 🏢 Business Scenario

The Executive Team reviews monthly business performance before planning future strategies.

Typical business questions include:

- Is monthly revenue increasing?
- Which month had the highest sales?
- How fast is customer acquisition growing?
- Are orders increasing every month?
- Is average order value improving?
- Are there seasonal sales patterns?

Currently, these reports are manually created every month.

Your responsibility is to automate this analysis by building a reusable **Monthly Sales Trend Analytics** Gold table.

---

# 📂 Source Tables

```
gold.sales_summary

gold.customer_analytics

gold.executive_business_kpis
```

---

# 🏗 Target Table

```
gold.monthly_sales_trend
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

✅ Monthly metrics calculated

✅ Revenue trends generated

✅ Growth percentages calculated

✅ Moving averages created

✅ Cumulative totals generated

✅ Gold Delta table created

✅ Validation report completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-309_Create_Monthly_Sales_Trend
```

---

## Task 2

Read the following tables.

```
gold.sales_summary

gold.customer_analytics

gold.executive_business_kpis
```

---

## Task 3

Create a monthly aggregated dataset.

Group data by

```
Year

Month
```

Calculate:

- Total Revenue
- Total Orders
- Total Customers
- Total Products Sold
- Average Order Value
- Average Freight Cost

---

## Task 4

Create monthly KPIs.

Generate the following columns.

```
year

month

monthly_revenue

monthly_orders

monthly_customers

monthly_products_sold

average_order_value

average_freight_cost
```

---

## Task 5

Calculate business growth metrics.

Examples:

- Month-over-Month Revenue Growth
- Month-over-Month Order Growth
- Month-over-Month Customer Growth
- Month-over-Month Product Growth

Use

```
LAG()
```

to compare the current month with the previous month.

---

## Task 6

Create cumulative business metrics.

Calculate:

- Running Revenue
- Running Orders
- Running Customers

Use

```
SUM()

OVER()
```

with Window Functions.

---

## Task 7

Calculate Moving Averages.

Examples:

- 3-Month Revenue Moving Average
- 3-Month Order Moving Average
- 3-Month Customer Moving Average

Use Window Frames to calculate rolling averages.

---

## Task 8

Identify business trends.

Create columns such as:

```
Revenue Trend

Order Trend

Customer Trend
```

Example values:

```
Increasing

Stable

Declining
```

Define logical business rules.

---

## Task 9

Apply Window Functions.

Use:

```
LAG()

LEAD()

ROW_NUMBER()

RANK()

DENSE_RANK()

SUM()

AVG()
```

Generate rankings for:

- Best Revenue Month
- Best Order Month
- Highest Customer Growth Month

---

## Task 10

Perform business validation.

Verify:

- Monthly Revenue matches Sales Summary.
- Revenue Growth calculations are accurate.
- Running Totals are correct.
- No duplicate monthly records exist.

Document any discrepancies.

---

## Task 11

Write the DataFrame as

```
gold.monthly_sales_trend
```

using Delta format.

---

## Task 12

Validate the Gold table.

Verify:

- Record Count
- Duplicate Months
- NULL Values
- Revenue Accuracy
- Growth Accuracy
- Moving Average Accuracy

---

## Task 13 ⭐

Create a Monthly Sales Trend Validation Report.

Include:

- Source Tables
- Monthly Record Count
- Revenue Validation
- Growth Validation
- Running Total Validation
- Moving Average Validation
- Data Quality Checks
- Business Rules Applied

---

# 📚 Concepts Covered

- Time-Series Analytics
- Moving Average
- Running Total
- Month-over-Month Growth
- Window Functions
- Rolling Aggregations
- Executive Reporting
- Gold Layer Design

---

# 💡 Mini Challenge

Answer the following using Spark SQL.

1. Which month generated the highest revenue?

2. Which month had the highest customer growth?

3. Calculate Month-over-Month Revenue Growth.

4. Calculate a 3-month Moving Average of revenue.

5. Calculate cumulative revenue.

6. Find the month with the highest average order value.

7. Which month sold the most products?

8. Calculate cumulative customer growth.

9. Which months had declining revenue?

10. Build a monthly executive summary using a single SQL query.

---

# 🧠 Real Interview Questions

### Q1

What is Month-over-Month (MoM) Growth?

---

### Q2

What is the difference between a Running Total and a Moving Average?

---

### Q3

How do Window Frames work in Spark SQL?

---

### Q4

When would you use `LAG()` instead of a self-join?

---

### Q5

How would you validate that your monthly revenue calculations are correct?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Monthly Sales Trend Notebook Created

✓ Monthly KPIs Calculated

✓ Revenue Growth Calculated

✓ Running Totals Generated

✓ Moving Averages Calculated

✓ Trend Analysis Completed

✓ Gold Monthly Sales Trend Table Created

✓ Validation Report Generated

✓ Business Metrics Verified
```

---

# 🏁 End Goal

At the end of Day 27, your Lakehouse will contain:

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
├── regional_sales
├── executive_business_kpis
├── customer_cohort_retention
└── monthly_sales_trend
```

You have successfully built a **Monthly Sales Trend Analytics** table that enables executives to monitor revenue growth, customer acquisition, seasonal patterns, and long-term business performance using a trusted time-series dataset.

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
| Sprint 3 | OLIST-306 | Create Gold Regional Sales | ✅ Complete |
| Sprint 3 | OLIST-307 | Create Executive Business KPIs | ✅ Complete |
| Sprint 3 | OLIST-308 | Create Customer Cohort & Retention Analytics | ✅ Complete |
| **Sprint 3** | **OLIST-309** | **Create Monthly Sales Trend Analytics** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 28)

## 🚀 JIRA ID: OLIST-310

Build the **Sales Forecast Preparation** Gold table by engineering time-series features for future forecasting. You'll create lag features, rolling statistics, seasonal indicators, holiday flags, and trend variables that prepare historical sales data for machine learning forecasting models while learning feature engineering techniques commonly used in real-world Data Engineering and Data Science projects.
