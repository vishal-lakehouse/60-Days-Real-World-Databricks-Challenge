# Day 36 — Sprint 5

# 🚀 JIRA ID: OLIST-506

## Epic

**Enterprise Security & Governance**

---

# 📖 User Story

**As a Cloud Security Engineer,**

I want to secure the Databricks Lakehouse using enterprise security best practices,

so that sensitive business data is protected while allowing controlled access for different teams and users.

---

# 🎯 Objective

Today you will implement **Enterprise Security** for your Lakehouse by securing credentials, managing user access, protecting sensitive data, and enforcing governance policies.

By the end of today's assignment, you will learn how to:

- Secure Secrets using Databricks Secret Scopes
- Integrate Azure Key Vault
- Configure Service Principals
- Implement RBAC
- Configure Unity Catalog Permissions
- Apply Row-Level Security (RLS)
- Apply Column-Level Security (CLS)
- Build a Secure Enterprise Lakehouse

---

# 🏢 Business Scenario

The Olist Lakehouse is now running in Production.

Multiple teams access the platform:

- Data Engineers
- Data Analysts
- Data Scientists
- Business Users
- Executives

Currently, everyone has unrestricted access to all data.

This creates several security risks:

- Sensitive customer information is exposed.
- Credentials are stored inside notebooks.
- Users have excessive permissions.
- No governance policy exists.

The Security Team wants to implement enterprise-grade access control and credential management.

Your responsibility is to secure the Lakehouse using Azure Databricks security best practices.

---

# 📂 Protected Assets

```
Azure Storage

Azure SQL Database

Delta Tables

Databricks Workflows

Power BI

Unity Catalog
```

---

# 🏗 Target Deliverables

```
Secret Scope

Azure Key Vault Integration

RBAC Configuration

Unity Catalog Permissions

Security Documentation
```

---

# 🛠 Technologies

- Azure Databricks
- Azure Key Vault
- Databricks Secret Scopes
- Unity Catalog
- Azure Active Directory (Microsoft Entra ID)
- Service Principals
- Delta Lake

---

# 📋 Acceptance Criteria

✅ Secret Scope created

✅ Azure Key Vault integrated

✅ Service Principal configured

✅ RBAC implemented

✅ Unity Catalog permissions configured

✅ Row-Level Security demonstrated

✅ Security documentation completed

---

# 🧑‍💻 Tasks

## Task 1

Create a notebook named

```
OLIST-506_Enterprise_Security
```

---

## Task 2

Identify sensitive information within the project.

Examples:

```
Storage Account Keys

Database Passwords

API Tokens

Client Secrets

Personal Customer Information
```

Classify each item according to its sensitivity.

---

## Task 3

Create a Databricks Secret Scope.

Store credentials such as:

```
Storage Account Key

Database Password

API Token

Client Secret
```

Verify that notebooks retrieve secrets securely instead of using hard-coded values.

---

## Task 4

Integrate Azure Key Vault.

Configure Databricks to access secrets from:

```
Azure Key Vault
```

Document:

- Vault Name
- Secret Names
- Access Configuration

Explain why Azure Key Vault is preferred over storing secrets inside notebooks.

---

## Task 5

Configure a Service Principal.

Grant the Service Principal access to:

```
Azure Storage

Databricks Workspace

Unity Catalog
```

Document:

- Authentication Method
- Required Roles
- Permission Scope

---

## Task 6

Implement Role-Based Access Control (RBAC).

Create sample roles such as:

```
Data Engineer

Data Analyst

Data Scientist

Business User

Administrator
```

Assign appropriate permissions for each role.

---

## Task 7

Configure Unity Catalog Permissions.

Grant access at different levels:

```
Catalog

Schema

Table

View
```

Examples:

```
SELECT

MODIFY

CREATE

USE SCHEMA

USE CATALOG
```

Verify permission inheritance.

---

## Task 8

Implement Data Security.

Demonstrate:

```
Row-Level Security (RLS)

Column-Level Security (CLS)

Dynamic Data Masking
```

Example:

- Analysts can view aggregated sales.
- Only Administrators can view customer email addresses.
- Executives can access all records.

Document your security logic.

---

## Task 9

Review Audit Logs.

Capture security-related events such as:

- Login Attempts
- Permission Changes
- Failed Access Requests
- Secret Access
- Table Access

Explain how audit logs help during security investigations.

---

## Task 10

