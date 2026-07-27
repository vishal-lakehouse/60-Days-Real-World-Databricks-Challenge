# Day 54 — Sprint 7

# 🚀 JIRA ID: OLIST-704

## Epic

**Enterprise Data Model & Database Architecture**

---

# 📖 User Story

**As a Data Architect,**

I want to design a scalable, optimized, and business-oriented enterprise data model,

so that the Data Engineering team can build reliable pipelines while business users receive fast and accurate analytics.

---

# 🎯 Objective

Today you will design the complete **Enterprise Data Model** for the Olist Lakehouse.

By the end of today's assignment, you will learn how to:

- Design Conceptual Data Models
- Create Logical Data Models
- Build Physical Database Models
- Design Star Schema
- Design Fact & Dimension Tables
- Implement Slowly Changing Dimensions (SCD)
- Optimize Partitioning Strategy
- Define Enterprise Naming Standards
- Prepare Production Database Architecture

---

# 🏢 Business Scenario

The Azure infrastructure has been successfully provisioned.

Before development begins, the client requires a production-ready data model that supports:

- Executive Dashboards
- Sales Analytics
- Customer Analytics
- Inventory Management
- Financial Reporting
- Historical Reporting
- Machine Learning Readiness

The architecture must support millions of records while maintaining excellent query performance and long-term scalability.

Your responsibility is to create the complete enterprise data model that will be used throughout the project lifecycle.

---

# 📂 Business Inputs

```
Business Requirement Document

Solution Architecture

Source System Inventory

Business KPIs

Reporting Requirements

Historical Data Requirements
```

---

# 🏗 Expected Deliverables

```
Conceptual Data Model

Logical Data Model

Physical Data Model

Star Schema

Fact & Dimension Design

SCD Strategy

Database Standards

ER Diagram
```

---

# 🛠 Technologies

- Azure Databricks
- Delta Lake
- Unity Catalog
- Apache Spark
- Spark SQL
- Power BI
- Draw.io / Lucidchart (Conceptual)
- GitHub

---

# 📋 Acceptance Criteria

✅ Conceptual model completed

✅ Logical model designed

✅ Physical model prepared

✅ Star schema created

✅ Fact and dimension tables defined

✅ SCD strategy documented

✅ ER diagrams completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-704_Data_Model_Architecture
```

---

## Task 2

Design the Conceptual Data Model.

Identify major business entities.

Example:

```
Customers

Orders

Products

Sellers

Payments

Reviews

Categories

Geolocation
```

Document the business relationship between each entity.

---

## Task 3

Create the Logical Data Model.

Define:

- Primary Keys
- Foreign Keys
- Relationships
- Cardinality
- Business Rules

Document one-to-one, one-to-many, and many-to-many relationships.

---

## Task 4

Design the Physical Database Model.

Specify:

```
Database

Catalog

Schema

Table Names

Column Names

Data Types

Constraints
```

Ensure the design follows enterprise naming conventions.

---

## Task 5

Design the Enterprise Star Schema.

Create:

### Fact Tables

```
fact_orders

fact_payments

fact_shipments
```

### Dimension Tables

```
dim_customer

dim_product

dim_seller

dim_category

dim_date

dim_location
```

Document:

- Grain
- Measures
- Keys
- Relationships

---

## Task 6

Implement Slowly Changing Dimensions (SCD).

Design SCD strategies for:

```
Customer

Product

Seller
```

Define where to use:

```
Type 1

Type 2

Type 3
```

Explain why each strategy is appropriate.

---

## Task 7

Design Partitioning & Optimization Strategy.

Create partitioning rules for:

```
Orders

Payments

Reviews

Logs
```

Document:

- Partition Columns
- File Size Strategy
- Delta Optimization
- Z-Ordering
- Data Skipping

---

## Task 8

Define Naming Standards.

Create naming conventions for:

```
Databases

Catalogs

Schemas

Tables

Columns

Primary Keys

Foreign Keys

Views

Pipelines
```

Ensure consistency across all environments.

---

## Task 9

Prepare Enterprise Data Dictionary.

For every table document:

```
Column Name

Data Type

Description

Nullable

Business Meaning

Example Value
```

Store the data dictionary in the project documentation.

---

## Task 10

Design Data Lineage.

Illustrate the flow:

```
Source Systems

↓

Bronze Tables

↓

Silver Tables

↓

Gold Tables

↓

Power BI Dashboards

↓

Business Users
```

Document transformations at each stage.

---

## Task 11

Create Enterprise ER Diagrams.

Prepare diagrams for:

```
Conceptual Model

Logical Model

Physical Model

Star Schema

Data Lineage
```

---

## Task 12 ⭐

Create the **Enterprise Data Modeling Document**.

Include:

- Conceptual Model
- Logical Model
- Physical Model
- Star Schema
- Fact Tables
- Dimension Tables
- SCD Strategy
- Partitioning Strategy
- Naming Standards
- Data Dictionary
- ER Diagrams
- Best Practices

---

# 📚 Concepts Covered

- Conceptual Data Modeling
- Logical Data Modeling
- Physical Data Modeling
- Star Schema
- Fact Tables
- Dimension Tables
- Slowly Changing Dimensions
- Data Dictionary
- Partitioning Strategy
- Enterprise Database Design

---

# 💡 Mini Challenge

Complete the following tasks.

1. Identify eight business entities.

2. Create a logical data model.

3. Design the physical schema.

4. Build a star schema.

5. Create three fact tables.

6. Create six dimension tables.

7. Implement SCD strategies.

8. Design a partitioning strategy.

9. Prepare a data dictionary.

10. Draw the complete ER diagram.

---

# 🧠 Real Interview Questions

### Q1

What is the difference between Conceptual, Logical, and Physical Data Models?

---

### Q2

Why is a Star Schema preferred for analytical workloads?

---

### Q3

How do Fact Tables differ from Dimension Tables?

---

### Q4

When would you use SCD Type 1, Type 2, and Type 3?

---

### Q5

How does partitioning improve query performance in Delta Lake?

---

### Q6

What should be included in an enterprise Data Dictionary?

---

### Q7

How do ER diagrams help Data Engineering teams during implementation?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Data Modeling Notebook Created

✓ Conceptual Data Model Designed

✓ Logical Data Model Completed

✓ Physical Database Model Created

✓ Star Schema Designed

✓ Fact & Dimension Tables Documented

✓ SCD Strategy Defined

✓ Partitioning Strategy Prepared

✓ Enterprise Data Dictionary Completed

✓ Enterprise Data Modeling Document Created
```

---

# 🏁 End Goal

At the end of Day 54, you will have a production-ready enterprise data model that serves as the blueprint for all pipeline development, analytics, and reporting.

```
Business Requirements
        │
        ▼
Conceptual Data Model
        │
        ▼
Logical Data Model
        │
        ▼
Physical Database Model
        │
        ▼
Star Schema
        │
        ▼
Fact & Dimension Tables
        │
        ▼
Gold Analytics Layer
        │
        ▼
Power BI Dashboards
```

Your enterprise data platform now has a standardized and scalable database architecture with optimized schemas, well-defined relationships, Slowly Changing Dimension strategies, partitioning guidelines, and complete documentation. This model provides the foundation for efficient data ingestion, transformation, governance, and business analytics.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| Sprint 3 | OLIST-301 → OLIST-310 | Gold Analytics Layer | ✅ Complete |
| Sprint 4 | OLIST-401 → OLIST-402 | Reporting Data Mart & Power BI | ✅ Complete |
| Sprint 5 | OLIST-501 → OLIST-510 | Production Lakehouse & Enterprise Features | ✅ Complete |
| Sprint 6 | OLIST-601 → OLIST-610 | Enterprise Platform Engineering | ✅ Complete |
| Sprint 7 | OLIST-701 | Enterprise Client Kickoff & Requirement Gathering | ✅ Complete |
| Sprint 7 | OLIST-702 | Enterprise Solution Architecture Design | ✅ Complete |
| Sprint 7 | OLIST-703 | Enterprise Azure Infrastructure Provisioning | ✅ Complete |
| **Sprint 7** | **OLIST-704** | **Enterprise Data Model & Database Architecture** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 55)

## 🚀 JIRA ID: OLIST-705

**Develop End-to-End Enterprise Data Pipelines** by implementing production-ready ingestion, transformation, and orchestration workflows for the Olist Lakehouse. You'll build metadata-driven Azure Data Factory pipelines, PySpark transformations in Azure Databricks, Delta Lake optimizations, Medallion architecture processing, incremental loading, Change Data Capture (CDC), workflow orchestration, exception handling, data quality validation, and operational monitoring to deliver trusted business-ready datasets.
