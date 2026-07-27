# Day 07 — Sprint 1

# 🚀 JIRA ID: OLIST-107

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Order Reviews** dataset into the Bronze layer,

so that customer feedback can be stored in Delta Lake and used for customer satisfaction analysis and downstream reporting.

---

# 🎯 Objective

Today you will ingest the **Order Reviews** dataset and validate its relationship with the Orders dataset.

By the end of today's assignment, you will learn how to:

- Load review data into Databricks
- Validate primary and foreign keys
- Analyse review scores
- Handle nullable text columns
- Create Delta tables
- Perform data quality validation using Spark SQL

---

# 🏢 Business Scenario

After receiving an order, customers can rate their shopping experience and leave written feedback.

Each review contains:

- Review ID
- Order ID
- Rating Score
- Review Title
- Review Message
- Review Creation Date
- Review Response Timestamp

Your responsibility is to ingest this dataset into the Bronze layer exactly as received from the source system.

No cleaning.

No sentiment analysis.

No modifications.

Only ingestion and validation.

---

# 📂 Source Dataset

```
datasets/raw/olist_order_reviews_dataset.csv
```

---

# 🏗 Target Layer

```
bronze.order_reviews
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

✅ Reviews CSV uploaded

✅ Data read successfully

✅ Schema validated

✅ Review IDs validated

✅ NULL values analysed

✅ Bronze Delta table created

✅ Relationship with Orders validated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-107_Load_Order_Reviews_Bronze
```

---

## Task 2

Upload

```
olist_order_reviews_dataset.csv
```

---

## Task 3

Read the CSV into a Spark DataFrame.

---

## Task 4

Display the first 10 records.

---

## Task 5

Print the schema.

Identify:

- review_id
- order_id
- review_score
- review_creation_date
- review_answer_timestamp

---

## Task 6

Count total review records.

---

## Task 7

Check duplicate Review IDs.

---

## Task 8

Analyse NULL values.

Pay special attention to:

```
review_comment_title

review_comment_message
```

Remember:

Many customers may leave only a rating without a written review.

Do **not** modify missing values in the Bronze layer.

---

## Task 9

Save the DataFrame as

```
bronze.order_reviews
```

using Delta format.

---

## Task 10

Validate relationship with Orders.

Questions:

- Does every review belong to an existing order?
- Are there reviews without matching orders?

Use:

```
LEFT ANTI JOIN
```

---

## Task 11

Explore Customer Ratings.

Find:

- Total reviews
- Average review score
- Highest review score
- Lowest review score
- Count of reviews for each rating (1–5)

---

## Task 12 ⭐

Analyse Review Messages.

Find:

- Reviews with no title
- Reviews with no message
- Reviews with both title and message
- Longest review message

---

# 📚 Concepts Covered

- Customer Feedback Data
- Primary Key Validation
- Foreign Key Validation
- NULL Analysis
- Data Profiling
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. What is the average review score?

2. Which rating (1–5) appears most frequently?

3. How many reviews have no written message?

4. How many reviews have both a title and a message?

5. Which review score has the fewest records?

---

# 🧠 Real Interview Questions

### Q1

Why are review comments often NULL?

---

### Q2

Why shouldn't NULL review messages be replaced in the Bronze layer?

---

### Q3

How would you validate that every review belongs to an existing order?

---

### Q4

What is the difference between structured and unstructured data in this dataset?

---

### Q5

Why is customer review data valuable for business analytics?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Order Reviews Notebook Created

✓ Reviews CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ Duplicate Check Completed

✓ NULL Analysis Completed

✓ Bronze Order Reviews Table Created

✓ Orders Relationship Validated

✓ Customer Rating Analysis Completed
```

---

# 🏁 End Goal

At the end of Day 7, your Bronze layer will contain:

```
bronze.customers

bronze.orders

bronze.order_items

bronze.products

bronze.sellers

bronze.order_payments

bronze.order_reviews
```

You now have almost all the core transactional datasets ingested into your Lakehouse, including customer feedback for future customer satisfaction and sentiment analysis.

---

# 📈 Sprint Progress

| JIRA ID | Task | Status |
|----------|------|--------|
| OLIST-101 | Load Customers | ✅ Complete |
| OLIST-102 | Load Orders | ✅ Complete |
| OLIST-103 | Load Order Items | ✅ Complete |
| OLIST-104 | Load Products | ✅ Complete |
| OLIST-105 | Load Sellers | ✅ Complete |
| OLIST-106 | Load Order Payments | ✅ Complete |
| **OLIST-107** | **Load Order Reviews** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 08)

**🚀 JIRA ID: OLIST-108**

Load the **Geolocation** dataset into the Bronze layer and explore geographic information such as ZIP codes, cities, states, latitude, and longitude. You'll prepare location data that will later enrich customer and seller analytics in the Silver and Gold layers.
