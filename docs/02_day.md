# Day 02 — Sprint 1

# 🚀 JIRA ID: OLIST-102

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Orders** dataset into the Bronze layer,

so that customer orders can be stored in Delta Lake and used by downstream pipelines.

---

# 🎯 Objective

Today you will ingest the Orders dataset and validate its relationship with the Customer dataset.

After completing today's assignment, you will understand:

- Loading multiple datasets
- Working with timestamps
- Schema validation
- Data quality checks
- Foreign key validation
- Creating multiple Bronze Delta tables
- Basic Spark SQL validation

---

# 🏢 Business Scenario

Every order placed by customers is exported daily from the Olist transaction system.

Your responsibility is to load the Orders dataset into the Bronze layer exactly as received without modifying any data.

---

# 📂 Source Dataset

```
datasets/raw/olist_orders_dataset.csv
```

---

# 🏗 Target Layer

```
bronze.orders
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

✅ Orders CSV uploaded

✅ Read using PySpark

✅ Schema validated

✅ Timestamp columns verified

✅ Record count validated

✅ Bronze Delta table created

✅ SQL validations completed

✅ Customer relationship validated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-102_Load_Orders_Bronze
```

---

## Task 2

Upload

```
olist_orders_dataset.csv
```

---

## Task 3

Read the CSV into a Spark DataFrame.

---

## Task 4

Display the first 10 rows.

---

## Task 5

Print the schema.

Identify all timestamp columns.

---

## Task 6

Count total records.

---

## Task 7

Check for duplicate Order IDs.

---

## Task 8

Check for NULL values in

```
order_id

customer_id
```

---

## Task 9

Save the DataFrame as

```
bronze.orders
```

using Delta format.

---

## Task 10

Validate using Spark SQL.

Example:

- Total Orders
- Delivered Orders
- Cancelled Orders
- Distinct Customers
- Distinct Order Status

---

## Task 11 ⭐

Validate relationship with Customers.

Questions:

- Does every order have a customer?
- Are there any customer IDs in Orders that do not exist in Customers?

(Hint: Use a LEFT ANTI JOIN.)

---

# 📚 Concepts Covered

- Multiple Delta Tables
- Timestamp Columns
- Foreign Keys
- LEFT ANTI JOIN
- DISTINCT
- COUNT
- Data Validation
- Spark SQL

---

# 💡 Mini Challenge

Find the answer to these questions:

1. How many unique customers placed orders?

2. Which order status appears most frequently?

3. Which customer placed the earliest order?

4. Which customer placed the latest order?

5. How many orders have not been delivered?

---

# 🧠 Real Interview Questions

### Q1

What is the purpose of the Orders table?

---

### Q2

Why should foreign key relationships be validated during ingestion?

---

### Q3

What is a LEFT ANTI JOIN?

Where is it used?

---

### Q4

Why should timestamps be stored using the correct data type?

---

### Q5

Why is the Bronze layer expected to preserve raw data?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Orders Notebook Created

✓ Orders CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ Duplicate Check Completed

✓ NULL Validation Completed

✓ Bronze Orders Table Created

✓ Customer Relationship Validated

✓ SQL Validation Completed
```

---

# 🏁 End Goal

At the end of Day 2, you will have two production-style Bronze Delta tables:

```
bronze.customers

bronze.orders
```

You will also validate the first business relationship in the project:

```
Customers
      │
      ▼
Orders
```

This is a fundamental step in building reliable data pipelines.

---

# 🔜 Tomorrow (Day 03)

**JIRA ID: OLIST-103**

Load the **Order Items** dataset into the Bronze layer and build relationships with Orders, Products, and Sellers.
