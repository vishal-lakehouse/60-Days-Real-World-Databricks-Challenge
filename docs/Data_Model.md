# 🗂️ Data Model

## Overview

This document describes the logical data model used throughout the **60 Days Real-World Databricks Challenge**.

The project is based on the **Olist E-Commerce Dataset**, which represents an online marketplace connecting customers, sellers, products, payments, and reviews.

The data model follows a **normalized transactional design** in the Source and Bronze layers and gradually evolves into an **analytics-ready dimensional model** in the Gold layer.

---

# Source System Data Model

```
Customers
    │
    │ customer_id
    ▼
Orders
    │
    ├──────────────┐
    │              │
    ▼              ▼
Order Items     Payments
    │
    │
    ├──────────────┐
    │              │
    ▼              ▼
Products      Sellers

Orders
   │
   ▼
Reviews

Products
   │
   ▼
Category Translation

Customers
Sellers
      │
      ▼
Geolocation
```

---

# Business Entities

The Olist dataset contains nine primary business entities.

| Entity | Description |
|----------|-------------|
| Customers | People purchasing products |
| Orders | Customer purchases |
| Order Items | Individual products within an order |
| Products | Product master data |
| Sellers | Marketplace sellers |
| Payments | Payment transactions |
| Reviews | Customer feedback |
| Product Categories | Category translation table |
| Geolocation | ZIP code location information |

---

# Entity Details

---

# Customers

## Purpose

Stores customer master information.

### Primary Key

```
customer_id
```

### Relationships

```
Customers
      │
      └────────► Orders
```

### Cardinality

```
1 Customer

↓

Many Orders
```

---

# Orders

## Purpose

Stores every order placed by customers.

### Primary Key

```
order_id
```

### Foreign Keys

```
customer_id
```

### Relationships

```
Orders

├────► Order Items

├────► Payments

└────► Reviews
```

### Cardinality

```
One Order

↓

Many Order Items

↓

Many Payments

↓

Many Reviews
```

---

# Order Items

## Purpose

Stores every product purchased within an order.

### Composite Primary Key

```
order_id

order_item_id
```

### Foreign Keys

```
order_id

product_id

seller_id
```

### Relationships

```
Orders

↓

Order Items

↓

Products

↓

Sellers
```

---

# Products

## Purpose

Stores product master information.

### Primary Key

```
product_id
```

### Relationship

```
Products

↓

Order Items
```

---

# Sellers

## Purpose

Stores seller information.

### Primary Key

```
seller_id
```

### Relationship

```
Sellers

↓

Order Items
```

---

# Payments

## Purpose

Stores payment information.

### Composite Primary Key

```
order_id

payment_sequential
```

### Relationship

```
Orders

↓

Payments
```

---

# Reviews

## Purpose

Stores customer ratings and feedback.

### Primary Key

```
review_id
```

### Relationship

```
Orders

↓

Reviews
```

---

# Product Categories

## Purpose

Maps Portuguese product categories to English.

### Primary Key

```
product_category_name
```

### Relationship

```
Product Categories

↓

Products
```

---

# Geolocation

## Purpose

Stores location information based on ZIP code prefixes.

### Used By

```
Customers

Sellers
```

---

# Logical Data Model

```
                    Customers
                        │
                        │
                        ▼
                    Orders
            ┌────────┼─────────┐
            ▼        ▼         ▼
      Order Items Payments Reviews
            │
      ┌─────┴─────┐
      ▼           ▼
 Products      Sellers
      │
      ▼
Category Translation

Customers
      │
      ▼
Geolocation
      ▲
      │
Sellers
```

---

# Medallion Data Model

## Bronze Layer

Stores raw data exactly as received.

```
bronze.customers

bronze.orders

bronze.order_items

bronze.products

bronze.sellers

bronze.payments

bronze.reviews

bronze.geolocation

bronze.product_category_translation
```

No transformations are applied.

---

## Silver Layer

Stores cleansed and standardized datasets.

Typical transformations include:

- Duplicate removal
- Null handling
- Data type corrections
- Schema validation
- Standardized naming
- Business rule validation

Tables

```
silver.customers

silver.orders

silver.order_items

silver.products

silver.sellers

silver.payments

silver.reviews

silver.geolocation

silver.product_categories
```

---

## Gold Layer

Contains analytics-ready datasets.

```
gold.sales_summary

gold.customer_analytics

gold.product_performance

gold.payment_analysis

gold.supplier_performance

gold.customer_satisfaction

gold.inventory_snapshot
```

---

# Business Process Flow

```
Customer

↓

Places Order

↓

Order Created

↓

Products Added

↓

Payment Processed

↓

Seller Ships Product

↓

Customer Receives Product

↓

Customer Writes Review

↓

Business Analytics
```

---

# Primary Keys

| Table | Primary Key |
|---------|-------------|
| Customers | customer_id |
| Orders | order_id |
| Order Items | order_id + order_item_id |
| Products | product_id |
| Sellers | seller_id |
| Payments | order_id + payment_sequential |
| Reviews | review_id |
| Product Categories | product_category_name |

---

# Foreign Keys

| Child Table | Foreign Key | Parent Table |
|--------------|-------------|--------------|
| Orders | customer_id | Customers |
| Order Items | order_id | Orders |
| Order Items | product_id | Products |
| Order Items | seller_id | Sellers |
| Payments | order_id | Orders |
| Reviews | order_id | Orders |
| Products | product_category_name | Product Categories |

---

# Gold Layer Business Model

```
                   Gold Layer

              Sales Analytics

                     │

        ┌────────────┼────────────┐

        ▼            ▼            ▼

 Customer KPI   Product KPI   Payment KPI

        ▼            ▼            ▼

 Executive Dashboards & BI Reports
```

---

# Summary

The project begins with a normalized transactional data model in the Source and Bronze layers. Through the Medallion Architecture, the data is progressively transformed into trusted, standardized, and analytics-ready datasets in the Silver and Gold layers. This design supports scalable data engineering workflows and efficient reporting for business intelligence.
