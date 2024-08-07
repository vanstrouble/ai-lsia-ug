import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


class KMeans:
    def __init__(self, X, num_clusters, plot=False):
        self.K = num_clusters
        self.X = X
        self.max_iterations = 100
        self.ploture = plot
        self.n_elements, self.n_features = X.shape
        self.centroids = None
        self.clusters = None

    def fit(self):
        self.centroids = self.random_centroids()

        for _ in range(self.max_iterations):
            self.clusters = self.create_clusters()

            old_centroids = self.centroids.copy()
            self.centroids = self.get_new_centroids()

            difference = self.centroids - old_centroids

            if not difference.any():
                break

        y_pred = self.predict()
        y_pred = y_pred.astype(np.int16)

        if self.ploture:
            self.plot(self.X, y_pred)

        return self.centroids, y_pred

    def random_centroids(self):
        return self.X[np.random.choice(range(self.n_elements), size=self.K, replace=False), :]

    def create_clusters(self):
        clusters = [[] for _ in range(self.K)]

        for idx_point, point in enumerate(self.X):
            closest_centroid = np.argmin([np.linalg.norm(point - mean) for mean in self.centroids])
            clusters[closest_centroid].append(idx_point)

        return clusters

    def get_new_centroids(self):
        centroids = np.empty((self.K, self.n_features), dtype=np.float64)
        for i, cluster in enumerate(self.clusters):
            new_centroid = np.mean(self.X[cluster], axis=0)
            centroids[i] = new_centroid

        return centroids

    def predict(self):
        y_pred = np.empty(self.n_elements)

        for idx_cluster, cluster in enumerate(self.clusters):
            for idx_sample in cluster:
                y_pred[idx_sample] = idx_cluster

        return y_pred

    def plot(self, X, y):
        plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
        plt.show()


if __name__ == "__main__":
    num_clusters = 4
    cols = [0, 1]
    data = pd.read_csv('iris.data', header=None).values[:, cols]

    # cols = [1, 2]
    # data = pd.read_csv('wine.data', header=None).values[:, cols]

    Kmeans = KMeans(X=data, num_clusters=num_clusters, plot=True)
    X, y_pred = Kmeans.fit()
