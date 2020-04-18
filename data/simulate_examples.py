import numpy as np
import pandas as pd
import os


def generate_2D_cluster(mean, cov, size=100):
    return np.random.multivariate_normal(mean=mean, cov=cov, size=size)


variance = 10
covariance = 0
vcov_matrix = np.array([[variance, covariance], [covariance, variance]])

cluster_means = [(0, 0), (0, 100), (100, 0), (100, 100), (50, 50)]

clusters = [generate_2D_cluster(mean, vcov_matrix) for mean in cluster_means]

clusters_df = pd.DataFrame(columns=["x", "y", "cluster"])

for cluster_id, cluster in enumerate(clusters):
    temp_df = pd.DataFrame(
        {"x": cluster[:, 0], "y": cluster[:, 1], "cluster": cluster_id + 1}
    )
    clusters_df = clusters_df.append(temp_df)

clusters_df.to_csv("data/clusters_2D.csv", index=False)
