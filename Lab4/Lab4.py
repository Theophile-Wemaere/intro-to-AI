#!/bin/python

import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

def TNN(X, Y, k=1):
    # Calculate distances between test data and training data
    distances = pairwise_distances(X, X, metric='euclidean')

    # Get indices of k nearest neighbors for each test data
    nearest_neighbors_indices = distances.argsort(axis=1)[:, :k]

    # Predicted labels for each test data
    predicted_labels = []
    for test_index, nearest_neighbors in enumerate(nearest_neighbors_indices):
        # Determine the majority class among the k nearest neighbors
        nearest_classes = Y[nearest_neighbors]
        majority_class = np.argmax(np.bincount(nearest_classes))
        predicted_labels.append(majority_class)

    # Calculate error rate
    error_rate = np.mean(predicted_labels != Y)
    return predicted_labels, error_rate

# Load Iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
Y = iris.target

# Test KNN with k=1
predicted_labels, error_rate = TNN(X, Y, k=1)
print("Error rate with k=1:", error_rate)

# Test KNN using sklearn's KNeighborsClassifier
knn_sklearn = KNeighborsClassifier(n_neighbors=1)
knn_sklearn.fit(X, Y)
Y_pred = knn_sklearn.predict(X)
error_rate_sklearn = np.mean(Y_pred != Y)
print("Error rate using sklearn KNN:", error_rate_sklearn)

# Test KNN with different values of k
for k in [2, 3, 5, 10]:
    predicted_labels, error_rate = TNN(X, Y, k=k)
    print("Error rate with k=", k, ":", error_rate)

# BONUS: Modify TNN to work with k neighbors
def TNN_kneighbors(X, Y, k):
    # Calculate distances between test data and training data
    distances = pairwise_distances(X, X, metric='euclidean')

    # Get indices of k nearest neighbors for each test data
    nearest_neighbors_indices = distances.argsort(axis=1)[:, :k]

    # Determine the majority class among the k nearest neighbors
    predicted_labels = []
    for test_index, nearest_neighbors in enumerate(nearest_neighbors_indices):
        # Count the occurrences of each class among the k nearest neighbors
        class_occurrences = np.bincount(Y[nearest_neighbors])

        # Predict the class with the highest occurrence
        predicted_class = class_occurrences.argmax()
        predicted_labels.append(predicted_class)

    # Calculate error rate
    error_rate = np.mean(predicted_labels != Y)
    return predicted_labels, error_rate

# Test KNN with multiple neighbors
for k in [2, 3, 5, 10]:
    predicted_labels, error_rate = TNN_kneighbors(X, Y, k)
    print("Error rate with k=", k, ":", error_rate)
