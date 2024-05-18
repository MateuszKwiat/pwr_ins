import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_breast_cancer

from sklearn import metrics
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

breast_cancer = load_breast_cancer()

X = breast_cancer.data
Y = breast_cancer.target

df = pd.DataFrame(X)

df.head()

print(df.isna().sum().sum(), df.isnull().sum().sum())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.3, random_state=42)
logistic_regression = LogisticRegression(max_iter=3000)

logistic_regression.fit(X_train, Y_train)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)

lr_Y_pred = logistic_regression.predict(X_test)
knn_Y_pred = knn.predict(X_test)

print('-----------------logistic regression-----------------')
print(metrics.classification_report(Y_test, lr_Y_pred))
print('\n---------------------k neighbors---------------------')
print(metrics.classification_report(Y_test, knn_Y_pred))

print('-----------------logistic regression-----------------')
print(f"accuracy: {metrics.accuracy_score(Y_test, lr_Y_pred)}\nprecision: {metrics.precision_score(Y_test, lr_Y_pred, average='weighted')}\nrecall: {metrics.recall_score(Y_test, lr_Y_pred, average='weighted')}")
print('\n---------------------k neighbors---------------------')
print(f"accuracy: {metrics.accuracy_score(Y_test, knn_Y_pred)}\nprecision: {metrics.precision_score(Y_test, knn_Y_pred, average='weighted')}\nrecall: {metrics.recall_score(Y_test, knn_Y_pred, average='weighted')}")
