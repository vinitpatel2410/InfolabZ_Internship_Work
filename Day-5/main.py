import pandas as pd
import requests
import matplotlib.pyplot as plt

# Task-1
data1 = pd.read_excel('RESULT1.xlsx')
data2 = pd.read_excel('RESULT2.xlsx')
print("Task-1: Data from RESULT1.xlsx:")
print(data1)
print("\nTask-1: Data from RESULT2.xlsx:")
print(data2)

# Task-2
merged_data = pd.concat([data1, data2], ignore_index=True)
plt.bar(merged_data['NAME'], merged_data['TOTAL'])
plt.xlabel('Name')
plt.ylabel('Total')
plt.title('Task-2: Bar graph of Total Scores')
plt.xticks(rotation=45, ha='right')
plt.show()

# Task-3
total_sum = merged_data['TOTAL'].sum()
print(f"Task-3: Total sum of 'TOTAL' column: {total_sum}")

# Task-4
sorted_data = merged_data.sort_values(by='TOTAL', ascending=False)
print("Task-4: Data sorted in decreasing order:")
print(sorted_data)

# Task-5
filtered_data = merged_data[merged_data['TOTAL'] > 200]
print("Task-5: Data with 'TOTAL' greater than 200:")
print(filtered_data)

# Task-6
def categorize_score(score):
    if 80 <= score <= 100:
        return 'scholar'
    elif 50 <= score <= 79:
        return 'average'
    else:
        return 'weak'

# Let's check the column names and adjust accordingly
print("Column names in merged_data:")
print(merged_data.columns)

if 'PERCENTA' in merged_data.columns:
    merged_data['CATEGORY'] = merged_data['PERCENTA'].apply(categorize_score)
    print("Task-6: Data with the 'CATEGORY' column:")
    print(merged_data)
else:
    print("'PERCENTA' column not found in the data. Please check the column names.")

# Task-7
url = 'https://data.covid19india.org/data.json'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    covid_data = pd.DataFrame(data['cases_time_series'])
    covid_data.to_csv('covid_data.csv', index=False)
    covid_data.to_excel('covid_data.xlsx', index=False)
    print("Task-7: Successfully fetched data and created csv and excel files.")
else:
    print("Task-7: Failed to fetch data from the API.")
