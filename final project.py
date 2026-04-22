import pandas as pd
import numpy as np

#  ----------------load dataset
customers = pd.read_csv("customers_dirty_2019_2025.csv")
orders = pd.read_csv("orders_dirty_2019_2025.csv")
products = pd.read_csv("products_dirty_2019_2025.csv")

# ----------------- handle missing values
# print(customers.isnull().sum())
# print(orders.isnull().sum())
# print(products.isnull().sum())

#------------------ remove duplicates

# orders = orders.drop_duplicates(subset=['order_id'])
# orders.drop_duplicates(subset=['order_id']).sum()
# print(orders)

# customers = customers.drop_duplicates(subset=['customer_id'])
# orders.drop_duplicates(subset=['customer_id']).sum()
# print(customers)

# products = products.drop_duplicates(subset=['product_id'])
# products.drop_duplicates(subset=['product_id']).sum()
# print(products)

# merge dataset
final_df = orders.merge(products, on='product_id', how='left')
final_df = final_df.merge(customers, on='customer_id', how='left')
# print(final_df)


print(final_df.isnull().sum())
# final_df.head()
