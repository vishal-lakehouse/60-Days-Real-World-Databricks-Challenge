# Day 05 — Sprint 1

# 🚀 JIRA ID: OLIST-105

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Sellers** dataset into the Bronze layer,

so that seller information is available for downstream reporting, analytics, and relationship validation.

---

# 🎯 Objective

Today you will ingest the **Sellers** dataset and understand how seller master data connects with customer orders.

By the end of today's assignment, you will learn how to:

- Load master data into Databricks
- Validate unique identifiers
- Perform data profiling
- Validate relationships between datasets
- Store data as Delta tables
- Use Spark SQL for data quality checks

---

# 🏢 Business Scenario

The Olist marketplace allows thousands of independent sellers to list and sell products.

Each seller has:

- Seller ID
- ZIP Code
- City
- State

Your responsibility is to ingest this dataset into the Bronze layer exactly as received from the source system.

No transformations.

No data cleansing.

Only ingestion and validation.

---

# 📂 Source Dataset

```
datasets/raw/olist_sellers_dataset.csv
```

---

# 🏗 Target Layer

```
bronze.sellers
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

✅ Sellers CSV uploaded

✅ Data read successfully

✅ Schema validated

✅ Duplicate Seller IDs checked

✅ NULL values analysed

✅ Bronze Delta table created

✅ Relationship with Order Items validated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-105_Load_Sellers_Bronze
```

---

## Task 2

Upload

```
olist_sellers_dataset.csv
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

- seller_id
- seller_zip_code_prefix
- seller_city
- seller_state

---

## Task 6

Count total sellers.

---

## Task 7

Check duplicate Seller IDs.

---

## Task 8

Analyse NULL values in every column.

Remember:

The Bronze layer stores raw data.

Do not modify missing values.

---

## Task 9

Save the DataFrame as

```
bronze.sellers
```

using Delta format.

---

## Task 10

Validate relationship with Order Items.

Questions:

- Does every Order Item reference a valid Seller?
- Are there Seller IDs in Order Items that do not exist in Sellers?
- Are there Sellers who have never sold any products?

Use:

```
LEFT JOIN

LEFT ANTI JOIN
```

---

## Task 11

Explore Seller Distribution.

Find:

- Total number of states
- Total number of cities
- Top 10 states by seller count
- Top 10 cities by seller count

---

# 📚 Concepts Covered

- Master Data
- Primary Key Validation
- Data Profiling
- LEFT JOIN
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL
- Relationship Validation

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many sellers are registered?

2. Which state has the highest number of sellers?

3. Which city has the highest number of sellers?

4. Are there sellers without any associated orders?

5. How many unique states are represented in the dataset?

---

# 🧠 Real Interview Questions

### Q1

Why is the Sellers table considered master data?

---

### Q2

Why should Seller IDs be unique?

---

### Q3

How would you identify sellers that have never sold a product?

---

### Q4

Why do we validate foreign key relationships after ingestion?

---

### Q5

Why should Bronze tables remain unchanged from the source data?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Sellers Notebook Created

✓ Sellers CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ Duplicate Check Completed

✓ NULL Analysis Completed

✓ Bronze Sellers Table Created

✓ Relationship Validation Completed

✓ Seller Distribution Analysis Completed
```

---

# 🏁 End Goal

At the end of Day 5, you will have successfully ingested the complete **Seller** master dataset into the Bronze layer.

Your Bronze layer will now contain:

```
bronze.customers

bronze.orders

bronze.order_items

bronze.products

bronze.sellers
```

You now have enough datasets to perform end-to-end relationship validation across customers, orders, products, sellers, and order items.

---

# 📈 Sprint Progress

| JIRA ID | Task | Status |
|----------|------|--------|
| OLIST-101 | Load Customers | ✅ Complete |
| OLIST-102 | Load Orders | ✅ Complete |
| OLIST-103 | Load Order Items | ✅ Complete |
| OLIST-104 | Load Products | ✅ Complete |
| **OLIST-105** | **Load Sellers** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 06)

**🚀 JIRA ID: OLIST-106**

Load the **Order Payments** dataset into the Bronze layer and analyse payment methods, instalments, and payment values while validating relationships with the Orders dataset.
