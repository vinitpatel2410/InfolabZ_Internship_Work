import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data from CSV
df = pd.read_csv('Example.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y')

# Sort the data by date in ascending order
df = df.sort_values(by='Date')

# Create a feature matrix X (independent variable) and target vector y (dependent variable)
X = df.index.values.reshape(-1, 1)  # Using the index as a numerical representation of time
y = df['Close']

# Initialize and fit the Linear Regression model
reg = LinearRegression()
reg.fit(X, y)

# Get the slope (coefficient) and intercept of the regression line
b1 = reg.coef_[0]
b0 = reg.intercept_

# Generate the predicted values using the model
y_pred = reg.predict(X)

# Plot the actual data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(df['Date'], df['Close'], label='Actual Data', marker='o')
plt.plot(df['Date'], y_pred, color='red', label='Regression Line')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Nifty 50 Index - 1 Year Data')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
