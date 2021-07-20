import requests
import json

url = "https://rawg-video-games-database.p.rapidapi.com/games"

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
#, "page":"1", "page_size":"1"
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()
for i in range(len(data['results'])):
	print(data['results'][i]['name'], data['results'][i]['released'])
