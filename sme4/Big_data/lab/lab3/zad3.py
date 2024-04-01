import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.linear_model import Ridge, LinearRegression, Lasso

months = np.array(np.arange(1, 13))
mean_temperature = np.array([9.4, 5.5, 11.1, 15.5, 22.2, 25.5, 26.1, 26.1, 25.0, 20.5, 13.3, 10.0])
kwh_usage = np.array([1100, 1197, 830, 722, 702, 1018, 784, 965, 893, 598, 645, 887])

alpha = 0.0001

ridge_model = Ridge(alpha=alpha)
lasso_model = Lasso(alpha=alpha)
linear_model = LinearRegression()

ridge_model.fit(mean_temperature.reshape(-1, 1), kwh_usage)
lasso_model.fit(mean_temperature.reshape(-1, 1), kwh_usage)
linear_model.fit(mean_temperature.reshape(-1, 1), kwh_usage)

y_pred_kwh_usage = ridge_model.predict(mean_temperature.reshape(-1, 1))
y_pred_kwh_usage0 = lasso_model.predict(mean_temperature.reshape(-1, 1))
y_pred_kwh_usage1 = linear_model.predict(mean_temperature.reshape(-1, 1))

plt.scatter(months, kwh_usage, color='red', label='data')
plt.plot(months, y_pred_kwh_usage, color='orange', label='ridge prediction')
plt.plot(months, y_pred_kwh_usage0, color='blue', label='lasso prediction')
plt.plot(months, y_pred_kwh_usage1, color='green', label='linear regression prediction')

plt.xlabel('months')
plt.ylabel('kwh usage')
plt.legend()

plt.show()