# Day 32 — Sprint 5

# 🚀 JIRA ID: OLIST-502

## Epic

**Production ETL Optimization**

---

# 📖 User Story

**As a Senior Data Engineer,**

I want to implement Incremental Data Loading and Change Data Capture (CDC),

so that the pipeline processes only new and modified records, reducing execution time, compute costs, and improving overall system efficiency.

---

# 🎯 Objective

Today you will upgrade your Lakehouse pipeline to support **Incremental Data Loading** and **Change Data Capture (CDC)** using Delta Lake.

By the end of today's assignment, you will learn how to:

- Implement Incremental ETL
- Perform Delta Lake MERGE operations
- Build Idempotent Pipelines
- Handle Inserts, Updates, and Deletes
- Implement Watermarking
- Apply Slowly Changing Dimensions (SCD)
- Optimize production ETL workflows

---

# 🏢 Business Scenario

The Olist platform receives new orders every day.

Currently, the ETL pipeline reloads the entire dataset, even when only a few records have changed.

This approach results in:

- Long execution times
- Higher compute costs
- Inefficient resource usage
- Increased operational overhead

The Engineering Team wants to process only the records that have changed since the last successful pipeline execution.

Your responsibility is to implement an efficient Incremental ETL strategy using Delta Lake.

---

# 📂 Source Tables

```
bronze.orders

silver.orders

gold.sales_summary
```

---

# 🏗 Target Tables

```
silver.orders

gold.sales_summary
```

---

# 🛠 Technologies

- Azure Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Delta MERGE
- Databricks Workflows

---

# 📋 Acceptance Criteria

✅ Incremental Load implemented

✅ Watermark column identified

✅ MERGE operation completed

✅ Inserts processed

✅ Updates processed

✅ Duplicate processing avoided

✅ Validation report generated

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-502_Incremental_Load_CDC
```

---

## Task 2

Read the following tables.

```
bronze.orders

silver.orders

gold.sales_summary
```

---

## Task 3

Identify the Incremental Column.

Choose an appropriate watermark column.

Examples:

```
order_purchase_timestamp

order_approved_at

last_updated_timestamp
```

Explain why the selected column is suitable for incremental processing.

---

## Task 4

Filter New Records.

Retrieve only records where:

```
Source Timestamp >

Last Successful Load Timestamp
```

Document the filtering logic.

---

## Task 5

Implement Delta MERGE.

Handle:

```
INSERT

UPDATE
```

using

```
MERGE INTO
```

Ensure existing records are updated and new records are inserted.

---

## Task 6

Handle Duplicate Processing.

Ensure:

- Re-running the notebook does not create duplicates.
- The pipeline is idempotent.
- Existing records remain consistent.

Document the approach.

---

## Task 7

Implement Change Data Capture (CDC).

Handle scenarios such as:

- New Orders
- Updated Order Status
- Updated Delivery Date
- Updated Payment Information

Document how each change is processed.

---

## Task 8

Implement Slowly Changing Dimensions.

Explain the differences between:

```
SCD Type 1

SCD Type 2
```

Implement one of the approaches for a selected dimension.

Document your design decision.

---

## Task 9

Refresh Downstream Gold Tables.

Update:

```
gold.sales_summary
```

using only the affected incremental records instead of rebuilding the entire table.

---

## Task 10

Validate Incremental Processing.

Verify:

- No duplicate Order IDs.
- Updates applied correctly.
- New records inserted successfully.
- Gold table reflects recent changes.
- Re-running the notebook produces the same result.

---

## Task 11

Measure Pipeline Performance.

Compare:

- Full Load Duration
- Incremental Load Duration
- Records Processed
- Estimated Compute Savings

Document your observations.

---

## Task 12 ⭐

Create an Incremental Load Validation Report.

Include:

- Source Tables
- Watermark Column
- Records Read
- Records Inserted
- Records Updated
- Records Ignored
- MERGE Validation
- Data Quality Checks
- Performance Comparison
- Business Rules Applied

---

# 📚 Concepts Covered

- Incremental Loading
- Change Data Capture (CDC)
- Delta Lake MERGE
- Watermarking
- Idempotent Pipelines
- Slowly Changing Dimensions
- Upserts
- Production ETL Optimization

---

# 💡 Mini Challenge

Complete the following using Spark SQL.

1. Find records added after the last successful pipeline run.

2. Write a `MERGE INTO` statement to update existing orders.

3. Count inserted and updated records separately.

4. Detect duplicate Order IDs.

5. Compare Full Load vs Incremental Load record counts.

6. Implement an SCD Type 1 update.

7. Identify records eligible for SCD Type 2.

8. Validate that no duplicate records exist after the MERGE.

9. Calculate pipeline execution time improvement.

10. Design a reusable Incremental ETL framework.

---

# 🧠 Real Interview Questions

### Q1

What is Incremental Data Loading?

---

### Q2

What is the difference between a Full Load and an Incremental Load?

---

### Q3

How does Delta Lake `MERGE` work?

---

### Q4

What is a Watermark in an ETL pipeline?

---

### Q5

How do you make an ETL pipeline idempotent?

---

### Q6

What is Change Data Capture (CDC)?

---

### Q7

What is the difference between SCD Type 1 and SCD Type 2?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Incremental ETL Notebook Created

✓ Watermark Strategy Implemented

✓ Delta MERGE Completed

✓ CDC Logic Implemented

✓ SCD Strategy Documented

✓ Gold Table Incrementally Updated

✓ Idempotent Pipeline Verified

✓ Performance Comparison Completed

✓ Validation Report Generated
```

---

# 🏁 End Goal

At the end of Day 32, your Lakehouse will support production-grade incremental processing.

```
New Source Data
        │
        ▼
 Watermark Filter
        │
        ▼
 Incremental Records
        │
        ▼
 Delta MERGE
        │
        ▼
 Silver Layer
        │
        ▼
 Incremental Gold Refresh
        │
        ▼
 Power BI Dashboard
```

Instead of processing the entire dataset, your pipeline now efficiently handles only new and changed records, significantly reducing execution time and compute costs while ensuring data consistency and reliability.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| Sprint 3 | OLIST-301 → OLIST-310 | Gold Analytics Layer | ✅ Complete |
| Sprint 4 | OLIST-401 → OLIST-402 | Reporting Data Mart & Power BI | ✅ Complete |
| Sprint 5 | OLIST-501 | Deploy Production Databricks Workflow | ✅ Complete |
| **Sprint 5** | **OLIST-502** | **Implement Incremental Loading & CDC** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 33)

## 🚀 JIRA ID: OLIST-503

**Optimize Delta Lake Performance** by implementing partitioning, Z-Ordering, `OPTIMIZE`, `VACUUM`, file compaction, and data skipping techniques. You'll learn how to tune Delta Lake tables for faster queries, lower storage costs, and high-performance analytics in enterprise-scale Lakehouse environments.
