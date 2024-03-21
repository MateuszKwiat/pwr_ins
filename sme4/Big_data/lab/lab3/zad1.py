import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('appartments.csv')

X = df.drop('price', axis=1)
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(f"------------------X --------------------\n{X.head(5)}\nX shape: {X.shape}")
print(f"------------------X_TRAIN --------------------\n{x_train.head(5)}\nX_TRAIN shape: {x_train.shape}")
print(f"------------------X_TEST --------------------\n{x_test.head(5)}\nX_TEST shape: {x_test.shape}")
print()
print(f"------------------Y --------------------\n{Y.head(5)}\nY shape: {Y.shape}")
print(f"------------------Y_TRAIN --------------------\n{y_train.head(5)}\nY_TRAIN shape: {y_train.shape}")
print(f"------------------Y_TEST --------------------\n{y_test.head(5)}\nY_TEST shape: {y_test.shape}\n")

linear_model = LinearRegression()

linear_model.fit(x_train, y_train)
y_prediction = linear_model.predict(X)

print(mean_squared_error(Y, y_prediction))
print(r2_score(Y, y_prediction))

fig, ax = plt.subplots()

ax.scatter(X['area'], Y, color='blue', label='original data')
ax.scatter(X['area'], y_prediction, color='red', label='predictions')

ax.set_xlabel('area')
ax.set_ylabel('price')
ax.legend()

plt.show()