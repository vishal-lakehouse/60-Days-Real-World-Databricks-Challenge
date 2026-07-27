# Day 08 — Sprint 1

# 🚀 JIRA ID: OLIST-108

## Epic

**Build Bronze Layer**

---

# 📖 User Story

**As a Data Engineer,**

I want to ingest the **Geolocation** dataset into the Bronze layer,

so that location data can be used to enrich customer, seller, and business analytics in downstream layers.

---

# 🎯 Objective

Today you will ingest the **Geolocation** dataset and understand how geographical information supports business intelligence.

By the end of today's assignment, you will learn how to:

- Load geographical datasets into Databricks
- Work with latitude and longitude
- Profile location data
- Understand datasets without a primary key
- Store data in Delta Lake
- Perform exploratory analysis using Spark SQL

---

# 🏢 Business Scenario

The Olist platform stores geographical information based on Brazilian ZIP code prefixes.

This dataset is used to determine where customers and sellers are located and helps answer business questions such as:

- Which states generate the most sales?
- Which cities have the most customers?
- Which regions have the most sellers?

Unlike previous datasets, this table is a **reference dataset** and does not have a unique primary key.

Your responsibility is to ingest the dataset into the Bronze layer exactly as received.

No transformations.

No deduplication.

No data cleaning.

Only ingestion and validation.

---

# 📂 Source Dataset

```
datasets/raw/olist_geolocation_dataset.csv
```

---

# 🏗 Target Layer

```
bronze.geolocation
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

✅ Geolocation CSV uploaded

✅ Data read successfully

✅ Schema validated

✅ Latitude and Longitude verified

✅ NULL values analysed

✅ Bronze Delta table created

✅ Basic geographical analysis completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-108_Load_Geolocation_Bronze
```

---

## Task 2

Upload

```
olist_geolocation_dataset.csv
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

- geolocation_zip_code_prefix
- geolocation_city
- geolocation_state
- geolocation_lat
- geolocation_lng

---

## Task 6

Count total records.

---

## Task 7

Analyse NULL values in every column.

Remember:

Do **not** modify missing values in the Bronze layer.

---

## Task 8

Check for duplicate ZIP code prefixes.

Questions:

- Are duplicate ZIP prefixes expected?
- Why might the same ZIP code appear multiple times?

Discuss your observations.

---

## Task 9

Save the DataFrame as

```
bronze.geolocation
```

using Delta format.

---

## Task 10

Explore the geographical data.

Find:

- Total unique ZIP code prefixes
- Total unique cities
- Total unique states
- Top 10 states by record count
- Top 10 cities by record count

---

## Task 11 ⭐

Analyse coordinates.

Find:

- Minimum latitude
- Maximum latitude
- Minimum longitude
- Maximum longitude

Check whether any coordinates appear to be missing or invalid.

---

# 📚 Concepts Covered

- Reference Data
- Latitude & Longitude
- Data Profiling
- Delta Lake
- Spark SQL
- Distinct Values
- Geographic Data

---

# 💡 Mini Challenge

Answer the following using Spark SQL:

1. How many unique ZIP code prefixes exist?

2. Which state has the most geolocation records?

3. Which city appears most frequently?

4. What is the northernmost latitude?

5. What is the westernmost longitude?

---

# 🧠 Real Interview Questions

### Q1

Why doesn't the Geolocation dataset have a unique primary key?

---

### Q2

Why can the same ZIP code prefix appear multiple times?

---

### Q3

What is the difference between transactional data and reference data?

---

### Q4

Why is geographical data important in analytics?

---

### Q5

Would you remove duplicate ZIP code prefixes in the Bronze layer? Why or why not?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Geolocation Notebook Created

✓ Geolocation CSV Uploaded

✓ Data Read Successfully

✓ Schema Printed

✓ Record Count Validated

✓ NULL Analysis Completed

✓ Bronze Geolocation Table Created

✓ Geographic Analysis Completed
```

---

# 🏁 End Goal

At the end of Day 8, your Bronze layer will contain:

```
bronze.customers

bronze.orders

bronze.order_items

bronze.products

bronze.sellers

bronze.order_payments

bronze.order_reviews

bronze.geolocation
```

You now have all the major transactional, master, and reference datasets loaded into the Bronze layer, bringing your Lakehouse one step closer to production readiness.

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
| OLIST-107 | Load Order Reviews | ✅ Complete |
| **OLIST-108** | **Load Geolocation** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 09)

**🚀 JIRA ID: OLIST-109**

Load the **Product Category Translation** dataset into the Bronze layer. You'll prepare the mapping between Portuguese and English product categories, completing the Bronze ingestion phase and making the project ready for the Silver layer transformations.
