import requests
from flight_data import FlightData
import os

TEQUILA_APIKEY = os.environ.get("TEQUILA_APIKEY")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

headers = {
            "apikey": TEQUILA_APIKEY
        }

class FlightSearch:
    def __init__(self):
        self.city_codes = []
    def get_iatacode(self, citynames):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        for city in citynames:
            query = {"term": city, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)

        return self.city_codes

    def check_flights(self, from_city_code, to_city_code, from_time, to_time):
        # Round Trip
        query = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }

        # One Way
        # query = {
        #     "fly_from": from_city_code,
        #     "fly_to": to_city_code,
        #     "date_from": from_time.strftime("%d/%m/%Y"),
        #     "date_to": to_time.strftime("%d/%m/%Y"),
        #     "one_for_city": 1,
        #     "max_stopovers": 0,
        #     "curr": "INR"
        # }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                from_city=data["route"][0]["cityFrom"],
                from_airport=data["route"][0]["flyFrom"],
                to_city=data["route"][0]["cityTo"],
                to_airport=data["route"][0]["flyTo"],
                going_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            # Round Trip
            flight_data = FlightData(
                price=data["price"],
                from_city=data["route"][0]["cityFrom"],
                from_airport=data["route"][0]["flyFrom"],
                to_city=data["route"][0]["cityTo"],
                to_airport=data["route"][0]["flyTo"],
                going_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data

        # One way
        # flight_data = FlightData(
        #     price=data["price"],
        #     from_city=data["route"][0]["cityFrom"],
        #     from_airport=data["route"][0]["flyFrom"],
        #     to_city=data["route"][0]["cityTo"],
        #     to_airport=data["route"][0]["flyTo"],
        #     going_date=data["route"][0]["local_departure"].split("T")[0]
        # )
        # return flight_data
