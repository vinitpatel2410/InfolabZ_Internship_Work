import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the CSV file into a DataFrame
df = pd.read_csv("orderdata.csv")

# Print the first few rows of the DataFrame
print(df.head())

# Print the column names of the DataFrame
print("Column names:", df.columns)

# Create a LinearRegression model
reg = LinearRegression()

# Fit the model using the specified features and target variable
# Make sure to adjust the column names if they are different in your DataFrame
reg.fit(df[['Users', 'Orders', 'Age']], df['Amount'])

# Predict the amount for a new data point
new_data = [[500, 562, 25]]
predicted_amount = reg.predict(new_data)
print("Predicted amount:", predicted_amount)
