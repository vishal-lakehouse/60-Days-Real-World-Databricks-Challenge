# Day 06 — Sprint 1

# 🚀 JIRA ID: OLIST-106

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Order Payments** dataset into the Bronze layer,

so that payment information is available for financial reporting, customer analysis, and downstream business intelligence.

---

# 🎯 Objective

Today you will ingest the **Order Payments** dataset and understand how payment information is linked to customer orders.

By the end of today's assignment, you will learn how to:

- Load payment transaction data into Databricks
- Work with composite primary keys
- Validate payment records
- Analyse payment methods
- Store payment data as Delta tables
- Validate relationships with the Orders dataset

---

# 🏢 Business Scenario

Customers can pay for an order using different payment methods such as:

- Credit Card
- Debit Card
- Voucher
- Boleto

Some orders may even contain multiple payment records.

Your responsibility is to ingest the payment dataset into the Bronze layer exactly as received from the source system.

No transformations.

No business rules.

Only ingestion and validation.

---

# 📂 Source Dataset

```
datasets/raw/olist_order_payments_dataset.csv
```

---

# 🏗 Target Layer

```
bronze.order_payments
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

✅ Payments CSV uploaded

✅ Data read successfully

✅ Schema validated

✅ Composite Primary Key validated

✅ Duplicate records checked

✅ NULL values analysed

✅ Bronze Delta table created

✅ Relationship with Orders validated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-106_Load_Order_Payments_Bronze
```

---

## Task 2

Upload

```
olist_order_payments_dataset.csv
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

- order_id
- payment_sequential
- payment_type
- payment_installments
- payment_value

---

## Task 6

Count total payment records.

---

## Task 7

Validate the Composite Primary Key.

```
order_id

payment_sequential
```

Ensure duplicate combinations do not exist.

---

## Task 8

Analyse NULL values.

Check every column for missing values.

Remember:

Do **not** clean the data in the Bronze layer.

---

## Task 9

Save the DataFrame as

```
bronze.order_payments
```

using Delta format.

---

## Task 10

Validate relationship with Orders.

Questions:

- Does every payment belong to an existing order?
- Are there payment records without matching orders?

Use:

```
LEFT ANTI JOIN
```

---

## Task 11

Explore Payment Methods.

Find:

- Total payment records
- Number of payment methods
- Most frequently used payment method
- Average payment value
- Highest payment value
- Highest number of instalments

---

# 📚 Concepts Covered

- Transactional Data
- Composite Primary Key
- Payment Analytics
- LEFT ANTI JOIN
- Delta Lake
- Spark SQL
- Data Profiling

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. Which payment method is used the most?

2. Which payment method generates the highest total payment value?

3. What is the average payment value by payment method?

4. How many orders have multiple payment records?

5. What is the maximum number of payment instalments?

---

# 🧠 Real Interview Questions

### Q1

Why does the Order Payments table use a Composite Primary Key?

---

### Q2

Why can a single order have multiple payment records?

---

### Q3

What is the purpose of validating payment records against the Orders table?

---

### Q4

Why should payment data remain unchanged in the Bronze layer?

---

### Q5

How would you identify payment records that don't belong to any order?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Order Payments Notebook Created

✓ Payments CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ Composite Key Validated

✓ NULL Analysis Completed

✓ Bronze Order Payments Table Created

✓ Orders Relationship Validated

✓ Payment Analysis Completed
```

---

# 🏁 End Goal

At the end of Day 6, your Bronze layer will contain:

```
bronze.customers

bronze.orders

bronze.order_items

bronze.products

bronze.sellers

bronze.order_payments
```

You will now have the complete financial transaction dataset required for downstream analytics in the Silver and Gold layers.

---

# 📈 Sprint Progress

| JIRA ID | Task | Status |
|----------|------|--------|
| OLIST-101 | Load Customers | ✅ Complete |
| OLIST-102 | Load Orders | ✅ Complete |
| OLIST-103 | Load Order Items | ✅ Complete |
| OLIST-104 | Load Products | ✅ Complete |
| OLIST-105 | Load Sellers | ✅ Complete |
| **OLIST-106** | **Load Order Payments** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 07)

**🚀 JIRA ID: OLIST-107**

Load the **Order Reviews** dataset into the Bronze layer and validate its relationship with the Orders dataset. You'll analyse customer ratings, review comments, and review timestamps while completing another core dataset in the Bronze layer.
