import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"
SID = "AC470e91d85e76e6dba2c489fd4372f057"
Auth_Token = "e88a40c2412c43d0b6f1050c865162d7"

parameters = {
    "lon": 9.198600,
    "lat": 50.424580,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}


response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(SID, Auth_Token)

    message = client.messages.create(
        body="Its going to rain today, Remember to bring an umbrella",
        from_="+16692094938",
        to="+917008046177"
    )
