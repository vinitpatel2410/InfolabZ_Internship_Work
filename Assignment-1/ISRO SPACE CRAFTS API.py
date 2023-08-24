import requests
#Print all main keys and the total number of main keys as well.
url = "https://isro.vercel.app/api/spacecrafts"
response = requests.get(url)
data = response.json()

main_keys = data.keys()
num_main_keys = len(main_keys)

print("Main keys in the API:")
print(main_keys)
print("Total number of main keys:", num_main_keys)
#Print all spacecraft names in the specified output format:
print("Spacecraft names:")
for index, spacecraft in enumerate(data['spacecrafts'], 1):
    print(f"{index}. {spacecraft['name']}")
#Allow the user to enter the name of the spacecraft. Print whether the spacecraft is found or not:
# Get user input
user_input = input("Enter the name of the spacecraft: ")

# Check if the spacecraft exists in the data
spacecraft_names = [spacecraft['name'].lower() for spacecraft in data['spacecrafts']]
if user_input.lower() in spacecraft_names:
    print("Spacecraft found!")
else:
    print("Spacecraft not found.")
