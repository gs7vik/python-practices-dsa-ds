import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

# Load data
digits = load_digits()
X = digits.data

# Fit PCA (all components)
pca = PCA().fit(X)

# Cumulative explained variance
cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

# Find smallest k such that variance ≥ 95%
k_95 = np.argmax(cumulative_variance >= 0.95) + 1  # +1 because indices start at 0

print(f"Number of components needed for 95% variance: {k_95}")

#digits dataset has 64 features.
#So, we need 29 components to explain 95% of the variance(information) in the data.
#We can reduce the dimensionality from 64 to 29 with minimal loss of information.
#This is useful in reducing computational cost and avoiding the curse of dimensionality.
"""
These 29 components are not the original features (pixels).
They are new features (linear combinations of pixels).
"""