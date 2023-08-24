import requests

# Get user input for the PINCODE
user_pincode = input("Enter the PINCODE: ")

# Construct the API URL with the user-provided PINCODE
url = f"https://api.postalpincode.in/pincode/{user_pincode}"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Check if the PINCODE is valid and has data
if data[0]['Status'] == 'Success':
    # Extract the names of all areas under the provided PINCODE
    areas = data[0]['PostOffice']
    area_names = [area['Name'] for area in areas]

    # Print the names of all areas
    print(f"The areas under PINCODE {user_pincode} are:")
    for area_name in area_names:
        print(area_name)
else:
    print(f"Invalid PINCODE: {user_pincode}")
