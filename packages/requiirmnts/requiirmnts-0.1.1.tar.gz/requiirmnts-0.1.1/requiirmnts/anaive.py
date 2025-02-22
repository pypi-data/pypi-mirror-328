import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Load dataset
iris = load_iris()
X, y, class_names = iris.data, iris.target, iris.target_names

class NaiveBayes:
    def fit(self, X, y):
        self._classes, counts = np.unique(y, return_counts=True)
        self._mean, self._var = np.array([X[y == c].mean(0) for c in self._classes]), np.array([X[y == c].var(0) for c in self._classes])
        self._priors = counts / len(y)

    def predict(self, X):
        return np.array([self._classes[np.argmax([np.log(prior) + np.sum(np.log(self._pdf(i, x))) for i, prior in enumerate(self._priors)])] for x in X])

    def _pdf(self, i, x):
        mean, var = self._mean[i], self._var[i]
        return np.exp(- (x - mean)**2 / (2 * var)) / np.sqrt(2 * np.pi * var)

# Train-test split & model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
nb = NaiveBayes()
nb.fit(X_train, y_train)

# Make predictions & print accuracy
y_pred = nb.predict(X_test)
print(f'Accuracy: {np.mean(y_pred == y_test):.4f}')
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=class_names))

# User input for prediction

try:
    inp = list(map(float, input("\nEnter 4 feature values (comma-separated): ").split(',')))
    if len(inp) != 4:
        print("Please enter exactly 4 numeric values.")
    pred = nb.predict([inp])[0]
    print(f'Predicted class: {class_names[pred]}')
except ValueError:
    print("Invalid input. Enter 4 numeric values separated by commas.")
