import requests
from pprint import pprint

# API endpoint for Sheety
SHEETY_ENDPOINT = "https://api.sheety.co/bc8b4dd28500c818560b5d44d71cf605/flightDeals1/prices"
# The sheet name you're working with
SHEET_NAME = "Flight Deals1"
# Your Sheety API key
SHEETY_API_KEY = "https://api.sheety.co/bc8b4dd28500c818560b5d44d71cf605/flightDeals1/prices"

# Headers for the Sheety API request
headers = {
    "Authorization": f"Bearer {SHEETY_API_KEY}"
}

# Parameters for the Sheety API request
params = {
    "sheet": SHEET_NAME
}

# Make a GET request to the Sheety API to get all the data in the sheet
response = requests.get(url=SHEETY_ENDPOINT, headers=headers, params=params)
response.raise_for_status()

# Get the JSON data from the response
data = response.json()
pprint(data)
