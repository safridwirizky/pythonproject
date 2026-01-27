import requests, os, json
from datetime import datetime

APP_ID = os.getenv("OWM_APP_ID")
API_KEY = os.getenv("OWM_API_KEY")
URL = "https://app.100daysofpython.dev"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# POST url
post_url = "/v1/nutrition/natural/exercise"

record = input("What your excercise?\n")

post_body = {
    "query": record
}

response = requests.post(url=URL+post_url, headers=header, json=post_body)
print(response.text)

data = json.loads(response.text)

exercise = data['exercises'][0]['name']
duration = int(data['exercises'][0]['duration_min'])
calories = int(data['exercises'][0]['nf_calories'])


# ---------------------------- Sheety ------------------------- #

sheet_url = "https://api.sheety.co/5d6a4a777fa70a7800399023828a2d14/myWorkouts/workouts"

sheet_header = {
    "Authorization": f'Bearer {os.getenv("OWM_AUTH_SHEETY")}'
}

responses = requests.get(url=sheet_url, headers=sheet_header)

# Get data from Sheety
responses.raise_for_status()
print(responses.json())

# Post data to Google Spreadsheet
sheet_param = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

responses = requests.post(url=sheet_url, headers=sheet_header, json=sheet_param)
print(responses.text)