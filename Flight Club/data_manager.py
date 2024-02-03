import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
SHEET_USERS_ENDPOINT = os.environ.get("SHEET_USERS_ENDPOINT")
BASIC_AUTH = os.environ.get("BASIC_AUTH")


headers = {
            "Authorization": f"Basic {BASIC_AUTH}",
            "Content-Type": "application/json",
        }


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

    def get_destination(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers,
            )
            print(response.text)
