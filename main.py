import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("="*40)
print("   E-Commerce Sales Data Analysis")
print("="*40)

# Upload CSV file
df = pd.read_csv("data.csv", encoding='ISO-8859-1')

# Show first rows of dataset
print("First rows of dataset:")
print(df.head())

# Show general information of dataset
print("\nGeneral information of dataset:")
print(df.info())

# Check how many data is missing by column
print("\nNull values by column:")
print(df.isnull().sum())

# ------------------------------
# DATA CLEANING
# ------------------------------

# Delete rows with Null description
df = df.dropna(subset=['Description'])

# Delete sales with negative amount or equal to 0
df = df[df['Quantity'] > 0]

#Transform InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Show Cleaning result
print(f"\nRows after clean: {len(df)}")
print(df.head())

# ------------------------------
# EDA (EXPLORATORY DATA ANALYSIS)
# ------------------------------

# Countries with most sales (top10)
top_countries = df['Country'].value_counts().head(10)
print("\nTop 10 countries with most sales;")
print(top_countries)

# Top 10 products
top_products = df['Description'].value_counts().head(10)
print("\nTop 10 products with most sales;")
print(top_products)

# Sales per hour
df['Hour'] = df['InvoiceDate'].dt.hour
sales_per_hour = df['Hour'].value_counts().sort_index()
print("\nSales per hour of day:")
print(sales_per_hour)

# Sales per day
df['Date'] = df['InvoiceDate'].dt.date
sales_per_day = df.groupby('Date').size()
print("\nSales per day:")
print(sales_per_day)

# ------------------------------
# DATA VISUALIZATION
# ------------------------------

print("="*50)
print("📊 E-Commerce Sales Dashboard")
print("="*50)

print(f"\nTotal number of transactions after cleaning: {len(df)}")
print(f"Date range: from {df['InvoiceDate'].min().date()} to {df['InvoiceDate'].max().date()}")

# Print top countries
print("\n🌍 Top 10 countries with most purchases:")
print(top_countries)

# Print top products
print("\n🛒 Top 10 best-selling products:")
print(top_products)

# -----------------------------
# GRAPH 1: Sales by country
# -----------------------------
plt.figure(figsize=(10,6))
top_countries.plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries by Number of Sales")
plt.xlabel("Country")
plt.ylabel("Number of Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# GRAPH 2: Best-selling products
# -----------------------------
plt.figure(figsize=(10,6))
top_products.plot(kind='barh', color='lightgreen')
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Number of Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.show()

# -----------------------------
# GRAPH 3: Sales by hour of day
# -----------------------------
plt.figure(figsize=(10,6))
sns.lineplot(x=sales_per_hour.index, y=sales_per_hour.values, marker='o')
plt.title("Sales by Hour of the Day")
plt.xlabel("Hour")
plt.ylabel("Number of Sales")
plt.xticks(range(0,24))
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# GRAPH 4: Sales by day
# -----------------------------
plt.figure(figsize=(12,6))
sales_per_day.plot(kind='line')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Sales")
plt.tight_layout()
plt.show()

print("\n✅ Dashboard execution complete.")

print("="*50)
print("End of report - Generated with Python 📈")
print("="*50)





