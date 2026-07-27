# Day 28 — Sprint 3

# 🚀 JIRA ID: OLIST-310

## Epic

**Build Gold Layer**

---

# 📖 User Story

**As a Data Scientist,**

I want a Sales Forecast Preparation table,

so that I can train machine learning models to accurately predict future sales, demand, and revenue trends.

---

# 🎯 Objective

Today you will build a **Gold Sales Forecast Preparation** table.

By the end of today's assignment, you will learn how to:

- Engineer time-series features
- Create lag features
- Build rolling statistics
- Generate calendar features
- Prepare ML-ready datasets
- Apply advanced Window Functions
- Build production-ready feature tables

---

# 🏢 Business Scenario

The Data Science team is planning to build a sales forecasting model.

However, raw transactional data cannot be directly used for Machine Learning.

The historical sales data must first be transformed into an ML-ready feature table containing trend, seasonality, and lag-based features.

Your responsibility is to build the **Sales Forecast Preparation** Gold table that will become the input dataset for forecasting models.

---

# 📂 Source Tables

```
gold.monthly_sales_trend

gold.sales_summary
```

---

# 🏗 Target Table

```
gold.sales_forecast_features
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

✅ Monthly sales data read successfully

✅ Calendar features created

✅ Lag features generated

✅ Rolling statistics calculated

✅ Forecast feature table created

✅ Gold Delta table created

✅ Validation report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-310_Create_Sales_Forecast_Features
```

---

## Task 2

Read the following tables.

```
gold.monthly_sales_trend

gold.sales_summary
```

---

## Task 3

Create a monthly feature dataset.

Generate one record per month containing:

```
year

month

monthly_revenue

monthly_orders

monthly_customers
```

Sort the dataset chronologically.

---

## Task 4

Create calendar features.

Generate:

```
year

quarter

month

month_name

week_of_year

day_of_year

is_weekend

is_month_end

is_quarter_end

is_year_end
```

Document why each feature can help forecasting models.

---

## Task 5

Create Lag Features.

Generate:

```
Revenue_Last_Month

Revenue_2_Months_Ago

Revenue_3_Months_Ago

Orders_Last_Month

Customers_Last_Month
```

Use:

```
LAG()
```

---

## Task 6

Create Rolling Statistics.

Examples:

```
3-Month Average Revenue

6-Month Average Revenue

3-Month Average Orders

Rolling Maximum Revenue

Rolling Minimum Revenue

Rolling Standard Deviation
```

Use Window Frames.

---

## Task 7

Create Growth Features.

Generate:

```
Revenue Growth %

Order Growth %

Customer Growth %

Running Revenue

Running Orders
```

Use:

```
LAG()

SUM()

OVER()
```

---

## Task 8

Create Trend Indicators.

Examples:

```
Revenue Trend

Order Trend

Growth Direction

Seasonality Indicator

Sales Momentum
```

Define business rules for each indicator.

---

## Task 9

Perform feature validation.

Verify:

- No duplicate months exist.
- Lag features align with previous months.
- Rolling averages are correctly calculated.
- Growth percentages are mathematically correct.
- No unexpected NULL values exist beyond the first lag periods.

Document all findings.

---

## Task 10

Write the DataFrame as

```
gold.sales_forecast_features
```

using Delta format.

---

## Task 11

Validate the Gold table.

Verify:

- Record Count
- Duplicate Months
- NULL Values
- Lag Feature Accuracy
- Rolling Average Accuracy
- Growth Calculations

---

## Task 12 ⭐

Create a Forecast Feature Validation Report.

Include:

- Source Tables
- Feature Count
- Lag Feature Validation
- Rolling Statistics Validation
- Growth Validation
- Data Quality Checks
- Business Rules Applied

---

# 📚 Concepts Covered

- Feature Engineering
- Time-Series Features
- Lag Features
- Rolling Windows
- Calendar Features
- Window Functions
- Machine Learning Data Preparation
- Gold Layer Design

---

# 💡 Mini Challenge

Answer the following using Spark SQL.

1. Calculate the previous month's revenue using `LAG()`.

2. Calculate the 3-month moving average of revenue.

3. Calculate cumulative revenue.

4. Find the highest rolling 3-month revenue.

5. Identify months with negative revenue growth.

6. Calculate Quarter-wise revenue.

7. Calculate Year-wise revenue.

8. Identify the fastest-growing quarter.

9. Calculate average monthly order growth.

10. Produce an ML-ready feature table using a single SQL query.

---

# 🧠 Real Interview Questions

### Q1

What is Feature Engineering?

---

### Q2

Why are Lag Features useful for forecasting?

---

### Q3

What is the difference between a Lag Feature and a Moving Average?

---

### Q4

Why do Machine Learning models require engineered features instead of raw transactional data?

---

### Q5

How would you validate that rolling statistics have been calculated correctly?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Sales Forecast Notebook Created

✓ Calendar Features Generated

✓ Lag Features Created

✓ Rolling Statistics Calculated

✓ Growth Features Generated

✓ Trend Indicators Created

✓ Gold Sales Forecast Feature Table Created

✓ Validation Report Generated

✓ ML-Ready Dataset Prepared
```

---

# 🏁 End Goal

At the end of Day 28, your Lakehouse will contain:

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
├── monthly_sales_trend
└── sales_forecast_features
```

You have successfully built a **Sales Forecast Preparation** table that transforms historical sales data into a machine learning-ready feature set, enabling accurate forecasting, demand planning, and predictive analytics.

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
| Sprint 3 | OLIST-309 | Create Monthly Sales Trend Analytics | ✅ Complete |
| **Sprint 3** | **OLIST-310** | **Create Sales Forecast Features** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 29)

## 🚀 JIRA ID: OLIST-311

Build the **Power BI Star Schema Data Mart** by designing Fact and Dimension tables from the Gold layer. You'll learn dimensional modelling, surrogate keys, slowly changing dimensions, fact vs. dimension design, and create a reporting-ready semantic model optimized for Power BI, Tableau, and enterprise BI platforms.
