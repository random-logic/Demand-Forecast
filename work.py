import pandas as pd
import numpy as np
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load Data
fedfunds_file_path = '/Users/weitaochen/Downloads/FEDFUNDS.csv'
walmart_file_path = '/Users/weitaochen/Downloads/Walmart.csv'

fedfunds_data = pd.read_csv(fedfunds_file_path)
walmart_data = pd.read_csv(walmart_file_path)

# Convert date columns to datetime
fedfunds_data['observation_date'] = pd.to_datetime(fedfunds_data['observation_date'])
walmart_data['Date'] = pd.to_datetime(walmart_data['Date'], format='%d-%m-%Y')

# Rename FEDFUNDS date column
fedfunds_data.rename(columns={'observation_date': 'Date'}, inplace=True)

# Clean data
walmart_data = walmart_data.drop_duplicates().dropna()
fedfunds_data = fedfunds_data.drop_duplicates().dropna()

# Merge datasets
merged_data = pd.merge(walmart_data, fedfunds_data, on='Date', how='inner')

# Define target and features
target_column = 'Weekly_Sales'
features = merged_data.drop(columns=[target_column, 'Date'])
target = merged_data[target_column]

# Normalize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Normalize target
target_scaler = StandardScaler()
target_scaled = target_scaler.fit_transform(target.values.reshape(-1, 1))

# Split dataset
X_train, X_test, y_train_scaled, y_test_scaled = train_test_split(features_scaled, target_scaled, test_size=0.2, random_state=42)

# Feature Importance Analysis
rf = RandomForestRegressor(n_estimators=50, random_state=42)
rf.fit(X_train, y_train_scaled.ravel())

# Define feature importance
feature_importance = pd.Series(rf.feature_importances_, index=features.columns)

# Keep only the top 5 important features
top_features = feature_importance.nlargest(5).index.tolist()
features = features[top_features]

# Ensure X_test_scaled is defined
X_test_scaled = scaler.transform(X_test)

# Optimized Neural Network Model (Leaky ReLU & Tanh for Stability)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(256),
    tf.keras.layers.LeakyReLU(alpha=0.01),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.4),

    tf.keras.layers.Dense(128),
    tf.keras.layers.LeakyReLU(alpha=0.01),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.4),

    tf.keras.layers.Dense(64),
    tf.keras.layers.LeakyReLU(alpha=0.01),
    tf.keras.layers.BatchNormalization(),

    tf.keras.layers.Dense(1, activation='tanh')  # Prevents large predictions
])

# Compile Model with Adjusted Learning Rate
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), loss='mse', metrics=['mae'])

# Early Stopping
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train Model
history = model.fit(X_train, y_train_scaled, epochs=50, validation_split=0.2, batch_size=8, verbose=1, callbacks=[early_stopping])

# Plot Training Loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title("Loss Convergence Plot")
plt.show()

# Evaluate Model
loss, mae = model.evaluate(X_test, y_test_scaled, verbose=0)
print(f"\nNeural Network Mean Absolute Error on Test Data (Scaled): {mae:.2f}")

# Debugging: Check Data Shape
print("📏 X_test shape:", X_test.shape)
print("📏 X_test_scaled shape:", X_test_scaled.shape)

# Make Predictions (Fixing Scaling Issue)
nn_predictions_scaled = model.predict(X_test_scaled[:3])

# Debugging: Check Scaling Before Inversion
print("Scaled Predictions:", nn_predictions_scaled.flatten())
print("Scaled Actuals:", y_test_scaled[:3].flatten())

# Apply Correct Inverse Transformation
nn_predictions = target_scaler.inverse_transform(nn_predictions_scaled.reshape(-1, 1))
actual_values = target_scaler.inverse_transform(y_test_scaled[:3].reshape(-1, 1))

# Debugging: Check Post-Inversion Values
print("Inverse Transformed Predictions:", nn_predictions.flatten())
print("Inverse Transformed Actuals:", actual_values.flatten())

# Print Predictions vs Actual Values
print("\nNeural Network Predictions vs Actual Values (First 3 Test Samples):")
for i in range(3):
    print(f"Prediction: {nn_predictions[i][0]:.2f}, Actual: {actual_values[i][0]:.2f}")
