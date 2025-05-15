import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    df = pd.read_csv("iris.data", names=column_names)
    df.dropna(how='all', inplace=True)
    print("First 5 rows:\n", df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values per Column:")
    print(df.isnull().sum())
    df.dropna(inplace=True)
except FileNotFoundError:
    print("Error: 'iris.data' file not found.")
except Exception as e:
    print("An error occurred:", e)

# Task 2: Basic Data Analysis
print("\nDescriptive Statistics:")
print(df.describe())

print("\nGroup by Species (Mean):")
print(df.groupby("species").mean())

print("\nInteresting Observations:")
print("- Setosa petals are shorter and narrower.")
print("- Virginica has the largest average petal and sepal dimensions.")

# Task 3: Data Visualization
sns.set(style="whitegrid")

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal_length'], label='Sepal Length')
plt.plot(df.index, df['petal_length'], label='Petal Length', linestyle='--')
plt.title('Line Chart of Sepal and Petal Length')
plt.xlabel('Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df['sepal_width'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()
