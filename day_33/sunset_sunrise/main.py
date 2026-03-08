import requests

MY_LAT = -7.626293
MY_LONG = 109.115922

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

url = "https://api.sunrise-sunset.org/json"
response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
print(data["results"]["sunrise"])