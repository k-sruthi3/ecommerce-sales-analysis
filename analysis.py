import pandas as pd

# Load dataset
df = pd.read_csv("train.csv",sep="\t")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())
