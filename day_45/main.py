from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("span.content_content__i0P3p h2 strong")

movies = []
for title in titles:
    text = title.get_text()
    if ")" not in text:
        continue
    movies.append(text)

with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies[::-1]:
        file.write(movie + '\n')