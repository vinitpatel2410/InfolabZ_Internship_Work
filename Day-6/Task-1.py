import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer


df = pd.read_csv('price.csv')
print(df.isnull().sum())
imputer = SimpleImputer(strategy='mean')
df[['area', 'price']] = imputer.fit_transform(df[['area', 'price']])

# Scatter plot of data points
plt.scatter(df.area, df.price)
plt.xlabel('Area')
plt.ylabel('Price')

# Linear regression
reg = LinearRegression()
reg.fit(df[['area']], df['price'])

# Prediction line
b0 = reg.intercept_
b1 = reg.coef_[0]
x_values = df.area
y_pred = b0 + b1 * x_values

# Plotting the prediction line
plt.plot(x_values, y_pred, color='red', label='Prediction Line')
plt.legend()
plt.show()

# Example prediction
area_to_predict = [[3300]]
predicted_price = reg.predict(area_to_predict)
print(f"Predicted price for area 3300 sq.ft: {predicted_price[0]}")
