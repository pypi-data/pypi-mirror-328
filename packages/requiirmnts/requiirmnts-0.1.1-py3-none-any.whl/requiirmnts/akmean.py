import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X, k = iris.data, 3  

def kmeans(X, k, max_iters=100):
    centroids = X[np.random.choice(len(X), k, replace=False)]
    for _ in range(max_iters):
        labels = np.argmin(np.linalg.norm(X[:, None] - centroids, axis=2), axis=1)
        centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
    return centroids, labels

centroids, labels = kmeans(X, k)

# User input for prediction
try:
    inp = np.array(list(map(float, input("\nEnter 4 feature values (comma-separated): ").split(','))))
    if inp.shape[0] != 4: raise ValueError
    pred_cluster = np.argmin(np.linalg.norm(centroids - inp, axis=1))

    # Plot clusters
    colors = ['r', 'g', 'b']
    for i, c in enumerate(colors):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], c=c, label=f'Cluster {i+1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='black', label='Centroids')
    
    # Plot user input
    plt.scatter(inp[0], inp[1], c='yellow', edgecolors='black', marker='o', s=150, label='User Input')
    plt.title('K-Means Clustering on Iris'); plt.xlabel('Sepal Length'); plt.ylabel('Sepal Width')
    plt.legend(); plt.show()

    print(f'Predicted Cluster: Cluster {pred_cluster + 1}')
except ValueError:
    print("Invalid input! Enter exactly 4 numeric values.")