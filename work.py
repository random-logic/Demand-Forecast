import pandas as pd
import numpy as np
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Filepaths for your CSV files
fedfunds_file_path = '/Users/weitaochen/Downloads/FEDFUNDS.csv'
walmart_file_path = '/Users/weitaochen/Downloads/Walmart.csv'

# Load the CSV files
fedfunds_data = pd.read_csv(fedfunds_file_path)
walmart_data = pd.read_csv(walmart_file_path)

# Convert date columns to datetime format
fedfunds_data['observation_date'] = pd.to_datetime(fedfunds_data['observation_date'])
walmart_data['Date'] = pd.to_datetime(walmart_data['Date'], format='%d-%m-%Y')  # Adjust format if needed

# Rename the FEDFUNDS date column for consistency
fedfunds_data.rename(columns={'observation_date': 'Date'}, inplace=True)

# Clean up Walmart data
# Drop duplicates
walmart_data = walmart_data.drop_duplicates()

# Handle missing values
walmart_data = walmart_data.dropna()  # Drop rows with missing values
# Alternatively, fill missing values:
# walmart_data = walmart_data.fillna({'Weekly_Sales': 0, 'Holiday_Flag': 0})

# Clean up FEDFUNDS data
# Drop duplicates
fedfunds_data = fedfunds_data.drop_duplicates()

# Handle missing values
fedfunds_data = fedfunds_data.dropna()

# Merge the two datasets on the 'Date' column
merged_data = pd.merge(walmart_data, fedfunds_data, on='Date', how='inner')

# Final cleaning of the merged data
# Drop unnecessary columns if needed
# merged_data = merged_data.drop(['Unnecessary_Column'], axis=1)

# Save the cleaned and merged data to a new CSV file
output_file_path = '/Users/weitaochen/Downloads/merged_data_cleaned.csv'
merged_data.to_csv(output_file_path, index=False)

# Display the cleaned and merged data and confirm the output file
print("Cleaned and merged data:")
print(merged_data.head())
print(f"\nCleaned and merged data saved to: {output_file_path}")


# Load the cleaned and merged dataset
file_path = '/Users/weitaochen/Downloads/merged_data_cleaned.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand the data
print(data.head())

# Step 1: Prepare the data
# Define the target variable (e.g., 'Weekly_Sales') and features
target_column = 'Weekly_Sales'  # Replace with your desired target column
features = data.drop(columns=[target_column, 'Date'])  # Exclude the target and date columns
target = data[target_column]

# Normalize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

# Step 2: Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Step 3: Train the model
history = model.fit(X_train, y_train, epochs=50, validation_split=0.2, batch_size=32, verbose=1)

# Step 4: Evaluate the model
loss, mae = model.evaluate(X_test, y_test, verbose=1)
print(f"Mean Absolute Error on Test Data: {mae}")

# Step 5: Make Predictions
predictions = model.predict(X_test[:5])
print(f"Predictions for first 5 test samples: {predictions.flatten()}")
print(f"Actual values for first 5 test samples: {y_test[:5].values}")

# Combine features and target variable into one dataframe
data['Weekly_Sales'] = y_train  # Replace 'Weekly_Sales' with your target variable column
features_with_target = data[['Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Weekly_Sales']]

# Compute the correlation matrix
correlation_matrix = features_with_target.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Feature Correlation Heatmap')
plt.show()

# Plot pairplot
sns.pairplot(features_with_target, diag_kind='kde', height=2.5)
plt.show()