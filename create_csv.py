import pandas as pd

# Create a sample dataset
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [28, 30, 25, 22, 35],
    'City': ['New York', 'London', 'Sydney', 'Berlin', 'Paris']
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)

# Print the DataFrame to confirm it's correct
print(df)
