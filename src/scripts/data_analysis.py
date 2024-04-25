import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the current directory of the script
current_dir = os.path.dirname(__file__)

# Navigate to the data folder from the script folder
data_folder = os.path.join(current_dir, '../data')

# Load the data from the CSV file
df = pd.read_csv(os.path.join(data_folder, 'benin-malanville.csv'))

# Display the first few rows of the DataFrame
print(df.head())

# Get an overview of the DataFrame structure
print(df.info())

# Calculate summary statistics for numeric columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Handle missing values (e.g., imputation or removal)
df.dropna(inplace=True)  # Example: remove rows with missing values

# Drop the 'Comments' column
df.drop(columns=['Comments'], inplace=True)

# Convert the Timestamp column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Set Timestamp as the index
df.set_index('Timestamp', inplace=True)

# Plot time series data for relevant variables
df['GHI'].plot()  # Example: plot Global Horizontal Irradiance over time

# Calculate correlation matrix
correlation_matrix = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Plot histograms for numeric variables
df.hist(figsize=(12, 10))
plt.show()

# Visualize relationships between variables using scatter plots
plt.scatter(df['Tamb'], df['GHI'])
plt.xlabel('Ambient Temperature (°C)')
plt.ylabel('Global Horizontal Irradiance (W/m²)')
plt.title('Ambient Temperature vs. GHI')
plt.show()

