import requests
import json
import matplotlib.pyplot as plt

# Step 1: Fetch data from the APIs
api1_url = 'https://isro.vercel.app/api/spacecrafts'
api2_url = 'https://isro.vercel.app/api/customer_satellites'

spacecrafts_response = requests.get(api1_url)
customer_satellites_response = requests.get(api2_url)

# Check if the responses are successful
if spacecrafts_response.status_code == 200 and customer_satellites_response.status_code == 200:
    # Load JSON data from the responses
    spacecrafts_data = json.loads(spacecrafts_response.text)
    customer_satellites_data = json.loads(customer_satellites_response.text)

    # Step 2: Process the data
    isro_spacecraft_count = sum(1 for spacecraft in spacecrafts_data['spacecrafts'] if 'owner' not in spacecraft or spacecraft['owner'] == 'ISRO')
    customer_satellites_count = len(customer_satellites_data['customer_satellites'])

    # Step 3: Calculate the percentages
    total_spacecrafts = isro_spacecraft_count + customer_satellites_count
    percentage_isro = (isro_spacecraft_count / total_spacecrafts) * 100
    percentage_customers = (customer_satellites_count / total_spacecrafts) * 100

    # Step 4: Generate the pie chart
    labels = ['ISRO', 'Customer Satellites']
    sizes = [percentage_isro, percentage_customers]
    colors = ['blue', 'orange']
    explode = (0.1, 0)  # To highlight the ISRO section

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

    plt.title("Percentage of ISRO's Own Spacecraft vs. Customer Satellites")
    plt.show()
else:
    print("Failed to fetch data from the API(s). Check the URLs and try again.")
