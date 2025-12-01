import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from matplotlib.colors import ListedColormap

def plot_decision_boundary(clf, X, y, title):
    # Create a mesh grid
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    # Predict
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=ListedColormap(['#FFCCCC', '#CCFFCC']))
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=ListedColormap(['#FF0000', '#00FF00']), s=100)
    plt.title(title)
    plt.xlabel("Input 1")
    plt.ylabel("Input 2")
    plt.grid(True)

# 1. DATA: Logic Gates
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_AND = np.array([0, 0, 0, 1]) # Linear
y_XOR = np.array([0, 1, 1, 0]) # Non-Linear

# 2. MODEL: Single Layer Perceptron
clf_and = Perceptron(tol=1e-3, random_state=0)
clf_and.fit(X, y_AND)

clf_xor = Perceptron(tol=1e-3, random_state=0)
clf_xor.fit(X, y_XOR)

# 3. VISUALIZATION
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plot_decision_boundary(clf_and, X, y_AND, "Perceptron on AND Gate (Success)")

plt.subplot(1, 2, 2)
plot_decision_boundary(clf_xor, X, y_XOR, "Perceptron on XOR Gate (Failure)")
# Note: In the XOR plot, the background color (decision region) cannot separate red/green perfectly.

plt.show()
