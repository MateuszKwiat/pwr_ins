import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_breast_cancer

from sklearn import metrics
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

breast_cancer = load_breast_cancer()

X = breast_cancer.data
Y = breast_cancer.target

df = pd.DataFrame(X)

print(df.head())

print(df.isna().sum().sum(), df.isnull().sum().sum())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=42)
logistic_regression = LogisticRegression(max_iter=3000)

logistic_regression.fit(X_train, Y_train)

Y_pred = logistic_regression.predict(X_test)

print(metrics.classification_report(Y_test, Y_pred))