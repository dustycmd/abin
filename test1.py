import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)
x1 = np.random.rand(1000, 1) * 10
x2 = np.random.rand(1000, 1) * 5
noise = np.random.randn(1000, 1) * 3

#y = 3*x1 +noise
#X = np.hstack([x1])
y = 3*x1 + 2*x2 + noise 
X = np.hstack([x1, x2]) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

ypred = model.predict(X_test)
print(f"R2 Score (Accuracy): {r2_score(y_test, ypred)}")
print(f"MAE: {mean_absolute_error(y_test, ypred)}")
print(f"MSE: {mean_squared_error(y_test, ypred)}")

plt.scatter(y_test, ypred, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], lw=2,color = 'red')
plt.xlabel("Actual Y")
plt.ylabel("Predicted Y")
plt.title("Actual vs Predicted (Linear/Multi)")
plt.show()
