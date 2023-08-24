import requests

# ISRO API
isro_url = "https://isro.vercel.app/api/spacecrafts"

# 1) Print total count of spacecraft
response = requests.get(isro_url)
isro_data = response.json()
total_spacecrafts = len(isro_data["spacecrafts"])
print("Total count of spacecrafts:", total_spacecrafts)

# 2) Print all data using a for loop (ID and Name)
for spacecraft in isro_data["spacecrafts"]:
    print("ID: {} Name: {}".format(spacecraft["id"], spacecraft["name"]))

# 3) Allow the user to insert an ID to get the spacecraft name, also if not found, print not found
user_spacecraft_id = input("Enter the spacecraft ID to get its name: ")
found = False
for spacecraft in isro_data["spacecrafts"]:
    if str(spacecraft["id"]) == user_spacecraft_id:
        print("Spacecraft name: {}".format(spacecraft["name"]))
        found = True
        break

if not found:
    print("Spacecraft not found with the given ID.")
