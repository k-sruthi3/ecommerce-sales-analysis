import pandas as pd

# Load dataset
df = pd.read_csv("train.csv", encoding="utf-8")  # comma is default

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

# Convert date columns to datetime (Day first format)
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

print("\nUpdated Data Types:")
print(df.dtypes)

# Feature Engineering
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.strftime('%B')
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

print("\nFirst 5 rows with new features:")
print(df.head())


