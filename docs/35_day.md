# Day 35 — Sprint 5

# 🚀 JIRA ID: OLIST-505

## Epic

**DevOps & CI/CD Automation**

---

# 📖 User Story

**As a DevOps Engineer,**

I want to automate the deployment of Databricks notebooks and workflows,

so that code changes are tested, version-controlled, and promoted safely across Development, Test, and Production environments.

---

# 🎯 Objective

Today you will implement a **CI/CD Pipeline** for your Databricks Lakehouse project.

By the end of today's assignment, you will learn how to:

- Integrate Databricks with Git
- Implement CI/CD
- Create Deployment Pipelines
- Manage Multiple Environments
- Perform Automated Testing
- Deploy Databricks Assets
- Follow Enterprise DevOps Best Practices

---

# 🏢 Business Scenario

The Olist Data Engineering team currently deploys notebooks manually into production.

This approach creates several problems:

- Human errors during deployment
- No automated testing
- Difficult rollback process
- No approval workflow
- Inconsistent production deployments

The Engineering Manager wants an automated CI/CD process that validates code before deploying it into Production.

Your responsibility is to build a production-ready deployment pipeline.

---

# 📂 Source Assets

```
Databricks Notebooks

Databricks Workflows

Delta Tables

Git Repository
```

---

# 🏗 Target Deliverables

```
CI/CD Pipeline

Deployment Strategy

Environment Configuration

Release Documentation
```

---

# 🛠 Technologies

- Azure Databricks
- Git
- GitHub
- GitHub Actions (or Azure DevOps)
- Databricks CLI
- Databricks Asset Bundles
- YAML Pipelines

---

# 📋 Acceptance Criteria

✅ Git repository connected

✅ Branch strategy implemented

✅ CI/CD pipeline created

✅ Automated testing configured

✅ Deployment automation implemented

✅ Environment promotion completed

✅ Documentation created

---

# 🧑‍💻 Tasks

## Task 1

Connect your Databricks Workspace to Git.

Use either:

```
GitHub

OR

Azure DevOps Repos
```

Verify that notebooks are version-controlled.

---

## Task 2

Create a Branch Strategy.

Implement branches such as:

```
main

develop

feature/*
```

Document the purpose of each branch.

---

## Task 3

Create Environment Configuration.

Define separate environments:

```
Development

Testing

Production
```

Document the configuration differences for each environment.

---

## Task 4

Create a CI Pipeline.

Configure the pipeline to automatically:

- Pull the latest code.
- Validate notebook structure.
- Run code quality checks.
- Execute unit tests (where applicable).
- Verify deployment artifacts.

Document every pipeline stage.

---

## Task 5

Create a CD Pipeline.

Automatically deploy:

```
Databricks Notebooks

Workflows

Configurations
```

to the selected environment after successful validation.

---

## Task 6

Implement Approval Workflow.

Before deploying to Production:

- Require manual approval.
- Verify successful Testing deployment.
- Review deployment summary.

Document the release process.

---

## Task 7

Implement Environment Promotion.

Deploy notebooks in sequence:

```
Development

↓

Testing

↓

Production
```

Ensure production deployment only occurs after successful validation.

---

## Task 8

Implement Versioning.

Tag releases using semantic versioning.

Example:

```
v1.0.0

v1.1.0

v2.0.0
```

Document your versioning strategy.

---

## Task 9

Implement Rollback Strategy.

Define how to:

- Restore previous notebook versions.
- Roll back failed deployments.
- Restore previous workflow configurations.

Document rollback procedures.

---

## Task 10

Validate the Deployment.

Verify:

- All notebooks deployed successfully.
- Workflow configuration remains unchanged.
- Git history reflects deployment.
- Production environment matches the release version.

---

## Task 11

Monitor Deployment Pipeline.

Capture:

- Build Duration
- Deployment Duration
- Pipeline Status
- Failed Stages
- Successful Deployments

Document deployment metrics.

---

## Task 12 ⭐

Create CI/CD Documentation.

Include:

- Git Branch Strategy
- CI Pipeline
- CD Pipeline
- Deployment Flow
- Environment Configuration
- Approval Process
- Rollback Strategy
- Versioning Strategy
- Best Practices

---

# 📚 Concepts Covered

- CI/CD
- Git Integration
- GitHub Actions
- Azure DevOps Pipelines
- Databricks Asset Bundles
- Environment Promotion
- Release Management
- Version Control
- Deployment Automation

---

# 💡 Mini Challenge

Complete the following tasks.

1. Connect Databricks to GitHub.

2. Create a `feature/new_pipeline` branch.

3. Build a CI workflow using GitHub Actions or Azure DevOps.

4. Validate notebook changes before deployment.

5. Deploy notebooks to the Development environment.

6. Promote changes to the Testing environment.

7. Configure Production approval.

8. Tag the release as `v1.0.0`.

9. Simulate a rollback after a failed deployment.

10. Draw the complete CI/CD architecture.

---

# 🧠 Real Interview Questions

### Q1

What is CI/CD, and why is it important in Data Engineering?

---

### Q2

What is the difference between Continuous Integration and Continuous Deployment?

---

### Q3

Why should Development, Testing, and Production environments be separated?

---

### Q4

What are Databricks Asset Bundles, and how do they simplify deployments?

---

### Q5

How would you roll back a failed production deployment?

---

### Q6

Why is Git version control important for Databricks projects?

---

### Q7

How would you automate notebook deployments using GitHub Actions?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Git Repository Connected

✓ Branch Strategy Implemented

✓ CI Pipeline Created

✓ CD Pipeline Created

✓ Development Environment Configured

✓ Testing Environment Configured

✓ Production Deployment Configured

✓ Release Version Tagged

✓ Rollback Strategy Documented

✓ Complete CI/CD Documentation Created
```

---

# 🏁 End Goal

At the end of Day 35, your Lakehouse project will support enterprise-grade DevOps practices.

```
Developer
      │
      ▼
Git Repository
      │
      ▼
Continuous Integration
      │
      ▼
Automated Validation
      │
      ▼
Development Environment
      │
      ▼
Testing Environment
      │
      ▼
Approval Process
      │
      ▼
Production Deployment
      │
      ▼
Azure Databricks
```

Your Databricks project is now fully integrated with a CI/CD pipeline, enabling automated testing, controlled deployments, version management, and safe promotion across environments—just like enterprise Data Engineering teams.

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
| **Sprint 5** | **OLIST-505** | **Implement CI/CD for Databricks Pipelines** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 36)

## 🚀 JIRA ID: OLIST-506

**Implement Secrets Management & Enterprise Security** by securing your Lakehouse with Azure Key Vault, Databricks Secret Scopes, service principals, RBAC, Unity Catalog permissions, data masking, row-level security, column-level security, and credential rotation. You'll learn how enterprise Data Engineering teams protect sensitive data and manage secure access across production environments.
