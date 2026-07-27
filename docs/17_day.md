# Day 17 — Sprint 2

# 🚀 JIRA ID: OLIST-208

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Geolocation** dataset from the Bronze layer into the Silver layer,

so that customer and seller location information is accurate, standardized, and ready for regional analytics.

---

# 🎯 Objective

Today you will transform the **Geolocation** dataset into a trusted Silver Delta table.

By the end of today's assignment, you will learn how to:

- Validate geographical reference data
- Standardize city and state names
- Validate latitude and longitude values
- Validate ZIP code prefixes
- Build production-quality ETL pipelines
- Generate a Data Quality Report

---

# 🏢 Business Scenario

The Geolocation dataset acts as a reference table for customer and seller locations.

Business teams use this information to answer questions like:

- Which states generate the highest revenue?
- Which cities have the most customers?
- Where are the top-performing sellers located?

Before this data can be trusted, it must be validated and standardized.

Your responsibility is to build a trusted **Silver Geolocation** table.

---

# 📂 Source Table

```
bronze.geolocation
```

---

# 🏗 Target Table

```
silver.geolocation
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

✅ Bronze Geolocation table read successfully

✅ Duplicate records analysed

✅ ZIP code prefixes validated

✅ Latitude and Longitude validated

✅ City and State standardized

✅ NULL values analysed

✅ Silver Delta table created

✅ Data Quality Report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-208_Transform_Geolocation_Silver
```

---

## Task 2

Read

```
bronze.geolocation
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Review the following columns:

```
geolocation_zip_code_prefix

geolocation_lat

geolocation_lng

geolocation_city

geolocation_state
```

---

## Task 4

Count total records.

Compare the result with the Bronze table.

---

## Task 5

Analyse duplicate records.

Questions:

- How many duplicate rows exist?
- How many duplicate ZIP code prefixes exist?
- Should duplicate ZIP prefixes always be removed?

Document your findings before making any changes.

---

## Task 6

Analyse NULL values.

Check every column.

Document all observations.

---

## Task 7

Validate business rules.

Examples:

- ZIP code prefix should not be NULL.
- Latitude must be between **-90** and **90**.
- Longitude must be between **-180** and **180**.
- State code should contain valid Brazilian state abbreviations.

Identify all records violating these rules.

---

## Task 8

Standardize geographical information.

Examples:

- Trim whitespace.
- Convert city names to Proper Case.
- Convert state codes to uppercase.
- Ensure latitude and longitude use the correct numeric data types.

Do not modify the actual coordinates.

---

## Task 9

Validate relationships.

Check whether every ZIP code used in:

```
silver.customers

silver.sellers
```

has a matching record in

```
silver.geolocation
```

Use:

```
LEFT ANTI JOIN
```

to identify missing reference records.

---

## Task 10

Write the transformed DataFrame as

```
silver.geolocation
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

Create a Geolocation Data Quality Report.

Include:

- Bronze Record Count
- Silver Record Count
- Duplicate Records Removed
- NULL Values Found
- Invalid Latitude Records
- Invalid Longitude Records
- Invalid State Codes
- Missing Customer ZIP Matches
- Missing Seller ZIP Matches
- Transformations Applied

---

# 📚 Concepts Covered

- Reference Data
- Geographic Data Validation
- Coordinate Validation
- Data Standardization
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many unique ZIP code prefixes exist?

2. Which state has the highest number of ZIP code prefixes?

3. Which city appears most frequently?

4. Are there any invalid latitude or longitude values?

5. How many customer ZIP code prefixes have no matching geolocation record?

---

# 🧠 Real Interview Questions

### Q1

Why is the Geolocation dataset considered reference data?

---

### Q2

Why shouldn't latitude and longitude values be modified during standardization?

---

### Q3

How would you validate whether coordinates are valid?

---

### Q4

Why is geolocation important for business analytics?

---

### Q5

How would you identify customers whose ZIP code does not exist in the Geolocation table?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Geolocation Notebook Created

✓ Bronze Geolocation Table Read Successfully

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Coordinate Validation Completed

✓ Business Rule Validation Completed

✓ Customer & Seller ZIP Validation Completed

✓ Silver Geolocation Table Created

✓ Geolocation Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 17, your Lakehouse will contain:

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
└── geolocation
```

You now have trusted geographical reference data that can be used to enrich customer, seller, logistics, and regional sales analytics.

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
| Sprint 2 | OLIST-206 | Transform Order Payments | ✅ Complete |
| Sprint 2 | OLIST-207 | Transform Order Reviews | ✅ Complete |
| **Sprint 2** | **OLIST-208** | **Transform Geolocation** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 18)

## 🚀 JIRA ID: OLIST-209

Transform the **Product Category Translation** dataset from the Bronze layer into the Silver layer by validating category mappings, standardizing category names, identifying missing translations, and creating a trusted lookup table that will support product analytics in the Gold layer.
