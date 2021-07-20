
'''#THIS GIVES US THE PLATFORM AND THE PLATFORM ID'S
import requests
import json

url = "https://api.rawg.io/api/platforms"

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
#, "page":"1", "page_size":"1"
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()
for i in range(len(data['results'])):
	#print(data['results'][i]['name'], data['results'][i]['released'])
  print(data['results'][i]['id'], data['results'][i]['name'])'''

  
#GETTING GAMES ON A PARTICULAR PLATFORM IN A SPECIFIC TIME FRAME
'''import requests
import json

url = "https://api.rawg.io/api/games?dates=2021-06-01,2021-06-30&platforms=187"

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
#, "page":"1", "page_size":"1"
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()
#for i in range(len(data['results'])):
	#print(data['results'][i]['name'], data['results'][i]['released'])
  #print(data['results'][i]['id'], data['results'][i]['name'])
  
print(len(data['results']))'''


#GETTING THE MOST ANTICIPATED GAMES OF THE 2022 AND THEIR IMAGES
#these are the most anticipated games of 2022

import requests
import json

url = "https://api.rawg.io/api/games?dates=2022-01-01,2022-12-31&ordering=-added"

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
#, "page":"1", "page_size":"1"
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()
for i in range(len(data['results'])):
	print(data['results'][i]['name'], 'and image link is: ', data['results'][i]['background_image'] )
  
print(('')*2)
  
#GETTING THE MOST POPULAR GAMES RIGHT NOW AND THEIR IMAGES
#these are the games that are hot right now
import requests
import json

url = "https://api.rawg.io/api/games?dates=2021-01-01,2021-12-31&ordering=-added"

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
#, "page":"1", "page_size":"1"
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()
for i in range(len(data['results'])):
	print(data['results'][i]['name'], 'and image link is: ', data['results'][i]['background_image'] )
  
  


