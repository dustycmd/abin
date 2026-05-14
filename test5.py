import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Generate Synthetic Dataset
X, y = make_classification(
    n_samples=300,
    n_features=5,
    n_informative=3,
    n_redundant=0,
    n_classes=3,
    n_clusters_per_class=1,
    random_state=42
)

df = pd.DataFrame(X, columns=['F1','F2','F3','F4','F5'])
print(df.head())

#model = PCA(n_components=2)
model = TruncatedSVD(n_components=2)
# model = LinearDiscriminantAnalysis(n_components=2)

# Apply Algorithm
if isinstance(model, LinearDiscriminantAnalysis):
    X_new = model.fit_transform(X, y)
else:
    X_new = model.fit_transform(X)

# Print Result
print("Transformed Data:")
print(X_new[:5])

plt.figure(figsize=(8,6))
plt.scatter(X_new[:,0], X_new[:,1], c=y, cmap='viridis')
plt.title("Universal PCA / SVD / LDA Template")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.show()
