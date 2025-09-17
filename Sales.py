# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

data = pd.read_csv(
    r"C:\Users\Yuvaraj\OneDrive\Pictures\New folder\python\sales_data.csv", 
)
print(data.head())

# Check for missing values
print("\nMissing values per column:")
print(data.isnull().sum())

# Drop duplicates
data.drop_duplicates(inplace=True)

# Create a Total Sales column
data['Total'] = data['Quantity'] * data['Price']

# --- Analysis ---

# 1. Total sales per product
product_sales = data.groupby('Product')['Total'].sum().sort_values(ascending=False)
print("\nTotal Sales per Product:")
print(product_sales)

# 2. Monthly revenue
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.to_period('M')
monthly_sales = data.groupby('Month')['Total'].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# 3. Sales by region
region_sales = data.groupby('Region')['Total'].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)

# --- Visualizations ---

# Monthly Sales Line Chart
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales')
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.show()

# Top Products Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(x=product_sales.values, y=product_sales.index)
plt.title("Top Products by Sales")
plt.xlabel("Sales Amount")
plt.ylabel("Product")
plt.show()

# Region Sales Pie Chart
plt.figure(figsize=(7,7))
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Sales by Region')
plt.ylabel("")
plt.show()


