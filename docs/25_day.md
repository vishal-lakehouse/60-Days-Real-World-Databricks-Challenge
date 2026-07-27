# Day 25 — Sprint 3

# 🚀 JIRA ID: OLIST-307

## Epic

**Build Gold Layer**

---

# 📖 User Story

**As a Chief Executive Officer (CEO),**

I want an Executive Business KPI Dashboard dataset,

so that I can monitor the overall health of the business from a single dashboard without analysing multiple reports.

---

# 🎯 Objective

Today you will build the **Executive Business KPI Dashboard** table.

By the end of today's assignment, you will learn how to:

- Build an executive-level Gold table
- Combine multiple Gold datasets
- Calculate executive KPIs
- Perform time-based aggregations
- Measure business growth
- Create dashboard-ready datasets
- Validate business metrics

---

# 🏢 Business Scenario

Every morning, the executive leadership team reviews a business dashboard before making strategic decisions.

Instead of analysing hundreds of reports, they want a single dataset containing the most important business KPIs.

Typical questions include:

- How much revenue did we generate?
- How many orders were placed?
- How many active customers do we have?
- Which sellers are performing best?
- Which product categories generate the highest revenue?
- Which states contribute the most revenue?
- Is business growing month over month?

Your responsibility is to build an executive-ready Gold table that powers the company's Power BI dashboard.

---

# 📂 Source Tables

```
gold.sales_summary

gold.customer_analytics

gold.seller_performance

gold.product_performance

gold.category_performance

gold.regional_sales
```

---

# 🏗 Target Table

```
gold.executive_business_kpis
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

✅ All Gold tables read successfully

✅ Executive KPIs calculated

✅ Monthly metrics generated

✅ Growth metrics calculated

✅ Dashboard-ready dataset created

✅ Gold Delta table created

✅ Validation report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-307_Create_Executive_Business_KPIs
```

---

## Task 2

Read the following Gold tables.

```
gold.sales_summary

gold.customer_analytics

gold.seller_performance

gold.product_performance

gold.category_performance

gold.regional_sales
```

---

## Task 3

Create executive KPIs.

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

Generate monthly business metrics.

Group by:

```
Year

Month
```

Calculate:

- Monthly Revenue
- Monthly Orders
- Monthly Customers
- Monthly Average Order Value

---

## Task 5

Calculate executive growth metrics.

Examples:

- Month-over-Month (MoM) Revenue Growth
- Month-over-Month Order Growth
- Customer Growth
- Seller Growth
- Average Order Value Growth

Use Window Functions such as:

```
LAG()

LEAD()
```

Calculate the growth percentage for each month.

---

## Task 6

Identify business leaders.

Determine:

- Top Revenue State
- Top Revenue City
- Top Seller
- Top Customer
- Top Product
- Top Product Category

Store these values in the executive dataset.

---

## Task 7

Create executive scorecards.

Examples:

```
Revenue Status

Customer Growth Status

Sales Trend

Business Health Score
```

Define business rules for each score.

---

## Task 8

Perform business validation.

Verify:

- Revenue matches Sales Summary.
- Customer count matches Customer Analytics.
- Seller count matches Seller Performance.
- Product count matches Product Performance.
- Regional revenue matches Regional Sales.

Document any discrepancies.

---

## Task 9

Write the DataFrame as

```
gold.executive_business_kpis
```

using Delta format.

---

## Task 10

Validate the Gold table.

Verify:

- Record Count
- Duplicate Records
- NULL Values
- KPI Accuracy
- Growth Calculations

---

## Task 11 ⭐

Create an Executive KPI Validation Report.

Include:

- Source Tables
- KPI Validation
- Revenue Validation
- Growth Validation
- Dashboard Readiness
- Data Quality Checks
- Business Rules Applied

---

# 📚 Concepts Covered

- Executive Dashboards
- Business KPIs
- Window Functions
- Time-Series Analysis
- Growth Analytics
- Dashboard Design
- Gold Layer
- Delta Lake

---

# 💡 Mini Challenge

Answer the following using Spark SQL.

1. Total Revenue by Month

2. Month-over-Month Revenue Growth

3. Total Orders by Month

4. Average Order Value by Month

5. Best Revenue Month

6. Worst Revenue Month

7. Top 5 States by Revenue

8. Top 5 Product Categories by Revenue

9. Top 10 Sellers by Revenue

10. Executive KPI Summary (single query)

---

# 🧠 Real Interview Questions

### Q1

Why do executive dashboards use Gold tables instead of Silver tables?

---

### Q2

What is Month-over-Month (MoM) growth?

---

### Q3

How would you calculate revenue growth using the `LAG()` function?

---

### Q4

How would you validate that executive KPIs are accurate?

---

### Q5

Why is it beneficial to pre-compute dashboard KPIs instead of calculating them in Power BI?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Executive KPI Notebook Created

✓ Executive KPIs Calculated

✓ Monthly Metrics Generated

✓ Growth Metrics Calculated

✓ Business Leaders Identified

✓ Executive Scorecards Created

✓ Gold Executive KPI Table Created

✓ Validation Report Generated

✓ Dashboard-Ready Dataset Prepared
```

---

# 🏁 End Goal

At the end of Day 25, your Lakehouse will contain:

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
└── executive_business_kpis
```

You have successfully built an **Executive Business KPI Dashboard** dataset that provides leadership with a centralized, trusted source for monitoring business performance, revenue trends, customer growth, operational health, and strategic decision-making.

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
| **Sprint 3** | **OLIST-307** | **Create Executive Business KPIs** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 26)

## 🚀 JIRA ID: OLIST-308

Build the **Customer Cohort & Retention Analytics** Gold table by analysing customer acquisition, repeat purchases, monthly cohorts, retention rates, and churn trends. You'll learn cohort analysis, advanced window functions, time-based analytics, and create one of the most frequently asked business reports in Data Engineering and Analytics interviews.
