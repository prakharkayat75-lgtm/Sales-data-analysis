import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.ticklabel_format(style='plain', axis='y')

# load data
orders=pd.read_excel("order_clean_E.xlsx")
products=pd.read_excel("product_clean_E.xlsx")
customers=pd.read_excel("customer_clean_E.xlsx")

# merge data
df = orders.merge(products, on='product_id', how='left')
df = df.merge(customers, on='customer_id', how='left')

# print(df)

df['revenue'] = df['qty'] * df['selling_price']
# print(df['revenue'])
df['profit'] = df['revenue']-(df['qty']*df['cost_price'])
# print(df['profit'])

df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')

# print(df['month'])

# VISUALISATION
# monthly_sales = df.groupby('month')['revenue'].sum()

#1 MONTHLY SALES
# plt.figure()
# monthly_sales.plot()
# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Revenue")
# plt.show()

#CATEGORY WISE REVENUE
# category_sales = df.groupby('category')['revenue'].sum()

# plt.figure()
# category_sales.plot(kind='bar')
# plt.title("Category-wise Revenue")
# plt.xlabel("Category")
# plt.ylabel("Revenue")
# plt.show()


# CITY WISE DISTRIBUTION
# city_sales = df.groupby('city')['revenue'].sum().sort_values(ascending=False).head(10)

# plt.figure()
# city_sales.plot(kind='bar')
# plt.title("Top 10 Cities by Revenue")
# plt.xlabel("City")
# plt.ylabel("Revenue")
# plt.show()

#AGE VS REVENUE(SCATTER PLOT)
# plt.figure()
# plt.scatter(df['age'], df['revenue'])
# plt.title("Age vs Revenue")
# plt.xlabel("Age")
# plt.ylabel("Revenue")
# plt.show()

# CORRELATON HEATMAP
# plt.figure()
# sns.heatmap(df[['age', 'qty', 'selling_price', 'cost_price', 'revenue', 'profit']].corr(), annot=True)
# plt.title("Correlation Heatmap")
# plt.show()


# REVENUE DISTRIBUTION
# plt.figure()
# sns.histplot(df['revenue'], bins=30)
# plt.title("Revenue Distribution")
# plt.show()

# PROFIT DISTRIBUTION
# plt.figure()
# plt.ticklabel_format(style='plain')
# sns.histplot(df['profit'], bins=30)
# plt.title("Profit Distribution")
# plt.show()

# category_sales = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
# print(category_sales.head(5))


# city_sales = df.groupby('city')['revenue'].sum().sort_values(ascending=False)
# print(city_sales.head(5))
# print(city_sales.tail(5))

# monthly_sales = df.groupby('month')['revenue'].sum().sort_values(ascending=False)
# print(monthly_sales.head(3))

# loss_products = df[df['profit'] < 0].groupby('product_id')['profit'].sum().sort_values()
# print(loss_products.head(5))

print(df.groupby('age')['revenue'].sum().sort_values(ascending=False).head())