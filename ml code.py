import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the synthetic dataset
data = pd.read_csv('synthetic_dataset.csv')

# Preprocess the data
X = data[['MQ135_PPM', 'MQ6_PPM']]  # Features: sensor readings
y = data['Air_Quality']              # Target: air quality labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Example usage of the trained model
new_data_point = np.array([[50, 75]])  # New sensor readings
predicted_air_quality = clf.predict(new_data_point)
print(f'Predicted Air Quality: {predicted_air_quality[0]}')
