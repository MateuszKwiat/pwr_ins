import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

from sklearn import metrics
from sklearn.model_selection import train_test_split

iris = load_iris()

X = iris.data
Y = iris.target

df = pd.DataFrame(X)
print(df.head(5))

print(df.dtypes)

print(df.isna().sum().sum(), df.isnull().sum().sum())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)

Y_pred = knn.predict(X_test)

print(metrics.classification_report(Y_test, Y_pred))