import pandas as pd
import numpy as np
from typing import NamedTuple, List

fake_data = pd.read_csv("data/clusters_2D.csv")
data = fake_data.iloc[:, 0:2]


class KMeans:
    def __init__(self, data, k, seed=None):

        # TODO Add Input validation for parameters
        self.data = data
        self.k = k
        np.random.seed(seed)
        self.centroids = pd.DataFrame()
        self._initialize_centroids()

        # The centroid column should not interfere
        # with the initialization of centroids
        self.data["centroid"] = None

    def _initialize_centroids(self):
        # Rows are dimensions

        # Get dimension range
        dimension_ranges = pd.DataFrame(
            {"min": self.data.min(), "max": self.data.max()}
        )

        # fill up centroids
        # For each K one row
        # For each dimension one columns

        for dimension_name, dimension_values in dimension_ranges.iterrows():
            generated_values = self._generate_k_values(
                dimension_values["min"], dimension_values["max"]
            )
            self.centroids[dimension_name] = generated_values

    def _generate_k_values(self, dimension_min, dimension_max):
        return np.random.uniform(dimension_min, dimension_max, size=self.k)

    def _assign_to_centroids(self):
        
        for index, values in self.data.iterrows():
            observation = values.iloc[:-1]
            self.data.loc[index, "centroid"] = self._closest_centroid(observation)

        print(data.head())

    def _closest_centroid(self, observation):
        distances = [
            np.linalg.norm((observation - centroid).values)
            for centroid in self.centroids.iterrows()
        ]
        return np.argmin(np.array(distances))

    def _update_centroids(self):
        for i in range(self.k):
            self.centroids.iloc[i, :] = self._new_centroid(
                self.data[data["centroid"] == i].iloc[:, :-1]
            )

    def _new_centroid(self, centroid_data):
        print(centroid_data.head())
        return centroid_data.mean()

    def fit(self):
        while not self._centroids_converged():
            self._assign_to_centroids()
            self._update_centroids()

    def _centroids_converged(self, tolerance=0.05):
        pass


kM = KMeans(data=data, k=3, seed=100)

print(kM.centroids)
# print(kM.data.values
print(kM._assign_to_centroids())
print(kM._update_centroids())
print(kM.centroids)
