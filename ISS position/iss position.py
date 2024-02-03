import time
import requests
from datetime import datetime
import smtplib

LAT = 21.170240
LNG = 72.831062
my_email = os.environ["MY_GMAIL"]
password = os.environ["PASSWORD"]


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)

    if LAT-5 <= latitude <= LAT+5 and LNG-5 <= longitude <= LNG+5:
        return True


def is_night():
    parameters = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="sahil@gmail.com",
                                msg="Subject:ISS IS OVERHEAD\n\nLOOK UP 👆🏻")
