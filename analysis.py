import pandas as pd

# Load ecommerce data
df = pd.read_csv("python/ecommerce_sales_data.csv")

# Basic information
print("Total Orders:", len(df))
print("Total Sales:", df["Total_Sales"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())
print("Average Order Value:", df["Total_Sales"].mean())

# Category-wise Sales
category_sales = df.groupby("Category")["Total_Sales"].sum()

print("\nCategory-wise Sales:")
print(category_sales)
# City-wise Sales
city_sales = df.groupby("City")["Total_Sales"].sum()

print("\nCity-wise Sales:")
print(city_sales)
# Product-wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

print("\nProduct-wise Sales:")
print(product_sales)
# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Monthly Sales
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)
print("\nMonthly Sales:")
print(monthly_sales)
