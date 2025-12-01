from twilio.rest import Client
import requests
import os

account_sid = os.environ.get("OWM_ACCOUNT_SID")
auth_token = os.environ.get("OWM_AUTH_TOKEN")
client = Client(account_sid, auth_token)

MY_LATITUDE = -10.755157
MY_LONGITUDE = 123.059333
API_KEY = os.environ.get("OWM_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_forecast = ["It will rain. don't forget to bring an Umbrella" if x["weather"][0]["id"] < 700 else "It will Dry" for x in weather_data["list"]]

messages = ''

for i, weather in enumerate(weather_forecast):
    match i:
        case 0:
            messages += f"06:00 AM = {weather}\n\n"
        case 1:
            messages += f"09:00 AM = {weather}\n\n"
        case 2:
            messages += f"12:00 PM = {weather}\n\n"
        case 3:
            messages += f"03:00 PM = {weather}"

message = client.messages.create(
    from_= 'whatsapp:+14155238886',
    body= messages,
    to= os.environ.get("OWM_WA_NUMBER")
)

print(message.sid)