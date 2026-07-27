# Day 53 — Sprint 7

# 🚀 JIRA ID: OLIST-703

## Epic

**Enterprise Azure Infrastructure Provisioning**

---

# 📖 User Story

**As a Cloud Infrastructure Engineer,**

I want to provision a secure, scalable, and production-ready Azure environment,

so that the Data Engineering team can build, deploy, and operate enterprise-grade data pipelines.

---

# 🎯 Objective

Today you will build the complete **Azure Infrastructure** required for the Olist Enterprise Lakehouse.

By the end of today's assignment, you will learn how to:

- Design Azure Landing Zone
- Provision Azure Resources
- Configure Networking
- Create Enterprise Storage
- Deploy Azure Databricks
- Configure Azure Data Factory
- Secure Resources using Key Vault
- Enable Monitoring & Logging
- Configure Unity Catalog
- Prepare Infrastructure for CI/CD

---

# 🏢 Business Scenario

The Solution Architecture has been approved by the client's Architecture Review Board.

Development cannot begin until the Azure environment has been provisioned.

The infrastructure must support:

- Secure Data Storage
- Enterprise Networking
- Multi-Environment Deployment
- High Availability
- Monitoring
- Disaster Recovery
- Future Scalability

The client expects all Azure resources to follow enterprise naming conventions and governance standards.

Your responsibility is to provision the complete Azure environment before the first pipeline is developed.

---

# 📂 Infrastructure Inputs

```
Solution Architecture Document

Azure Naming Standards

Security Policies

Networking Standards

Resource Hierarchy

Governance Guidelines

Project Requirements
```

---

# 🏗 Expected Deliverables

```
Azure Subscription Structure

Resource Groups

Azure Data Lake Storage Gen2

Azure Databricks Workspace

Azure Data Factory

Azure Key Vault

Azure Monitor

Log Analytics Workspace

Unity Catalog

Infrastructure Documentation
```

---

# 🛠 Technologies

- Microsoft Azure
- Azure Databricks
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Key Vault
- Azure Monitor
- Azure Log Analytics
- Microsoft Entra ID
- Unity Catalog
- GitHub
- Azure RBAC

---

# 📋 Acceptance Criteria

✅ Azure resources provisioned

✅ Resource groups created

✅ Storage account configured

✅ Databricks workspace deployed

✅ Azure Data Factory deployed

✅ Key Vault configured

✅ Monitoring enabled

✅ Infrastructure documentation completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-703_Azure_Infrastructure
```

---

## Task 2

Create the Azure Resource Groups.

Example:

```
rg-olist-dev

rg-olist-test

rg-olist-uat

rg-olist-prod

rg-olist-monitoring

rg-olist-network
```

Document the purpose of each resource group.

---

## Task 3

Provision Azure Data Lake Storage Gen2.

Create the storage account.

Create containers:

```
raw

bronze

silver

gold

archive

logs

backups

configs
```

Enable:

- Hierarchical Namespace
- Secure Transfer
- Soft Delete
- Versioning

---

## Task 4

Deploy Azure Databricks.

Configure:

```
Workspace Name

Managed Resource Group

Region

Pricing Tier

Unity Catalog

Git Integration
```

Document all configuration choices.

---

## Task 5

Deploy Azure Data Factory.

Configure:

```
Managed Identity

GitHub Repository

Integration Runtime

Diagnostic Logs

Global Parameters
```

Validate connectivity with Databricks and ADLS.

---

## Task 6

Configure Azure Key Vault.

Create secrets for:

```
Storage Access

Database Credentials

API Keys

Service Principal

Application Secrets
```

Document the secret naming convention.

---

## Task 7

Configure Microsoft Entra ID & RBAC.

Create role assignments for:

```
Platform Administrator

Data Engineer

Data Analyst

Business User

Security Administrator
```

Apply the Principle of Least Privilege.

---

## Task 8

Configure Azure Monitor & Log Analytics.

Enable monitoring for:

```
Azure Databricks

Azure Data Factory

Storage Account

Key Vault

