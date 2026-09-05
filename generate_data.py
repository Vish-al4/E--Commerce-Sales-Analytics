import pandas as pd
import numpy as np

# Number of customers
n = 1000

# Customer IDs
customer_id = np.arange(1001, 1001 + n)

# Customer names
customer_name = np.random.choice(
    ["Rahul", "Priya", "Amit", "Sneha", "Vishal"],
    n
)

# Cities
city = np.random.choice(
    ["Pune", "Mumbai", "Nanded", "Delhi"],
    n
)

# Product categories
categories = np.random.choice(
    ["Electronics", "Furniture", "Clothing", "Grocery"],
    n
)

# Category-wise products
product_map = {
    "Electronics": ["Laptop", "Mobile", "Headphones", "Tablet"],
    "Furniture": ["Chair", "Table", "Sofa", "Bed"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Shoes"],
    "Grocery": ["Rice", "Oil", "Tea", "Coffee"]
}

# Product according to Category
products = [
    np.random.choice(product_map[category])
    for category in categories
]

# Create DataFrame
df = pd.DataFrame({
    "Customer_ID": customer_id,
    "Customer_Name": customer_name,
    "City": city,
    "Category": categories,
    "Product": products
})

# Display data
print(df)
# Price
price = np.random.randint(100, 50001, n)

# Add Price column
df["Price"] = price

print(df)
# Quantity
quantity = np.random.randint(1, 6, n)

# Add Quantity column
df["Quantity"] = quantity

print(df)
# Order Date
order_date = pd.date_range(
    start="2026-01-01",
    periods=n,
    freq="D"
)

# Add Order Date column
df["Order_Date"] = order_date

print(df)
# Payment Mode
payment_mode = np.random.choice(
    ["UPI", "Credit Card", "Debit Card", "Cash"],
    n
)

# Add Payment Mode column
df["Payment_Mode"] = payment_mode

# Product-wise realistic price

price_map = {
    "Laptop": (30000, 80000),
    "Mobile": (10000, 50000),
    "Headphones": (1000, 10000),
    "Tablet": (15000, 40000),

    "Chair": (1000, 5000),
    "Table": (3000, 10000),
    "Sofa": (15000, 50000),
    "Bed": (10000, 40000),

    "T-Shirt": (300, 1500),
    "Jeans": (800, 3000),
    "Jacket": (1500, 5000),
    "Shoes": (1000, 5000),

    "Rice": (50, 200),
    "Oil": (100, 300),
    "Tea": (100, 500),
    "Coffee": (150, 600)
}

# Select price according to product
price = [
    np.random.randint(
        price_map[product][0],
        price_map[product][1] + 1
    )
    for product in products
]

# Add Price column
df["Price"] = price

print(df)
# Total Sales
total_sales = df["Price"] * df["Quantity"]

# Add Total Sales column
df["Total_Sales"] = total_sales

print(df)
df["Total_Sales"] = total_sales

print(df)
# Save data to CSV file
df.to_csv(
    "ecommerce_sales_data.csv",
    index=False
)

print("CSV file created successfully!")
