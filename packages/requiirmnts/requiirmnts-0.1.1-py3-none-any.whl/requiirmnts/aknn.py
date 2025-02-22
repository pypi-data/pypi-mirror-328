import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=1)
class_names = iris.target_names

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train, self.y_train = X, y

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        distances = np.linalg.norm(self.X_train - x, axis=1)  # Vectorized Euclidean distance
        k_nearest_labels = self.y_train[np.argsort(distances)[:self.k]]  # Get top-k labels
        return Counter(k_nearest_labels).most_common(1)[0][0]  # Most common class

# Train and evaluate k-NN
knn = KNN(k=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Accuracy and evaluation metrics
print(f'Accuracy: {np.mean(y_pred == y_test):.4f}')
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=class_names))

# User input for prediction
try:
    inp = np.array(list(map(float, input("\nEnter 4 feature values (comma-separated): ").split(','))))
    if inp.shape[0] != 4:
        raise ValueError("Please enter exactly 4 numeric values.")
    print(f'Predicted class: {class_names[knn.predict([inp])[0]]}')
except ValueError as e:
    print(f"Invalid input: {e}")