Azure Activity Logs
```

Create alerts for:

- Pipeline Failures
- Storage Errors
- Cluster Failures
- Authentication Failures

---

## Task 9

Configure Unity Catalog.

Create:

```
Catalog

Schemas

Managed Storage

External Locations

Volumes
```

Assign permissions to different teams.

---

## Task 10

Prepare Infrastructure for CI/CD.

Configure:

```
GitHub Repository

Branch Strategy

Environment Variables

Deployment Pipelines

Secrets Management

Release Strategy
```

Document the deployment workflow.

---

## Task 11

Validate the Infrastructure.

Verify:

- Resources deployed successfully.
- Storage is accessible.
- Databricks connects to ADLS.
- ADF connects to Databricks.
- Monitoring is active.
- RBAC permissions work correctly.
- Unity Catalog is operational.

---

## Task 12 ⭐

Create the **Infrastructure Deployment Guide**.

Include:

- Azure Resource Inventory
- Naming Standards
- Networking Configuration
- Storage Configuration
- Databricks Configuration
- ADF Configuration
- Key Vault Configuration
- Monitoring Setup
- RBAC Assignments
- Deployment Checklist

---

# 📚 Concepts Covered

- Azure Landing Zone
- Resource Groups
- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Data Factory
- Azure Key Vault
- Microsoft Entra ID
- Azure RBAC
- Azure Monitor
- Unity Catalog

---

# 💡 Mini Challenge

Complete the following tasks.

1. Create six resource groups.

2. Design an ADLS Gen2 container structure.

3. Deploy Azure Databricks.

4. Configure Azure Data Factory.

5. Create a Key Vault with five secrets.

6. Assign RBAC roles.

7. Enable Azure Monitor.

8. Configure Unity Catalog.

9. Validate infrastructure connectivity.

10. Prepare the Infrastructure Deployment Guide.

---

# 🧠 Real Interview Questions

### Q1

Why should enterprise Azure resources be separated into multiple resource groups?

---

### Q2

What is the purpose of Azure Key Vault in a Data Engineering project?

---

### Q3

How does Microsoft Entra ID improve security in Azure Databricks?

---

### Q4

What are the advantages of enabling Unity Catalog from the beginning of a project?

---

### Q5

Why should Azure Monitor and Log Analytics be configured before production deployment?

---

### Q6

How would you securely connect Azure Data Factory with Azure Databricks?

---

### Q7

Which Azure resources would you provision first when starting a new enterprise Data Engineering project?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Azure Infrastructure Notebook Created

✓ Resource Groups Provisioned

✓ Azure Data Lake Storage Gen2 Configured

✓ Azure Databricks Workspace Deployed

✓ Azure Data Factory Configured

✓ Azure Key Vault Implemented

✓ RBAC Permissions Assigned

✓ Azure Monitor & Log Analytics Enabled

✓ Unity Catalog Configured

✓ Infrastructure Deployment Guide Completed
```

---

# 🏁 End Goal

At the end of Day 53, you will have a fully provisioned Azure environment ready for enterprise Data Engineering development.

```
Azure Subscription
        │
        ▼
Resource Groups
        │
        ▼
Azure Data Lake Storage Gen2
        │
        ▼
Azure Databricks
        │
        ▼
Azure Data Factory
        │
        ▼
Unity Catalog
        │
        ▼
Azure Monitor
        │
        ▼
GitHub CI/CD
```

Your Azure platform is now enterprise-ready with secure networking, governed storage, monitored services, centralized secrets management, role-based access control, and integrated development workflows. This environment provides the foundation for building, testing, and deploying production-grade data pipelines.

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
| **Sprint 7** | **OLIST-703** | **Enterprise Azure Infrastructure Provisioning** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 54)

## 🚀 JIRA ID: OLIST-704

**Design the Enterprise Data Model & Database Architecture** by transforming business requirements into a scalable logical and physical data model. You'll design conceptual, logical, and physical ER models, define fact and dimension tables, implement Slowly Changing Dimensions (SCD), optimize partitioning and indexing strategies, establish naming conventions, and prepare the production database schema for the complete Olist Lakehouse solution.
