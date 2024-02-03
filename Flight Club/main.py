from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination()

ORIGIN_CITY_IATA = "BOM"

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_iatacode(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_later = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_later
    )
    if flight is None:
        continue
    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstname"] for row in users]

        # Round Trip
        message = (f"Only ₹{flight.price}\n"
                   f"{flight.from_city}-{flight.from_airport} -> "
                   f"{flight.to_city}-{flight.to_airport}\n"
                   f"{flight.going_date} to {flight.return_date}.")

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        notification_manager.send_emails(emails, message)
        # One Way
        # notification_manager.send_email(message=f"Only ₹{flight.price}\n"
        #                                         f"{flight.from_city}-{flight.from_airport} -> "
        #                                         f"{flight.to_city}-{flight.to_airport}\n"
        #                                         f"{flight.going_date}.")
