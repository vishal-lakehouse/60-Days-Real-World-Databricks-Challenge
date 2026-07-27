# Day 03 — Sprint 1

# 🚀 JIRA ID: OLIST-103

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Order Items** dataset into the Bronze layer,

so that every product purchased in each order is stored in Delta Lake for downstream processing and analytics.

---

# 🎯 Objective

Today you will ingest the **Order Items** dataset and validate its relationships with Orders, Products, and Sellers.

By the end of today's assignment, you will learn how to:

- Load transactional datasets
- Work with composite primary keys
- Validate foreign key relationships
- Detect duplicate records
- Perform data quality checks
- Store data as Delta tables
- Query data using Spark SQL

---

# 🏢 Business Scenario

Each customer order may contain one or more products.

Every product is sold by a seller and belongs to an order.

Your responsibility is to ingest the Order Items dataset into the Bronze layer exactly as received from the source system.

---

# 📂 Source Dataset

```
datasets/raw/olist_order_items_dataset.csv
```

---

# 🏗 Target Layer

```
bronze.order_items
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

✅ Order Items CSV uploaded

✅ Data read successfully using PySpark

✅ Schema validated

✅ Composite Primary Key verified

✅ Duplicate records checked

✅ Null value validation completed

✅ Bronze Delta table created

✅ Relationships validated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-103_Load_Order_Items_Bronze
```

---

## Task 2

Upload

```
olist_order_items_dataset.csv
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

- Price column
- Freight column
- Timestamp column

---

## Task 6

Count total records.

---

## Task 7

Validate the Composite Primary Key

```
order_id

order_item_id
```

Ensure no duplicate combinations exist.

---

## Task 8

Check NULL values for:

```
order_id

order_item_id

product_id

seller_id
```

---

## Task 9

Save the dataset as

```
bronze.order_items
```

using Delta format.

---

## Task 10

Validate the Orders relationship.

Questions:

- Does every Order Item belong to an Order?
- Are there any Order IDs that don't exist in the Orders table?

(Hint: Use a LEFT ANTI JOIN.)

---

## Task 11

Validate the Products relationship.

Questions:

- Are there any Product IDs that don't exist in the Products dataset?

*(If Products haven't been loaded yet, write the validation query and execute it after Day 4.)*

---

## Task 12

Validate the Sellers relationship.

Questions:

- Are there any Seller IDs that don't exist in the Sellers dataset?

*(If Sellers haven't been loaded yet, write the validation query and execute it after Day 5.)*

---

# 📚 Concepts Covered

- Composite Primary Keys
- Foreign Keys
- LEFT ANTI JOIN
- Data Quality Validation
- Delta Tables
- Spark SQL
- Transactional Data

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many products were sold?

2. Which order contains the highest number of items?

3. Which seller sold the most products?

4. What is the highest product price?

5. What is the average freight value?

---

# 🧠 Real Interview Questions

### Q1

Why is a Composite Primary Key used in the Order Items table?

---

### Q2

Why shouldn't duplicate Order Items exist?

---

### Q3

What is the difference between a Primary Key and a Foreign Key?

---

### Q4

Why do we validate relationships during data ingestion?

---

### Q5

Why is Delta Lake preferred over storing raw CSV files for analytics?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Order Items Notebook Created

✓ Order Items CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ Composite Key Validated

✓ Duplicate Check Completed

✓ NULL Validation Completed

✓ Bronze Order Items Table Created

✓ Relationship Validation Completed (Orders)

✓ Validation Queries Prepared (Products & Sellers)
```

---

# 🏁 End Goal

At the end of Day 3, you will have three production-style Bronze Delta tables:

```
bronze.customers

bronze.orders

bronze.order_items
```

You will also establish the core transactional relationship:

```
Customers
      │
      ▼
Orders
      │
      ▼
Order Items
```

This forms the backbone of the entire e-commerce data model and is essential for downstream transformations in the Silver and Gold layers.

---

# 🔜 Tomorrow (Day 04)

**🚀 JIRA ID: OLIST-104**

Load the **Products** dataset into the Bronze layer and prepare it for product analytics and category mapping.
