import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Sigmoid function
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# Logistic Regression Model using Gradient Descent
def logistic_regression(X, y, num_iterations=200, learning_rate=0.001):
    weights = np.zeros(X.shape[1])  # Initialize weights
    for _ in range(num_iterations):
        z = np.dot(X, weights)
        h = sigmoid(z)
        gradient_val = np.dot(X.T, (h - y)) / y.shape[0]
        weights -= learning_rate * gradient_val
    return weights

# Load and preprocess the dataset
iris = load_iris()
X = iris.data[:, :2]  # Use only sepal length and width
y = (iris.target != 0) * 1  # Convert to binary classification (Setosa vs. Others)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=9)

# Standardize the features
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# Train logistic regression model
weights = logistic_regression(X_train_std, y_train)

# Take user input for Sepal Length and Sepal Width
sepal_length = float(input("Enter Sepal Length (cm): "))
sepal_width = float(input("Enter Sepal Width (cm): "))

# Standardize user input using the same scaler
user_input = np.array([[sepal_length, sepal_width]])
user_input_std = sc.transform(user_input)

# Make prediction
prediction = sigmoid(np.dot(user_input_std, weights)) > 0.5

# Print the result
if prediction:
    print("Predicted Class: Not Setosa (Class 1)")
else:
    print("Predicted Class: Setosa (Class 0)")