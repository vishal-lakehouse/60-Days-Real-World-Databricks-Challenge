# Day 14 — Sprint 2

# 🚀 JIRA ID: OLIST-205

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Sellers** dataset from the Bronze layer into the Silver layer,

so that downstream applications can use clean, standardized, and trusted seller master data for analytics and reporting.

---

# 🎯 Objective

Today you will transform the **Sellers** dataset into a trusted Silver Delta table.

By the end of today's assignment, you will learn how to:

- Read Delta tables
- Validate seller master data
- Remove duplicate records
- Standardize location information
- Validate business rules
- Generate a Data Quality Report
- Compare Bronze vs Silver datasets

---

# 🏢 Business Scenario

The Olist marketplace consists of thousands of independent sellers located across Brazil.

Before seller information is consumed by reporting systems and business users, it must be validated and standardized.

As a Data Engineer, your responsibility is to build a trusted **Silver Sellers** table that will later support supplier performance dashboards and regional analytics.

---

# 📂 Source Table

```
bronze.sellers
```

---

# 🏗 Target Table

```
silver.sellers
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

✅ Bronze Sellers table read successfully

✅ Duplicate Seller IDs removed

✅ NULL values analysed

✅ Seller location standardized

✅ ZIP code validated

✅ Silver Delta table created

✅ Bronze vs Silver comparison completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-205_Transform_Sellers_Silver
```

---

## Task 2

Read

```
bronze.sellers
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Review the following columns:

```
seller_id

seller_zip_code_prefix

seller_city

seller_state
```

---

## Task 4

Count total records.

Compare the result with the Bronze table.

---

## Task 5

Validate Seller IDs.

Check for duplicate

```
seller_id
```

Remove duplicates if found.

---

## Task 6

Analyse NULL values.

Check every column.

Document your observations.

---

## Task 7

Validate business rules.

Examples:

- Seller ID should never be NULL.
- ZIP code prefix should be numeric.
- City name should not contain leading or trailing spaces.
- State code should contain only valid Brazilian state abbreviations.

Identify records that violate these rules.

---

## Task 8

Standardize seller information.

Examples:

- Trim whitespace.
- Convert city names to Proper Case.
- Convert state codes to uppercase.
- Ensure ZIP code prefix uses the correct data type.

Do not change the business meaning of the data.

---

## Task 9

Validate relationship with Geolocation.

Verify whether every seller ZIP code exists in:

```
bronze.geolocation
```

Identify seller records without matching ZIP code prefixes.

Use:

```
LEFT ANTI JOIN
```

---

## Task 10

Write the transformed DataFrame as

```
silver.sellers
```

using Delta format.

---

## Task 11

Validate the Silver table.

Compare:

- Bronze record count
- Silver record count
- Duplicate records removed
- Invalid records identified

---

## Task 12 ⭐

Create a Seller Data Quality Report.

Include:

- Bronze Record Count
- Silver Record Count
- Duplicate Sellers Removed
- NULL Values Found
- Invalid ZIP Codes
- Invalid State Codes
- Missing Geolocation Matches
- Transformations Applied

---

# 📚 Concepts Covered

- Master Data Management
- Data Standardization
- Data Quality Validation
- Reference Data Validation
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many unique sellers exist?

2. Which state has the highest number of sellers?

3. Which city has the highest number of sellers?

4. How many sellers do not have matching geolocation records?

5. How many distinct ZIP code prefixes exist?

---

# 🧠 Real Interview Questions

### Q1

Why is the Sellers table considered master data?

---

### Q2

Why should city and state values be standardized?

---

### Q3

Why is Geolocation used to validate seller information?

---

### Q4

How would you identify sellers with invalid ZIP codes?

---

### Q5

Why should duplicate seller records be removed in the Silver layer instead of the Bronze layer?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Sellers Notebook Created

✓ Bronze Sellers Table Read Successfully

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Business Rule Validation Completed

✓ Geolocation Validation Completed

✓ Seller Information Standardized

✓ Silver Sellers Table Created

✓ Seller Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 14, your Lakehouse will contain:

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
└── sellers
```

You now have trusted seller master data that can be used for supplier performance analysis, regional sales reporting, and downstream business intelligence.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 | Transform Customers | ✅ Complete |
| Sprint 2 | OLIST-202 | Transform Orders | ✅ Complete |
| Sprint 2 | OLIST-203 | Transform Order Items | ✅ Complete |
| Sprint 2 | OLIST-204 | Transform Products | ✅ Complete |
| **Sprint 2** | **OLIST-205** | **Transform Sellers** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 15)

## 🚀 JIRA ID: OLIST-206

Transform the **Order Payments** dataset from the Bronze layer into the Silver layer by validating payment records, analysing payment methods, checking instalment values, enforcing business rules, and preparing trusted payment data for financial analytics.
