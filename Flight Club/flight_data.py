class FlightData:
    # Round trip
    def __init__(self, price, from_city, from_airport, to_city, to_airport, going_date, return_date, stop_overs=0,
                 via_city=""):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.going_date = going_date
        self.return_date = return_date
        self.stop_over = stop_overs
        self.via_city = via_city

    # One Way
    # def __init__(self, price, from_city, from_airport, to_city, to_airport, going_date):
    #     self.price = price
    #     self.from_city = from_city
    #     self.from_airport = from_airport
    #     self.to_city = to_city
    #     self.to_airport = to_airport
    #     self.going_date = going_date
