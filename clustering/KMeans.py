import pandas as pd
import numpy as np
from typing import NamedTuple, List

fake_data = pd.read_csv("data/clusters_2D.csv")


class KMeans:
    def __init__(self, data, k):

        # TODO Add Input validation for parameters
        self.data = data
        self.k = k
        self.centroids = pd.DataFrame()
        self._initialize_centroids()

    def _initialize_centroids(self):
        # Rows are dimensions

        #Get dimension range
        dimension_ranges = pd.DataFrame({"min": self.data.min(), "max": self.data.max()})


        # fill up centroids
        # For each K one row
        # For each dimension one columns

        for i, dimension in dimension_ranges.iterrows():
            dimension_min = dimension["min"]
            dimension_max = dimension["max"]
            values = _generate_K_values(dimension_min, dimension_max)
            self.centroids[i+1] = values

    def _generate_K_values(self, dimension_min, dimension_max):
        np.random
