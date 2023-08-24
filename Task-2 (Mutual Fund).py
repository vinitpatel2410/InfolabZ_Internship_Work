import requests

# Mutual Fund API
mutual_fund_url = "https://api.mfapi.in/mf"

# 1) Print total count of mutual funds
response = requests.get(mutual_fund_url)
mutual_fund_data = response.json()
total_mutual_funds = len(mutual_fund_data)
print("Total count of mutual funds:", total_mutual_funds)

# 2) Print all data using a for loop (scheme code: _____ scheme name: ________________)
for fund in mutual_fund_data:
    print("Scheme code: {} Scheme name: {}".format(fund["schemeCode"], fund["schemeName"]))

# 3) Allow the user to insert a scheme code, search, and print the scheme name
user_scheme_code = input("Enter a scheme code to search: ")
found = False
for fund in mutual_fund_data:
    if str(fund["schemeCode"]) == user_scheme_code:
        print("Scheme name: {}".format(fund["schemeName"]))
        found = True
        break

if not found:
    print("No scheme found with the given scheme code.")
