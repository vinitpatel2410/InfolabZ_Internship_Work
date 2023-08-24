import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the CSV file into a DataFrame
df = pd.read_csv("Advertising.csv")

# Print the first few rows of the DataFrame
print(df.head())

# Create a LinearRegression model
reg = LinearRegression()

# Fit the model using the specified features (TV, radio, newspaper) and target variable (sales)
reg.fit(df[['TV', 'radio', 'newspaper']], df['sales'])

# Predict the sales for a new data point
new_data = pd.DataFrame({'TV': [230.1], 'radio': [37.8], 'newspaper': [69.2]})
predicted_sales = reg.predict(new_data)
print("Predicted sales:", predicted_sales)
