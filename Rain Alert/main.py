import requests

END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "54299aa5ef44f42356a64564ceda8d55"

weather_params = {
    "lat": 21.170240,
    "lon": 72.831062,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(END_POINT, params=weather_params)
response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0]["id"]) current weather condition code
will_rain = False
for hours in data["list"]:
    condition_code = hours["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True
if will_rain:
    print("Bring an Umbrella.")