Perform Security Validation.

Verify:

- Secrets are never hard-coded.
- Unauthorized users cannot access protected data.
- RBAC works correctly.
- Unity Catalog permissions are enforced.
- Sensitive columns are masked.

---

## Task 11

Review Security Best Practices.

Document recommendations for:

- Secret Rotation
- Least Privilege Access
- Multi-Factor Authentication (MFA)
- Credential Management
- Periodic Access Reviews
- Encryption at Rest
- Encryption in Transit

---

## Task 12 ⭐

Create Enterprise Security Documentation.

Include:

- Security Architecture
- Secret Management
- Azure Key Vault Integration
- Service Principal Configuration
- RBAC Design
- Unity Catalog Permissions
- Row-Level Security
- Column-Level Security
- Audit Logging
- Security Best Practices

---

# 📚 Concepts Covered

- Azure Key Vault
- Databricks Secret Scopes
- Service Principals
- Microsoft Entra ID
- RBAC
- Unity Catalog
- Row-Level Security
- Column-Level Security
- Dynamic Data Masking
- Security Governance

---

# 💡 Mini Challenge

Complete the following tasks.

1. Create a Secret Scope.

2. Store a Storage Account Key securely.

3. Retrieve a secret inside a notebook.

4. Configure Azure Key Vault integration.

5. Create a Service Principal.

6. Grant SELECT permission to Analysts.

7. Restrict UPDATE permission to Data Engineers.

8. Mask customer email addresses for Business Users.

9. Verify Unity Catalog permissions.

10. Draw the enterprise security architecture.

---

# 🧠 Real Interview Questions

### Q1

Why should secrets never be hard-coded inside Databricks notebooks?

---

### Q2

What is the difference between Azure Key Vault and Databricks Secret Scopes?

---

### Q3

What is a Service Principal, and why is it used?

---

### Q4

Explain Role-Based Access Control (RBAC).

---

### Q5

How does Unity Catalog improve data governance?

---

### Q6

What is the difference between Row-Level Security and Column-Level Security?

---

### Q7

How would you secure a production Databricks environment?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Enterprise Security Notebook Created

✓ Secret Scope Configured

✓ Azure Key Vault Integrated

✓ Service Principal Configured

✓ RBAC Implemented

✓ Unity Catalog Permissions Applied

✓ Row-Level Security Demonstrated

✓ Column-Level Security Demonstrated

✓ Security Validation Completed

✓ Enterprise Security Documentation Created
```

---

# 🏁 End Goal

At the end of Day 36, your Lakehouse will be protected using enterprise-grade security controls.

```
Users
      │
      ▼
Microsoft Entra ID
      │
      ▼
Role-Based Access Control
      │
      ▼
Unity Catalog Permissions
      │
      ▼
Azure Databricks
      │
      ▼
Secret Scopes
      │
      ▼
Azure Key Vault
      │
      ▼
Secure Delta Lake
```

Your Lakehouse now follows enterprise security best practices with secure credential management, governed data access, centralized secret storage, and fine-grained permissions, making it suitable for production environments handling sensitive business data.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| Sprint 3 | OLIST-301 → OLIST-310 | Gold Analytics Layer | ✅ Complete |
| Sprint 4 | OLIST-401 → OLIST-402 | Reporting Data Mart & Power BI | ✅ Complete |
| Sprint 5 | OLIST-501 | Deploy Production Databricks Workflow | ✅ Complete |
| Sprint 5 | OLIST-502 | Implement Incremental Loading & CDC | ✅ Complete |
| Sprint 5 | OLIST-503 | Optimize Delta Lake Performance | ✅ Complete |
| Sprint 5 | OLIST-504 | Implement Data Quality Framework & Pipeline Monitoring | ✅ Complete |
| Sprint 5 | OLIST-505 | Implement CI/CD for Databricks Pipelines | ✅ Complete |
| **Sprint 5** | **OLIST-506** | **Implement Secrets Management & Enterprise Security** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 37)

## 🚀 JIRA ID: OLIST-507

**Implement Delta Live Tables (DLT) & Data Pipeline Expectations** by rebuilding parts of your Bronze and Silver pipelines using Delta Live Tables. You'll create declarative ETL pipelines, enforce data quality expectations, quarantine invalid records, automate dependency management, and monitor pipeline health using DLT—one of the most in-demand enterprise features in the Databricks Lakehouse Platform.
