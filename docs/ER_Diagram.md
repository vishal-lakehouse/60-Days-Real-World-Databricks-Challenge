# ABC Retail Ltd. - Source System ER Diagram

```mermaid
erDiagram

    olist_customers_dataset ||--o{ olist_orders_dataset : places

    olist_orders_dataset ||--o{ olist_order_items_dataset : contains

    olist_orders_dataset ||--o{ olist_order_payments_dataset : paid_by

    olist_orders_dataset ||--o{ olist_order_reviews_dataset : receives

    olist_products_dataset ||--o{ olist_order_items_dataset : ordered

    olist_sellers_dataset ||--o{ olist_order_items_dataset : sells

    product_category_name_translation ||--o{ olist_products_dataset : translates

    olist_geolocation_dataset ||--o{ olist_customers_dataset : customer_location

    olist_geolocation_dataset ||--o{ olist_sellers_dataset : seller_location



    olist_customers_dataset {

        string customer_id PK

        string customer_unique_id

        int customer_zip_code_prefix

        string customer_city

        string customer_state

    }



    olist_orders_dataset {

        string order_id PK

        string customer_id FK

        string order_status

        datetime order_purchase_timestamp

        datetime order_approved_at

        datetime order_delivered_carrier_date

        datetime order_delivered_customer_date

        datetime order_estimated_delivery_date

    }



    olist_order_items_dataset {

        string order_id FK

        int order_item_id

        string product_id FK

        string seller_id FK

        datetime shipping_limit_date

        decimal price

        decimal freight_value

    }



    olist_products_dataset {

        string product_id PK

        string product_category_name

        int product_name_length

        int product_description_length

        int product_photos_qty

        int product_weight_g

        int product_length_cm

        int product_height_cm

        int product_width_cm

    }



    olist_sellers_dataset {

        string seller_id PK

        int seller_zip_code_prefix

        string seller_city

        string seller_state

    }



    olist_order_payments_dataset {

        string order_id FK

        int payment_sequential

        string payment_type

        int payment_installments

        decimal payment_value

    }



    olist_order_reviews_dataset {

        string review_id PK

        string order_id FK

        int review_score

        string review_comment_title

        string review_comment_message

        datetime review_creation_date

        datetime review_answer_timestamp

    }



    product_category_name_translation {

        string product_category_name PK

        string product_category_name_english

    }



    olist_geolocation_dataset {

        int geolocation_zip_code_prefix

        decimal geolocation_lat

        decimal geolocation_lng

        string geolocation_city

        string geolocation_state

    }

```
