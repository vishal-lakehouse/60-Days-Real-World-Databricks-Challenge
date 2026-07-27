# Day 16 — Sprint 2

# 🚀 JIRA ID: OLIST-207

## Epic

**Build Silver Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to transform the **Order Reviews** dataset from the Bronze layer into the Silver layer,

so that business users can analyze trusted customer feedback, ratings, and review trends.

---

# 🎯 Objective

Today you will transform the **Order Reviews** dataset into a trusted Silver Delta table.

By the end of today's assignment, you will learn how to:

- Validate review records
- Remove duplicate reviews
- Standardize review data
- Handle nullable review fields
- Validate relationships with Orders
- Build production-quality ETL pipelines
- Generate a Data Quality Report

---

# 🏢 Business Scenario

After an order is delivered, customers can leave a rating and optional written feedback.

These reviews help the business measure customer satisfaction and identify areas for improvement.

Before the data is used for dashboards and analytics, it must be validated and standardized.

Your responsibility is to build a trusted **Silver Order Reviews** table.

---

# 📂 Source Table

```
bronze.order_reviews
```

---

# 🏗 Target Table

```
silver.order_reviews
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

✅ Bronze Reviews table read successfully

✅ Duplicate Review IDs removed

✅ NULL values analysed

✅ Review scores validated

✅ Review timestamps validated

✅ Relationship with Orders validated

✅ Silver Delta table created

✅ Data Quality Report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-207_Transform_Order_Reviews_Silver
```

---

## Task 2

Read

```
bronze.order_reviews
```

into a Spark DataFrame.

---

## Task 3

Print the schema.

Review the following columns:

```
review_id

order_id

review_score

review_comment_title

review_comment_message

review_creation_date

review_answer_timestamp
```

---

## Task 4

Count total records.

Compare the result with the Bronze table.

---

## Task 5

Validate the Primary Key.

```
review_id
```

Remove duplicate Review IDs if found.

---

## Task 6

Analyse NULL values.

Pay special attention to:

```
review_comment_title

review_comment_message

review_answer_timestamp
```

Document whether the NULL values are expected.

---

## Task 7

Validate business rules.

Examples:

- Review Score should be between **1 and 5**.
- Review ID should never be NULL.
- Order ID should never be NULL.
- Review Creation Date should not be after Review Answer Timestamp (where applicable).

Identify all records violating these rules.

---

## Task 8

Standardize review data.

Examples:

- Trim leading and trailing spaces.
- Remove unnecessary whitespace.
- Ensure Review Score is stored as an integer.
- Standardize timestamp data types.

Do not modify customer comments or ratings.

---

## Task 9

Validate relationship with Orders.

Verify every review belongs to an existing order.

Identify orphan reviews using:

```
LEFT ANTI JOIN
```

---

## Task 10

Write the transformed DataFrame as

```
silver.order_reviews
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

Create a Review Data Quality Report.

Include:

- Bronze Record Count
- Silver Record Count
- Duplicate Reviews Removed
- NULL Values Found
- Invalid Review Scores
- Missing Order References
- Invalid Timestamp Records
- Transformations Applied

---

# 📚 Concepts Covered

- Customer Feedback Data
- Data Standardization
- Business Rule Validation
- Primary Key Validation
- Foreign Key Validation
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. What is the average review score?

2. How many reviews exist for each score (1–5)?

3. How many reviews have no written message?

4. How many reviews have both a title and a message?

5. Which review score is the least common?

---

# 🧠 Real Interview Questions

### Q1

Why should Review Scores be validated in the Silver layer?

---

### Q2

Why are review comments often NULL?

---

### Q3

How would you identify reviews that don't belong to any order?

---

### Q4

Why shouldn't customer comments be modified during transformation?

---

### Q5

How does customer review data help business decision-making?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Silver Order Reviews Notebook Created

✓ Bronze Reviews Table Read Successfully

✓ Primary Key Validated

✓ Duplicate Analysis Completed

✓ NULL Analysis Completed

✓ Business Rule Validation Completed

✓ Orders Relationship Validated

✓ Review Data Standardized

✓ Silver Order Reviews Table Created

✓ Review Data Quality Report Generated

✓ Bronze vs Silver Validation Completed
```

---

# 🏁 End Goal

At the end of Day 16, your Lakehouse will contain:

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
└── order_reviews
```

You now have a trusted customer feedback dataset ready for customer satisfaction analysis, review trend reporting, and future Gold-layer KPIs.

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
| **Sprint 2** | **OLIST-207** | **Transform Order Reviews** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 17)

## 🚀 JIRA ID: OLIST-208

Transform the **Geolocation** dataset from the Bronze layer into the Silver layer by validating ZIP code prefixes, standardizing city and state names, verifying latitude and longitude values, and preparing trusted geographic reference data for customer and seller analytics.
