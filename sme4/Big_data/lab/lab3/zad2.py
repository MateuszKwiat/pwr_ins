import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score

months = np.array(np.arange(1, 13))
temperatures = np.array([-2, 0, 5, 12, 18, 23, 26, 25, 21, 15, 8, 2])
deg = 4

poly = PolynomialFeatures(deg)
x_poly = poly.fit_transform(months.reshape(-1, 1))

linear_model = LinearRegression()
linear_model.fit(x_poly, temperatures)
x_values = np.linspace(1, 12, 100)

x_poly_values_plot = poly.transform(x_values.reshape(-1, 1))
y_pred_plot = linear_model.predict(x_poly_values_plot)

x_poly_values = poly.transform(months.reshape(-1, 1))
y_pred = linear_model.predict(x_poly_values)

print(mean_squared_error(temperatures, y_pred))
print(r2_score(temperatures, y_pred))

plt.scatter(months, temperatures, color='red', label='data')
plt.plot(x_values, y_pred_plot, color='orange', label='prediction')
plt.xlabel('months')
plt.ylabel('temperatures')
plt.legend()
plt.show()