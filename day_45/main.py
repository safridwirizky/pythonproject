from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify())