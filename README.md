# 🚀 60 Days Real World Databricks Challenge

> **A Complete Enterprise Azure Databricks & Data Engineering Project**
>
> Learn Azure Databricks the way it's used in real companies — by building a complete end-to-end Enterprise Lakehouse Platform from scratch.

---

# 🌍 About This Project

Most Databricks tutorials teach isolated concepts.

This repository is different.

Instead of learning random notebooks or small demos, you'll work on a **real-world enterprise project** exactly like a professional Azure Data Engineering team.

Throughout **60 days**, you'll play the role of a **Data Engineer** working for a fictional client (**Olist Brazilian E-Commerce**) while following an Agile Scrum process.

You'll receive realistic Jira tickets, business requirements, architecture decisions, implementation tasks, testing activities, deployment processes, production support, and finally client handover.

By the end, you'll understand **how Enterprise Data Engineering projects are actually delivered.**

---

# 🎯 What You'll Build

An Enterprise Lakehouse Solution using

- Azure Databricks
- Apache Spark
- PySpark
- Delta Lake
- Unity Catalog
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure SQL Database
- Git & GitHub
- Power BI
- Enterprise DevOps
- Production Support

---

# 🏢 Business Case

You are working as an **Azure Data Engineer Consultant**.

Your client is **Olist**, one of Brazil's largest e-commerce marketplaces.

The company wants to modernize its analytics platform by migrating from traditional databases to an Enterprise Lakehouse architecture.

Your responsibility is to design, build, deploy, and support the complete solution.

---

# 📚 What You'll Learn

## Azure

- Azure Databricks
- Azure Data Factory
- Azure Storage (ADLS Gen2)
- Azure SQL Database
- Azure Monitor
- Azure Key Vault

---

## Databricks

- Workspaces
- Compute
- Unity Catalog
- Volumes
- Notebooks
- Workflows
- Jobs
- Repos

---

## Apache Spark

- Spark Architecture
- DataFrames
- Spark SQL
- Optimizations
- Partitioning
- Caching

---

## PySpark

- Data Transformations
- Joins
- Window Functions
- Aggregations
- Performance Optimization
- Modular Coding

---

## Delta Lake

- ACID Transactions
- MERGE
- Time Travel
- CDC
- Schema Evolution
- Optimization

---

## Enterprise Data Engineering

- ETL
- ELT
- Medallion Architecture
- Incremental Loading
- Change Data Capture
- Metadata Driven Pipelines
- Data Validation
- Data Quality
- Monitoring
- Error Handling

---

## DevOps

- Git
- GitHub
- CI/CD
- Release Management
- Production Deployment
- Rollback Strategy

---

## Reporting

- Star Schema
- Power BI
- Executive Dashboards
- KPI Reporting

---

## Enterprise Operations

- Production Support
- Incident Management
- SLA Monitoring
- Root Cause Analysis
- Hypercare
- Client Handover

---

# 🏗 Architecture

```
                    Source Systems
                           │
          SQL Server • CSV • APIs • SFTP
                           │
                           ▼
                Azure Data Factory (ADF)
                           │
                           ▼
               Azure Data Lake Storage Gen2
                           │
                           ▼
               Azure Databricks (PySpark)
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
      Bronze            Silver             Gold
       Layer             Layer             Layer
         │                 │                 │
         └─────────────────┼─────────────────┘
                           ▼
                    Power BI Dashboards
                           │
                           ▼
                  Business Decision Making
```

---

# 🏛 Medallion Architecture

```
Raw Data
    │
    ▼
🥉 Bronze
Raw Ingestion
    │
    ▼
🥈 Silver
Clean & Standardized
    │
    ▼
🥇 Gold
Business Ready Data
```

---

# 📂 Repository Structure

```text
60-Days-Real-World-Databricks-Challenge/
│
├── datasets/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── docs/
│   ├── Architecture.md
│   ├── Data_Dictionary.md
│   ├── Data_Model.md
│   └── ER_Diagram.md
│
├── notebooks/
│
├── images/
│
├── README.md
│
└── LICENSE
```

---

# 🗓 Challenge Roadmap

| Sprint | Days | Focus |
|----------|------|-------------------------------|
| Sprint 1 | Day 1 – 9 | Bronze Layer |
| Sprint 2 | Day 10 – 18 | Silver Layer |
| Sprint 3 | Day 19 – 28 | Gold Layer |
| Sprint 4 | Day 29 – 30 | Power BI Reporting |
| Sprint 5 | Day 31 – 40 | Production Engineering |
| Sprint 6 | Day 41 – 50 | Enterprise Platform Engineering |
| Sprint 7 | Day 51 – 60 | Enterprise Client Delivery |

---

# 📖 Daily Format

Every day contains a realistic Jira ticket.

Each task includes

- Epic
- User Story
- Business Scenario
- Objectives
- Enterprise Tasks
- Acceptance Criteria
- Mini Challenge
- Interview Questions
- Deliverables
- Sprint Progress

Exactly like a real enterprise project.

---

# 📦 Dataset

This challenge uses the famous

**Olist Brazilian E-Commerce Dataset**

Tables include

- Customers
- Orders
- Order Items
- Products
- Sellers
- Payments
- Reviews
- Geolocation
- Product Categories

---

# 🎯 Skills You'll Gain

✅ Azure Databricks

✅ Apache Spark

✅ PySpark

✅ Spark SQL

✅ Delta Lake

✅ Unity Catalog

✅ Azure Data Factory

✅ Azure Data Lake Storage Gen2

✅ Azure SQL Database

✅ Git & GitHub

✅ Data Engineering Best Practices

✅ Medallion Architecture

✅ ETL & ELT

✅ Incremental Loading

✅ CDC

✅ Delta MERGE

✅ Data Quality Framework

✅ Workflow Orchestration

✅ CI/CD

✅ DevOps

✅ Power BI

✅ Production Deployment

✅ Production Support

✅ Incident Management

✅ Enterprise Architecture

✅ Client Communication

---

# 👨‍💻 Who Is This For?

This project is perfect for

- Data Engineers
- Azure Data Engineers
- Databricks Engineers
- Data Analysts
- BI Developers
- ETL Developers
- Cloud Engineers
- Software Engineers
- Students
- Professionals preparing for interviews

---

# 💼 Real-World Experience

By completing this repository you'll simulate the work of

- Azure Data Engineer
- Databricks Engineer
- Data Platform Engineer
- Analytics Engineer
- Cloud Data Engineer
- Big Data Engineer

You'll experience the complete project lifecycle from

```
Requirement Gathering
        │
        ▼
Architecture
        │
        ▼
Infrastructure
        │
        ▼
Development
        │
        ▼
Testing
        │
        ▼
CI/CD
        │
        ▼
Production Deployment
        │
        ▼
Production Support
        │
        ▼
Client Handover
```

---

# 🏆 Final Outcome

After completing this challenge, you will have

- ✅ A production-style Azure Databricks project
- ✅ A professional GitHub portfolio
- ✅ Hands-on Enterprise Data Engineering experience
- ✅ Practical Azure knowledge
- ✅ Real interview confidence
- ✅ A strong understanding of enterprise project delivery
- ✅ A reusable reference for future projects

---

# ⭐ Support the Project

If you found this repository helpful,

⭐ **Star this repository**

🍴 **Fork it**

📢 **Share it with others**

Your support helps more learners build real-world Data Engineering skills.

---

# 🤝 Contributing

Contributions are always welcome.

If you'd like to improve documentation, add enhancements, fix issues, or share ideas, feel free to open an Issue or submit a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to use it for learning, teaching, and personal portfolio projects.

---

# 🚀 Happy Learning!

> *"Don't just learn Databricks. Build it like a real Data Engineer."*

**Made with ❤️ for the Data Engineering Community**
