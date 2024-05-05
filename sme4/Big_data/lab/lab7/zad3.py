import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_digits

from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.svm import SVC

digits = load_digits()
X = digits.data
Y = digits.target

df = pd.DataFrame(X)
print(df.head(5))

print(df.isna().sum().sum(), df.isnull().sum().sum())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=42)

svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, Y_train)

Y_pred = svm_classifier.predict(X_test)

print(metrics.classification_report(Y_test, Y_pred))