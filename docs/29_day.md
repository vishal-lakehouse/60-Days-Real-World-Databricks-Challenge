# Day 29 — Sprint 4

# 🚀 JIRA ID: OLIST-401

## Epic

**Build Reporting Data Mart**

---

# 📖 User Story

**As a Power BI Developer,**

I want a reporting-ready Star Schema,

so that dashboards load quickly, relationships are easy to maintain, and business users can analyse data efficiently.

---

# 🎯 Objective

Today you will design and build a **Power BI Star Schema Data Mart** from the Gold layer.

By the end of today's assignment, you will learn how to:

- Design a Star Schema
- Create Fact and Dimension tables
- Generate Surrogate Keys
- Design reporting models
- Optimize BI datasets
- Build enterprise-ready semantic models
- Validate dimensional models

---

# 🏢 Business Scenario

The Analytics Team is preparing executive dashboards in Power BI.

Using a single large table for reporting creates several problems:

- Slow dashboard performance
- Duplicate data
- Difficult maintenance
- Poor scalability

To solve these issues, the team has decided to implement a **Star Schema**.

Your responsibility is to build a reporting-ready dimensional model that will become the foundation for all BI dashboards.

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

# 🏗 Target Tables

```
gold.fact_sales

gold.dim_customer

gold.dim_product

gold.dim_seller

gold.dim_category

gold.dim_region

gold.dim_date
```

---

# 🛠 Technologies

- Azure Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Power BI
- Dimensional Modeling

---

# 📋 Acceptance Criteria

✅ Star Schema designed

✅ Fact table created

✅ Dimension tables created

✅ Surrogate Keys generated

✅ Business relationships validated

✅ Gold Delta tables created

✅ Validation report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-401_Create_Star_Schema
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

Design the Star Schema.

Draw the relationship between:

```
Fact Sales

↓

Customer

Product

Seller

Category

Region

Date
```

Document your design inside the notebook.

---

## Task 4

Create the **Fact Sales** table.

Include measures such as:

```
Sales Key

Customer Key

Product Key

Seller Key

Category Key

Region Key

Date Key

Order ID

Revenue

Freight

Quantity

Order Value
```

---

## Task 5

Create the **Customer Dimension**.

Include:

```
Customer Key

Customer ID

City

State

Customer Segment

First Purchase

Last Purchase
```

Generate a surrogate key.

---

## Task 6

Create the **Product Dimension**.

Include:

```
Product Key

Product ID

Category

Average Price

Average Review Score

Performance Category
```

Generate a surrogate key.

---

## Task 7

Create the **Seller Dimension**.

Include:

```
Seller Key

Seller ID

City

State

Performance Category
```

Generate a surrogate key.

---

## Task 8

Create the remaining dimensions.

### Category

```
Category Key

Category Name

Revenue Category
```

### Region

```
Region Key

State

City

Region Tier
```

### Date

Generate a complete Date Dimension containing:

```
Date Key

Date

Day

Week

Month

Quarter

Year

Day Name

Month Name

Weekend Flag

Month End Flag

Quarter End Flag
```

---

## Task 9

Validate relationships.

Verify:

- Every Fact record has matching Dimension records.
- No orphan keys exist.
- Surrogate Keys are unique.
- Duplicate Dimension records are removed.

Use:

```
LEFT ANTI JOIN
```

to identify missing relationships.

---

## Task 10

Write all Fact and Dimension tables as Delta tables.

```
gold.fact_sales

gold.dim_customer

gold.dim_product

gold.dim_seller

gold.dim_category

gold.dim_region

gold.dim_date
```

---

## Task 11

Validate the Star Schema.

Verify:

- Record Counts
- Duplicate Keys
- NULL Foreign Keys
- Relationship Integrity
- Fact Table Accuracy

---

## Task 12 ⭐

Create a Star Schema Validation Report.

Include:

- Source Tables
- Fact Record Count
- Dimension Record Counts
- Relationship Validation
- Surrogate Key Validation
- Data Quality Checks
- Business Rules Applied

---

# 📚 Concepts Covered

- Star Schema
- Fact Tables
- Dimension Tables
- Surrogate Keys
- Primary Keys
- Foreign Keys
- Dimensional Modeling
- Power BI Data Modeling
- Delta Lake

---

# 💡 Mini Challenge

Answer the following using Spark SQL.

1. How many Dimension tables were created?

2. How many records exist in the Fact table?

3. Identify orphan Customer Keys.

4. Identify orphan Product Keys.

5. Count distinct Sellers.

6. Count distinct Categories.

7. Count distinct Regions.

8. Count distinct Dates.

9. Find the largest Dimension table.

10. Verify that every Fact record has matching Dimension records.

---

# 🧠 Real Interview Questions

### Q1

What is a Star Schema?

---

### Q2

What is the difference between a Fact table and a Dimension table?

---

### Q3

Why are Surrogate Keys used instead of business keys?

---

### Q4

What problems occur if a Fact table contains orphan foreign keys?

---

### Q5

Why is a Star Schema preferred for Power BI and Tableau?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Star Schema Notebook Created

✓ Fact Sales Table Created

✓ Customer Dimension Created

✓ Product Dimension Created

✓ Seller Dimension Created

✓ Category Dimension Created

✓ Region Dimension Created

✓ Date Dimension Created

✓ Relationship Validation Completed

✓ Star Schema Validation Report Generated
```

---

# 🏁 End Goal

At the end of Day 29, your Lakehouse will contain:

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
├── sales_forecast_features
├── fact_sales
├── dim_customer
├── dim_product
├── dim_seller
├── dim_category
├── dim_region
└── dim_date
```

You have successfully built an enterprise-ready **Star Schema Data Mart** that serves as the foundation for Power BI, Tableau, Excel, and other BI tools. The model is optimized for fast reporting, scalable analytics, and simplified business queries.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| Sprint 3 | OLIST-301 → OLIST-310 | Gold Analytics Layer | ✅ Complete |
| **Sprint 4** | **OLIST-401** | **Build Power BI Star Schema Data Mart** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 30)

## 🚀 JIRA ID: OLIST-402

Build the **Power BI Executive Dashboard** by connecting the Star Schema Data Mart to Power BI Desktop. You'll create relationships, DAX measures, KPI cards, slicers, drill-through pages, interactive visualizations, and executive dashboards that answer real business questions using the data warehouse you've built over the last 29 days.
