# Day 31 — Sprint 5

# 🚀 JIRA ID: OLIST-501

## Epic

**Production Deployment & Workflow Automation**

---

# 📖 User Story

**As a Data Engineering Lead,**

I want to orchestrate the complete Lakehouse pipeline using Azure Databricks Workflows,

so that Bronze, Silver, and Gold pipelines execute automatically in the correct order without manual intervention.

---

# 🎯 Objective

Today you will build a **Production Databricks Workflow** that orchestrates the complete Olist Lakehouse project.

By the end of today's assignment, you will learn how to:

- Create Databricks Workflows
- Build Multi-Task Jobs
- Configure Task Dependencies
- Schedule Automated Pipelines
- Configure Retries
- Handle Failures
- Monitor Production Jobs

---

# 🏢 Business Scenario

The Olist data platform currently requires engineers to execute every notebook manually.

This process is:

- Time-consuming
- Error-prone
- Difficult to monitor
- Not suitable for production

The company wants a fully automated pipeline that executes every stage in sequence.

Every day at midnight, the system should:

1. Load Bronze data
2. Transform Silver data
3. Build Gold analytics
4. Refresh reporting tables

Your responsibility is to automate the entire Lakehouse using **Azure Databricks Workflows**.

---

# 📂 Source Notebooks

```
Bronze Layer

OLIST-101
...
OLIST-109

Silver Layer

OLIST-201
...
OLIST-209

Gold Layer

OLIST-301
...
OLIST-310

Reporting Layer

OLIST-401

OLIST-402
```

---

# 🏗 Deliverables

```
Databricks Workflow

Task Dependency Graph

Job Configuration

Execution Schedule

Workflow Documentation
```

---

# 🛠 Technologies

- Azure Databricks
- Databricks Workflows
- Delta Lake
- PySpark
- Spark SQL
- Azure Monitor (Optional)

---

# 📋 Acceptance Criteria

✅ Workflow created

✅ All notebooks added

✅ Task dependencies configured

✅ Retry policy configured

✅ Schedule created

✅ Workflow executed successfully

✅ Monitoring enabled

---

# 🧑‍💻 Tasks

## Task 1

Create a Databricks Job named

```
OLIST_Production_Pipeline
```

---

## Task 2

Create Job Tasks.

Add every notebook from:

```
Bronze

Silver

Gold

Reporting
```

---

## Task 3

Configure Task Dependencies.

Example execution order:

```
Bronze

↓

Silver

↓

Gold

↓

Reporting
```

Ensure no Gold notebook starts until all Silver notebooks finish successfully.

---

## Task 4

Configure Compute.

Choose an appropriate compute option.

Examples:

```
Existing Cluster

Job Cluster

Serverless (if available)
```

Document why your selected option is suitable.

---

## Task 5

Configure Retry Policy.

Examples:

```
Retry Attempts

Retry Interval

Timeout

Maximum Concurrent Runs
```

Define production-ready values.

---

## Task 6

Configure Notifications.

Examples:

```
Success Notification

Failure Notification

Skipped Tasks

Timeout Alerts
```

Document the notification settings.

---

## Task 7

Create a Schedule.

Example:

```
Daily

12:00 AM
```

Configure:

- Time Zone
- Cron Expression (optional)
- Manual Trigger
- Scheduled Trigger

---

## Task 8

Run the Workflow.

Monitor:

- Execution Time
- Task Status
- Failed Tasks
- Successful Tasks
- Total Duration

Capture screenshots of the execution graph.

---

## Task 9

Handle Failures.

Simulate a notebook failure.

Verify:

- Workflow stops appropriately.
- Dependent tasks are skipped.
- Retry policy executes.
- Failure notification is generated.

Document your observations.

---

## Task 10

Review Job History.

Analyse:

- Previous Runs
- Execution Duration
- Failed Runs
- Retry Attempts
- Task Logs

Document your findings.

---

## Task 11

Optimize Workflow.

Examples:

- Parallelize independent Bronze tasks.
- Parallelize independent Silver tasks.
- Minimize cluster startup time.
- Reduce unnecessary notebook execution.
- Improve overall pipeline efficiency.

Explain your optimization decisions.

---

## Task 12 ⭐

Create Workflow Documentation.

Include:

- Workflow Architecture
- Task Dependency Diagram
- Compute Configuration
- Retry Policy
- Schedule
- Notifications
- Monitoring Strategy
- Failure Recovery Process
- Best Practices

---

# 📚 Concepts Covered

- Databricks Workflows
- Multi-Task Jobs
- Job Scheduling
- Task Dependencies
- Retry Policies
- Production Automation
- Pipeline Monitoring
- Workflow Optimization

---

# 💡 Mini Challenge

Complete the following tasks.

1. Create a Databricks Workflow.

2. Add all Bronze notebooks.

3. Configure parallel execution where possible.

4. Configure sequential execution between layers.

5. Configure retry policy.

6. Configure failure notifications.

7. Schedule the workflow.

8. Execute the workflow.

9. Review execution logs.

10. Document the workflow architecture.

---

# 🧠 Real Interview Questions

### Q1

What is the difference between a Databricks Job and a Databricks Workflow?

---

### Q2

Why are task dependencies important in ETL pipelines?

---

### Q3

When would you use an Existing Cluster instead of a Job Cluster?

---

### Q4

How do retry policies improve production reliability?

---

### Q5

How would you troubleshoot a failed Databricks Workflow?

---

# 🎯 Deliverables

By the end of today you should have:

```
✓ Production Workflow Created

✓ Multi-Task Job Configured

✓ Task Dependencies Implemented

✓ Compute Configured

✓ Retry Policy Added

✓ Notifications Configured

✓ Schedule Created

✓ Workflow Executed Successfully

✓ Monitoring Verified

✓ Workflow Documentation Completed
```

---

# 🏁 End Goal

At the end of Day 31, your complete Lakehouse solution will be fully automated.

```
Daily Schedule
        │
        ▼
 Databricks Workflow
        │
        ▼
 Bronze Layer
        │
        ▼
 Silver Layer
        │
        ▼
 Gold Layer
        │
        ▼
 Reporting Layer
        │
        ▼
 Executive Dashboard
```

The entire pipeline now runs automatically with monitoring, retries, logging, and task dependencies—just like a production-grade enterprise Data Engineering solution.

---

# 📈 Sprint Progress

| Sprint | JIRA ID | Task | Status |
|---------|----------|------|--------|
| Sprint 1 | OLIST-101 → OLIST-109 | Bronze Layer | ✅ Complete |
| Sprint 2 | OLIST-201 → OLIST-209 | Silver Layer | ✅ Complete |
| Sprint 3 | OLIST-301 → OLIST-310 | Gold Analytics Layer | ✅ Complete |
| Sprint 4 | OLIST-401 → OLIST-402 | Reporting Data Mart & Power BI | ✅ Complete |
| **Sprint 5** | **OLIST-501** | **Deploy Production Databricks Workflow** | 🚧 In Progress |

---

# 🔜 Tomorrow (Day 32)

## 🚀 JIRA ID: OLIST-502

**Implement Incremental Data Loading & Change Data Capture (CDC)** by upgrading your Bronze and Silver pipelines to process only new and changed records. You'll learn watermarking, Delta Lake `MERGE`, upserts, deletes, Slowly Changing Dimensions (SCD Type 1 & Type 2), idempotent pipelines, and production-grade incremental ETL strategies used in enterprise Data Engineering.
