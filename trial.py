
'''#PlayStation Store ID is: 3 and domain is:  store.playstation.com
#Xbox Store ID is: 2 and domain is:  microsoft.com

4 PC
187 PlayStation 5
186 Xbox Series S/X'''


# THIS GIVES US THE PLATFORM AND THE PLATFORM ID'S
# here we can get the different platforms we want
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
  print(data['results'][i]['id']," is for" ,data['results'][i]['name'])
  
  '''


# GETTING GAMES ON A PARTICULAR PLATFORM IN A SPECIFIC TIME FRAME
# here we can get any game we want on any platform and it's release date
import requests
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
for i in range(len(data['results'])):
	print(data['results'][i]['name'], data['results'][i]['released'])
  

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
  
  
#GETTING THE TOP RATED GAMES RIGHT NOW
#these are the games that people like right now
import requests
import json

url = "https://api.rawg.io/api/games?dates=2021-01-01,2021-12-31&ordering=-rating"

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()
for i in range(len(data['results'])):
	print(data['results'][i]['name'], 'and image link is:', data['results'][i]['background_image'] )




#GETTING STORE DATA THAT CAN HELP GET PRICE
#these are the games that people like right now
import requests
import json

url = "https://rawg-video-games-database.p.rapidapi.com/stores/2"

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()
for i in range(len(data['results'])):
	print(data['results'][i]['name'], 'ID is:', data['results'][i]['id'],'and domain is: ',data['results'][i]['domain'])

#THIS GETS THE MOST POPULAR GAMES ON ANY PLATFORM IN ANYTIME FRAME
import requests
import json

url = "https://api.rawg.io/api/games?dates=2020-01-01,2021-12-31&platforms=186&ordering=-added"

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()
for i in range(len(data['results'])):
	print(data['results'][i]['name'])
  

  
#GETTING THE GAMES ON A PLATFORM
import requests
import json

page = 1
while(page <= 3):
  url = "https://api.rawg.io/api/games?platforms=187"

  key = {"key":"abb52e9723084913a5e0668b3c92523f", "page":str(page), "page_size":"39"}
  page += 1
  headers = {
        'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
        'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
            }

  response = requests.get(url, headers=headers, params=key)

  data = response.json()
	games_availablePS5 = [(data['results'][i]['name']) for i in range(len(data['results']))]

  

#GETTING THE RATINGS FOR GAME
import requests
import json

url = "https://api.rawg.io/api/games/fifa-21" #format the user input

key = {"key":"abb52e9723084913a5e0668b3c92523f"}
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=key)

data = response.json()

#print(data)

print(data['description'])
print('')
print(data['metacritic'])
print('')
for i in range(len(data['metacritic_platforms'])):
  print(data['metacritic_platforms'][i]['metascore'],": ", data['metacritic_platforms'][i]['platform']['name'])
print(data['background_image'])







import requests
import json

page = 1
platform_ids = {"PC": "4", "PlayStation 5":"187", "Xbox Series S/X":"186"}
p_name = input("Choose your platform, (PC, Playstation 5, Xbox Series S/X): ")
while(True):
	if p_name in platform_ids.keys():
		break
	else:
		print("Enter a name as shown")
		p_name = input("Choose your platform, (PC, Playstation 5, Xbox Series S/X): ")

id_no = platform_ids[p_name]
while(page <= 3):
		url = "https://api.rawg.io/api/games?platforms="+id_no

		key = {"key":"abb52e9723084913a5e0668b3c92523f", "page":str(page), "page_size":"39"}
		page += 1
		headers = {
				'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
				'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
						}

		response = requests.get(url, headers=headers, params=key)

		data = response.json()
		games_available = [(data['results'][i]['name']) for i in range(len(data['results']))]

print(p_name)
for i in range(10):
	print(games_available[i])'''






  



