import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# 1. Generate Synthetic Dataset
X, y = make_classification(
    n_samples=50000, 
    n_features=10, 
    n_informative=8, 
    n_classes=2, 
    random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#model = RandomForestClassifier(n_estimators=100)
#model = AdaBoostClassifier()
model = GradientBoostingClassifier()
# model = XGBClassifier(eval_metric='logloss')
# model = LGBMClassifier(verbose=-1)

model.fit(X_train, y_train)
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print(f"--- Model: {type(model).__name__} ---")
print(f"Training Accuracy: {accuracy_score(y_train, train_pred):.4f}")
print(f"Testing Accuracy:  {accuracy_score(y_test, test_pred):.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, test_pred))

print("\nClassification Report:")
print(classification_report(y_test, test_pred))
