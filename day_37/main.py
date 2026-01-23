import requests, os
from datetime import datetime

TOKEN = os.getenv("OWM_TOKEN_PIXELA")
USERNAME = "masaprol"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

param_graph = {
    "id": "a1",
    "name": "Habit Tracker",
    "unit": "repetition",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, headers=header, json=param_graph)
# print(response.text)

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/a1"

param_pixel = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "10"
}

response = requests.post(url=pixel_endpoint, headers=header, json=param_pixel)
print(response.text)