# def sigmoid(z):
#     return 1 / (1 + (2.71828 ** -z))  # Basic approximation of the sigmoid function

# def initialize_parameters(num_features):
#     weights = [0] * num_features
#     bias = 0
#     return weights, bias

# def compute_cost(y, y_pred):
#     m = len(y)
#     cost = (-1 / m) * sum(y_i * (safe_log(y_pred_i) if y_pred_i != 0 else 0) +
#                           (1 - y_i) * (safe_log(1 - y_pred_i) if 1 - y_pred_i != 0 else 0) for y_i, y_pred_i in zip(y, y_pred))
#     return cost

# def safe_log(x):
#     return 0 if x == 0 else x * (2.30259)  # Basic approximation of the natural logarithm

# def fit(X, y, learning_rate=0.01, num_iterations=1000):
#     m, num_features = len(X), len(X[0])
#     weights, bias = initialize_parameters(num_features)

#     for _ in range(num_iterations):
#         # Forward pass
#         z = [sum(x_i * w_i for x_i, w_i in zip(X[j], weights)) + bias for j in range(m)]
#         y_pred = [sigmoid(z_i) for z_i in z]

#         # Compute cost
#         cost = compute_cost(y, y_pred)

#         # Backward pass
#         dz = [y_pred_i - y_i for y_i, y_pred_i in zip(y, y_pred)]
#         dw = [sum(dz_i * X[j][i] for j, dz_i in enumerate(dz)) / m for i in range(num_features)]
#         db = sum(dz_i for dz_i in dz) / m

#         # Update parameters
#         weights = [w - learning_rate * dw_i for w, dw_i in zip(weights, dw)]
#         bias -= learning_rate * db

#         # Print the cost every 100 iterations
#         if _ % 100 == 0:
#             print(f'Cost after iteration {_}: {cost}')

#     return weights, bias

# def predict(X, weights, bias):
#     z = [sum(x_i * w_i for x_i, w_i in zip(X[j], weights)) + bias for j in range(len(X))]
#     y_pred = [sigmoid(z_i) for z_i in z]
#     y_pred_class = [1 if pred_i > 0.5 else 0 for pred_i in y_pred]
#     return y_pred_class, y_pred

# # Additional Information about the Iris dataset
# from sklearn.datasets import load_iris

# iris = load_iris()
# print("Dataset Information:")
# print("Name of the dataset: Iris")
# print("Number of features:", iris.data.shape[1])
# print("Number of instances:", iris.data.shape[0])
# print("Number of numerical features:", iris.data.shape[1])
# print("Number of categorical features: 1")
# print("Name of the Target variable: Species")

# # Binary classification for Iris-Virginica
# y_binary = (iris.target == 2).astype(int)

# # Train-test split
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(iris.data, y_binary, test_size=0.2, random_state=42)

# # Standardize features (optional but can help with convergence)
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Train the model
# weights, bias = fit(X_train, y_train, learning_rate=0.01, num_iterations=1000)

# # Make predictions on the test data
# predictions, predicted_probabilities = predict(X_test, weights, bias)

# # Display predictions along with true labels
# result = list(zip(predictions, predicted_probabilities, y_test))
# print("\nPredictions:")
# print("Predicted | Probability | Actual")
# print("-----------------------------")
# for pred, prob, actual in result:
#     print(f"    {pred}    |     {prob:.4f}     |    {actual}")

# # Evaluate the accuracy or other metrics based on your task
# accuracy = sum(pred == true_label for pred, true_label in zip(predictions, y_test)) / len(y_test)
# print(f'\nAccuracy: {accuracy}')


import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris=datasets.load_iris()
x = iris.data[:, :2]
y=(iris.target!=0)*1

sc=StandardScaler()
x=sc.fit_transform(x)
print(x[:5])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=42)


class LogisticRegression():
    def __init__(self):
        self.weights=None
    
    def sigmoid(self,z):
        return 1.0/(1.0+np.exp(-z))
    
    def cost(self,h,y):
        return -(y*np.log(h)+(1-y)*np.log(1-h))
    
    def gradient(self,x,h,y):
        return np.dot(x.T,(h-y))/y.shape[0]
    
    def fit(self,x,y,num_iterations=200,learning_rate=0.01):
        self.weights=np.zeros(x.shape[1])
        for i in range(num_iterations):
            z=np.dot(x,self.weights)
            h=self.sigmoid(z)
            grad=self.gradient(x,h,y)
            self.weights=self.weights-learning_rate*grad
    
    def predict(self,x):
        if self.weights is None:
            print("Train first")
            return None
        z=np.dot(x,self.weights)
        return (self.sigmoid(z)>0.5)*1
    
lr=LogisticRegression()
lr.fit(x_train,y_train,learning_rate=0.01,num_iterations=200)

y_pred=lr.predict(x_test)
np.mean(y_pred==y_test)
print(np.mean(y_pred==y_test))

import matplotlib.pyplot as plt
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)

plt.title('Logistic Regression Decision Boundaries')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')