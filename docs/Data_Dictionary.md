# 📖 Data Dictionary

## Overview

The **Data Dictionary** provides detailed information about every dataset used in this project. It explains the purpose of each table, its columns, primary keys, foreign keys, and how the table is used throughout the Medallion Architecture.

---

# Dataset Summary

| Dataset | Description | Primary Key |
|----------|-------------|-------------|
| olist_customers_dataset | Customer master information | customer_id |
| olist_orders_dataset | Order information | order_id |
| olist_order_items_dataset | Products purchased in each order | order_id + order_item_id |
| olist_products_dataset | Product master information | product_id |
| olist_sellers_dataset | Seller master information | seller_id |
| olist_order_payments_dataset | Payment details | order_id + payment_sequential |
| olist_order_reviews_dataset | Customer reviews | review_id |
| product_category_name_translation | Product category translation | product_category_name |
| olist_geolocation_dataset | Postal code location information | No unique primary key |

---

# 1. olist_customers_dataset

## Description

Contains customer master information.

### Primary Key

```
customer_id
```

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| customer_id | String | Unique customer identifier |
| customer_unique_id | String | Permanent customer identifier |
| customer_zip_code_prefix | Integer | ZIP code prefix |
| customer_city | String | Customer city |
| customer_state | String | Customer state |

---

# 2. olist_orders_dataset

## Description

Contains all order transactions.

### Primary Key

```
order_id
```

### Foreign Key

```
customer_id
```

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| order_id | String | Unique order ID |
| customer_id | String | Customer identifier |
| order_status | String | Order status |
| order_purchase_timestamp | Timestamp | Purchase time |
| order_approved_at | Timestamp | Payment approval time |
| order_delivered_carrier_date | Timestamp | Carrier pickup date |
| order_delivered_customer_date | Timestamp | Delivery date |
| order_estimated_delivery_date | Timestamp | Estimated delivery |

---

# 3. olist_order_items_dataset

## Description

Contains products purchased within each order.

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

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| order_id | String | Order identifier |
| order_item_id | Integer | Item sequence |
| product_id | String | Product identifier |
| seller_id | String | Seller identifier |
| shipping_limit_date | Timestamp | Shipping deadline |
| price | Decimal | Product price |
| freight_value | Decimal | Shipping charge |

---

# 4. olist_products_dataset

## Description

Contains product information.

### Primary Key

```
product_id
```

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| product_id | String | Product identifier |
| product_category_name | String | Product category |
| product_name_length | Integer | Product name length |
| product_description_length | Integer | Description length |
| product_photos_qty | Integer | Number of images |
| product_weight_g | Integer | Weight (grams) |
| product_length_cm | Integer | Length |
| product_height_cm | Integer | Height |
| product_width_cm | Integer | Width |

---

# 5. olist_sellers_dataset

## Description

Contains seller information.

### Primary Key

```
seller_id
```

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| seller_id | String | Seller identifier |
| seller_zip_code_prefix | Integer | ZIP prefix |
| seller_city | String | Seller city |
| seller_state | String | Seller state |

---

# 6. olist_order_payments_dataset

## Description

Contains payment information for every order.

### Composite Primary Key

```
order_id

payment_sequential
```

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| order_id | String | Order identifier |
| payment_sequential | Integer | Payment sequence |
| payment_type | String | Payment method |
| payment_installments | Integer | Number of installments |
| payment_value | Decimal | Payment amount |

---

# 7. olist_order_reviews_dataset

## Description

Contains customer reviews.

### Primary Key

```
review_id
```

### Foreign Key

```
order_id
```

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| review_id | String | Review identifier |
| order_id | String | Order identifier |
| review_score | Integer | Rating (1–5) |
| review_comment_title | String | Review title |
| review_comment_message | String | Review message |
| review_creation_date | Timestamp | Review date |
| review_answer_timestamp | Timestamp | Response timestamp |

---

# 8. product_category_name_translation

## Description

Maps Portuguese category names to English.

### Primary Key

```
product_category_name
```

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| product_category_name | String | Portuguese category |
| product_category_name_english | String | English category |

---

# 9. olist_geolocation_dataset

## Description

Contains postal code geographical information.

### Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| geolocation_zip_code_prefix | Integer | ZIP code prefix |
| geolocation_lat | Decimal | Latitude |
| geolocation_lng | Decimal | Longitude |
| geolocation_city | String | City |
| geolocation_state | String | State |

---

# Relationship Summary

| Parent Table | Child Table | Relationship |
|--------------|-------------|--------------|
| customers | orders | One-to-Many |
| orders | order_items | One-to-Many |
| orders | order_payments | One-to-Many |
| orders | order_reviews | One-to-Many |
| products | order_items | One-to-Many |
| sellers | order_items | One-to-Many |
| product_category_translation | products | One-to-Many |

---

# Medallion Mapping

| Source | Bronze | Silver | Gold |
|----------|---------|---------|------|
| Customers | bronze.customers | silver.customers | gold.customer_analytics |
| Orders | bronze.orders | silver.orders | gold.sales_summary |
| Order Items | bronze.order_items | silver.order_items | gold.product_performance |
| Products | bronze.products | silver.products | gold.product_performance |
| Sellers | bronze.sellers | silver.sellers | gold.supplier_performance |
| Payments | bronze.payments | silver.payments | gold.payment_analysis |
| Reviews | bronze.reviews | silver.reviews | gold.customer_satisfaction |
| Geolocation | bronze.geolocation | silver.geolocation | gold.regional_sales |

---

## Notes

- Source datasets remain unchanged in the **Raw** layer.
- Bronze stores data as ingested.
- Silver applies cleansing, validation, and standardization.
- Gold provides curated datasets optimized for analytics and reporting.
