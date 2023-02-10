import os

main_path = r"C:\Users\Administrator\Desktop"
customersPath = os.path.join(main_path, "raw_data", "olist_customers_dataset.csv")
geolocationPath = os.path.join(main_path, "raw_data", "olist_geolocation_dataset.csv")
order_itemsPath = os.path.join(main_path, "raw_data", "olist_order_items_dataset.csv")
order_paymentPath = os.path.join(main_path, "raw_data", "olist_order_payments_dataset.csv")
order_reviewsPath = os.path.join(main_path, "raw_data", "olist_order_reviews_dataset.csv")
ordersPath = os.path.join(main_path, "raw_data", "olist_orders_dataset.csv")
productsPath = os.path.join(main_path, "raw_data", "olist_products_dataset.csv")
sellersPath = os.path.join(main_path, "raw_data", "olist_sellers_dataset.csv")

customersPK = ""
geolocationPK = "geolocation_zip_code_prefix"
