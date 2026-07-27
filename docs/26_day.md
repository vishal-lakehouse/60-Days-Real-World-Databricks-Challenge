# Day 26 — Sprint 3

# 🚀 JIRA ID: OLIST-308

## Epic

**Build Gold Layer**

---

# 📖 User Story

**As a Marketing Manager,**

I want a Customer Cohort & Retention Analytics table,

so that I can understand customer acquisition, retention, repeat purchase behaviour, and churn trends to improve customer loyalty and business growth.

---

# 🎯 Objective

Today you will build a **Gold Customer Cohort & Retention Analytics** table.

By the end of today's assignment, you will learn how to:

- Perform Cohort Analysis
- Build Retention Reports
- Calculate Customer Churn
- Use Date Functions
- Apply Advanced Window Functions
- Build Time-Series Analytics
- Create Executive Business Reports

---

# 🏢 Business Scenario

The Marketing Team wants to understand how well the company retains customers.

They frequently ask questions like:

- How many customers return after their first purchase?
- Which month's customers are the most loyal?
- What is our monthly retention rate?
- Which customer cohorts generate the highest revenue?
- How many customers never return?

Instead of calculating these metrics every month, they want a reusable Gold table.

Your responsibility is to build a **Customer Cohort & Retention Analytics** dataset for business reporting.

---

# 📂 Source Tables

```
gold.customer_analytics

gold.sales_summary

silver.orders
```

---

# 🏗 Target Table

```
gold.customer_cohort_retention
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

✅ Customer acquisition month identified

✅ Cohorts created

✅ Monthly retention calculated

✅ Repeat customers identified

✅ Churn metrics calculated

✅ Gold Delta table created

✅ Validation report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-308_Create_Customer_Cohort_Retention
```

---

## Task 2

Read the following tables.

```
gold.customer_analytics

gold.sales_summary

silver.orders
```

---

## Task 3

Determine each customer's **First Purchase Date**.

Create:

```
first_purchase_date

cohort_month
```

Example:

```
Customer A

First Purchase

2018-01-12

Cohort

2018-01
```

---

## Task 4

Determine customer activity.

For every purchase calculate:

```
purchase_month

months_since_first_purchase
```

Example:

```
Month 0

Month 1

Month 2

Month 3
```

---

## Task 5

Build the Cohort Table.

For each cohort calculate:

- Total Customers
- Active Customers
- Repeat Customers

Group by

```
cohort_month

months_since_first_purchase
```

---

## Task 6

Calculate business KPIs.

Generate:

```
cohort_month

active_customers

retained_customers

retention_rate

repeat_purchase_rate

average_customer_revenue

average_orders_per_customer
```

---

## Task 7

Calculate churn metrics.

Examples:

- Churn Rate
- One-Time Customers
- Returning Customers
- Average Customer Lifetime
- Average Days Between Purchases

Document your calculation logic.

---

## Task 8

Apply Window Functions.

Use functions such as:

```
LAG()

LEAD()

ROW_NUMBER()

DENSE_RANK()
```

Examples:

- Previous Month Retention
- Cohort Ranking
- Retention Trend
- Revenue Trend

---

## Task 9

Create business classifications.

Example:

```
Highly Loyal Cohort

Healthy Cohort

Average Cohort

High Churn Cohort
```

Define business rules for each category.

---

## Task 10

Perform business validation.

Verify:

- Every customer belongs to exactly one cohort.
- Retention Rate is between **0%** and **100%**.
- Churn Rate is between **0%** and **100%**.
- Customer counts match Customer Analytics.

Document any discrepancies.

---

## Task 11

Write the DataFrame as

```
gold.customer_cohort_retention
```

using Delta format.

---

## Task 12

Validate the Gold table.

Verify:

- Record Count
- Duplicate Cohorts
- NULL Values
- Retention Accuracy
- Churn Accuracy

---

## Task 13 ⭐

Create a Customer Cohort Validation Report.

Include:

- Source Tables
- Cohort Count
- Retention Validation
- Churn Validation
- Revenue Validation
- Data Quality Checks
- Business Rules Applied

---

# 📚 Concepts Covered

- Cohort Analysis
- Customer Retention
- Customer Churn
- Time-Series Analytics
- Window Functions
- Customer Lifetime
- Business KPIs
- Gold Layer Design

---

# 💡 Mini Challenge

Answer the following using Spark SQL.

1. Which cohort has the highest retention after 3 months?

2. Which cohort generated the highest revenue?

3. Average retention rate across all cohorts

4. Number of one-time customers

5. Number of repeat customers

6. Average customer lifetime

7. Top 5 cohorts by revenue

8. Customers who placed more than 5 orders

9. Monthly customer acquisition trend

10. Monthly churn trend

---

# 🧠 Real Interview Questions

### Q1

What is Cohort Analysis?

---

### Q2

Why is Cohort Analysis more useful than simply counting monthly customers?

---

### Q3

How do you calculate Customer Retention Rate?

---

### Q4

How would you calculate Customer Churn Rate?

---

### Q5

How would you build a Cohort Table using Spark SQL?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Customer Cohort Notebook Created

✓ Customer Acquisition Month Calculated

✓ Cohort Table Created

✓ Retention Metrics Calculated

✓ Churn Metrics Calculated

✓ Window Functions Applied

✓ Business Classifications Created

✓ Gold Customer Cohort Table Created

✓ Validation Report Generated

✓ Business Metrics Verified
```

---

# 🏁 End Goal

At the end of Day 26, your Lakehouse will contain:

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
└── customer_cohort_retention
```

You have successfully built a **Customer Cohort & Retention Analytics** table that enables marketing and business teams to analyse customer acquisition, loyalty, retention, churn, and long-term customer behaviour using a single trusted dataset.

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
| **Sprint 3** | **OLIST-308** | **Create Customer Cohort & Retention Analytics** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 27)

## 🚀 JIRA ID: OLIST-309

Build the **Monthly Sales Trend Analytics** Gold table by analysing monthly revenue, order growth, customer growth, seasonal trends, and year-over-year performance. You'll learn advanced date transformations, rolling aggregations, moving averages, cumulative totals, and time-series analytics used in executive dashboards and forecasting.
