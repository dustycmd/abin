import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# 1. Generate Dataset (2 features for 2D plotting)
X, y = make_classification(
    n_samples=300,
    n_features=2,
    n_redundant=0,
    n_classes=2,
    random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- THE SWITCH ---
#model = DecisionTreeClassifier(max_depth=3)
model = KNeighborsClassifier(n_neighbors=10)
#model = SVC(kernel='rbf')

# 2. Train and Predict
model.fit(X_train, y_train)
pred = model.predict(X_test)

# 3. Standard Output
print(f"--- {type(model).__name__} Results ---")
print(f"Accuracy: {accuracy_score(y_test, pred):.4f}")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, pred))
print("\nClassification Report:\n", classification_report(y_test, pred))

# --- 4. MODEL SPECIFIC GRAPHS ---

# DECISION TREE: Tree structure visualization
if isinstance(model, DecisionTreeClassifier):
    plt.figure(figsize=(12,8))
    plot_tree(model, max_depth=3, filled=True, feature_names=['F1', 'F2'], class_names=['C0', 'C1'])
    plt.title("Decision Tree (Max Depth = 3)")

# KNN & SVC: Both use Decision Boundary Scatterplots
elif isinstance(model, (KNeighborsClassifier, SVC)):
    # Create meshgrid for background coloring
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    # Predict results for every point in the mesh
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    #Inital datset before training 
    plt.scatter(X[:,0],X[:,1],color = "yellow")
    plt.show()

    
    # Plot the contour (decision regions) and the data points
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
    plt.title(f"{type(model).__name__} Decision Boundary")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")

plt.show()
