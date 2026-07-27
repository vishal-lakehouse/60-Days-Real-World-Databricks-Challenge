# Day 30 — Sprint 4

# 🚀 JIRA ID: OLIST-402

## Epic

**Build Business Intelligence Dashboard**

---

# 📖 User Story

**As a CEO,**

I want an interactive Executive Dashboard,

so that I can monitor the company's performance in real time and make data-driven business decisions without writing SQL queries.

---

# 🎯 Objective

Today you will connect your **Star Schema Data Mart** to **Power BI** and build an executive dashboard.

By the end of today's assignment, you will learn how to:

- Connect Power BI to Databricks
- Import Fact & Dimension tables
- Create a Star Schema Model
- Build DAX Measures
- Design Executive Dashboards
- Build Interactive Reports
- Optimize Dashboard Performance

---

# 🏢 Business Scenario

The Executive Leadership Team needs a single dashboard that answers the most important business questions.

Instead of opening multiple reports, they want one interactive dashboard containing:

- Revenue
- Orders
- Customers
- Sellers
- Products
- Categories
- Regional Performance
- Monthly Growth

Your responsibility is to build an enterprise-ready Power BI Dashboard using the Star Schema created yesterday.

---

# 📂 Source Tables

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

# 🏗 Deliverables

```
Power BI Dashboard (.pbix)

Dashboard Screenshots

Dashboard Documentation
```

---

# 🛠 Technologies

- Azure Databricks
- Delta Lake
- Power BI Desktop
- Power Query
- DAX
- Star Schema
- Power BI Service (Optional)

---

# 📋 Acceptance Criteria

✅ Connect Power BI to Databricks

✅ Import Fact & Dimension Tables

✅ Build Star Schema Relationships

✅ Create DAX Measures

✅ Design Executive Dashboard

✅ Validate Dashboard Metrics

✅ Dashboard Performance Optimized

---

# 🧑‍💻 Tasks

## Task 1

Install **Power BI Desktop** (if not already installed).

---

## Task 2

Connect Power BI to your Databricks workspace.

Import:

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

## Task 3

Create the Star Schema Model.

Build relationships between:

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

Ensure:

- One-to-Many Relationships
- Single Direction Filtering
- No Circular Relationships

---

## Task 4

Create DAX Measures.

Examples:

```
Total Revenue

Total Orders

Average Order Value

Total Customers

Total Sellers

Total Products Sold

Average Review Score

Revenue Growth %

```

Validate each measure.

---

## Task 5

Create KPI Cards.

Examples:

```
💰 Total Revenue

📦 Total Orders

👥 Customers

🏪 Sellers

🛒 Products Sold

⭐ Average Rating

🚚 Average Freight Cost
```

---

## Task 6

Build Dashboard Visualizations.

Examples:

### Revenue Analysis

- Line Chart
- Area Chart
- Monthly Revenue Trend

---

### Customer Analysis

- Customer Growth
- Customer Distribution by State

---

### Product Analysis

- Top Products
- Category Revenue

---

### Seller Analysis

- Top Sellers
- Revenue by Seller

---

### Regional Analysis

- Revenue by State
- Revenue by City
- Filled Map

---

## Task 7

Add Interactive Filters.

Examples:

```
Year

Month

State

City

Category

Seller

Product
```

Use slicers to allow users to filter the dashboard.

---

## Task 8

Create Drill-through Pages.

Examples:

```
Customer Details

Seller Details

Product Details

Regional Details
```

Allow users to navigate from summary to detailed reports.

---

## Task 9

Optimize Dashboard Performance.

Examples:

- Hide unnecessary columns.
- Remove unused fields.
- Disable Auto Date/Time if not required.
- Use Star Schema relationships.
- Reduce unnecessary visuals.

Document all optimization steps.

---

## Task 10

Validate Dashboard.

Verify:

- Revenue matches Fact Table.
- Customer count matches Dimension.
- Seller count matches Dimension.
- Filters work correctly.
- DAX calculations are accurate.

---

## Task 11 ⭐

Create Dashboard Documentation.

Include:

- Dashboard Overview
- Data Sources
- Star Schema Diagram
- KPIs
- DAX Measures
- Dashboard Pages
- Filters
- Drill-through Pages
- Performance Optimizations

---

# 📚 Concepts Covered

- Power BI Desktop
- Power Query
- Star Schema
- DAX
- KPI Cards
- Slicers
- Drill-through
- Interactive Dashboards
- Dashboard Optimization

---

# 💡 Mini Challenge

Complete the following Power BI tasks.

1. Create a KPI Card showing Total Revenue.

2. Create a Line Chart showing Monthly Revenue.

3. Create a Filled Map showing Revenue by State.

4. Create a Bar Chart showing Top 10 Sellers.

5. Create a Pie Chart showing Revenue by Category.

6. Create a Matrix showing Revenue by State and Category.

7. Create a Drill-through Page for Seller Details.

8. Create a Revenue Growth KPI using DAX.

9. Add slicers for Year, State, and Category.

10. Publish the dashboard to Power BI Service (optional).

---

# 🧠 Real Interview Questions

### Q1

Why is a Star Schema recommended for Power BI?

---

### Q2

What is the difference between a Calculated Column and a Measure?

---

### Q3

Why are DAX Measures preferred over calculated fields in many reporting scenarios?

---

### Q4

How would you optimize a slow Power BI dashboard?

---

### Q5

What steps would you take to validate that dashboard KPIs match the underlying database?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Power BI Connected to Databricks

✓ Star Schema Imported

✓ Relationships Created

✓ DAX Measures Created

✓ KPI Cards Built

✓ Executive Dashboard Designed

✓ Interactive Filters Added

✓ Drill-through Pages Created

✓ Dashboard Performance Optimized

✓ Dashboard Documentation Completed
```

---

# 🏁 End Goal

At the end of Day 30, you will have completed the first production-ready Business Intelligence solution for the Olist Data Warehouse.

```
Azure Databricks
        │
        ▼
 Delta Lake Tables
        │
        ▼
 Star Schema Data Mart
        │
        ▼
 Power BI Desktop
        │
        ▼
 Executive Dashboard
```

Business users can now explore sales, customers, products, sellers, categories, and regional performance through a fully interactive dashboard without writing a single SQL query.

---

# 🎉 Sprint 4 Completed

## Sprint Goal

Build a reporting-ready Data Mart and create an interactive executive dashboard.

### Sprint Deliverables

```
✓ Star Schema Data Model Created

✓ Fact Table Created

✓ Dimension Tables Created

✓ Power BI Connected to Databricks

✓ Executive Dashboard Built

✓ DAX Measures Implemented

✓ Interactive Reports Designed

✓ Dashboard Documentation Completed
```

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| Sprint 3 | OLIST-301 → OLIST-310 | Gold Analytics Layer | ✅ Complete |
| Sprint 4 | OLIST-401 | Build Power BI Star Schema | ✅ Complete |
| **Sprint 4** | **OLIST-402** | **Build Executive Power BI Dashboard** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 31)

## 🚀 JIRA ID: OLIST-501

**Deploy the Complete Lakehouse Solution** by creating a production-ready Azure Databricks Workflow. You'll orchestrate Bronze, Silver, and Gold notebooks into a single automated pipeline, configure job clusters, task dependencies, retries, scheduling, failure notifications, and monitoring—just like a real enterprise Data Engineering project.
