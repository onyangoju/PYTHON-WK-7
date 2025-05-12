import pandas as pd

# Make sure the correct path is provided for your CSV file
df = pd.read_csv(r'C:/Users/Junior/Documents/data.csv')  # Adjust path if needed

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Display basic statistics of numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Check for any missing values
print("\nMissing values:")
print(df.isnull().sum())
