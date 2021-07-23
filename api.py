#GETTING THE MOST ANTICIPATED GAMES OF THE 2022 AND THEIR IMAGES
#these are the most anticipated games of 2022

import requests
import json

#getting the most anticipated games
def anticipated_games():
    headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }
    key = {"key":"abb52e9723084913a5e0668b3c92523f"}
    url = "https://api.rawg.io/api/games?dates=2022-01-01,2022-12-31&ordering=-added"
    response = requests.get(url, headers=headers, params=key)
    data = response.json()
    game_name = [data['results'][i]['name'] for i in range(len(data['results']))]
    image_link = [data['results'][i]['background_image'] for i in range(len(data['results']))]
    GameName = []
    ImageLink = []
    for i in range(len(image_link)):
        if image_link[i] != None:
            GameName.append(game_name[i])
            ImageLink.append(image_link[i])
    
    return GameName, ImageLink

#GETTING THE MOST POPULAR GAMES FOR 2021
def the_most_popular():
    headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }
    key = {"key":"abb52e9723084913a5e0668b3c92523f"}
    url = "https://api.rawg.io/api/games?dates=2021-01-01,2021-12-31&ordering=-added"
    response = requests.get(url, headers=headers, params=key)
    data = response.json()
    game_name = [data['results'][i]['name'] for i in range(len(data['results']))]
    image_link = [data['results'][i]['background_image'] for i in range(len(data['results']))]
    
    return game_name, image_link

#MAKING A GAME SEARCH TO GET GAME DETAILS, GAME RATING, AND RATING BASED ON CONSOLE 
def search(gameName):
    headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }
    key = {"key":"abb52e9723084913a5e0668b3c92523f"}
    
    name = gameName.replace(" ", "-")

    url = "https://api.rawg.io/api/games/"+name
    response = requests.get(url, headers=headers, params=key)

    data = response.json()

    game_description = data['description']
    game_rating = data['metacritic'] #CHANGES to Remove tags
    game_image = data['background_image']
    website_link = data["website"]
    platform_name = [data['metacritic_platforms'][i]['platform']['name'] for i in range(len(data['metacritic_platforms']))]
    platform_rating = [data['metacritic_platforms'][i]['metascore'] for i in range(len(data['metacritic_platforms']))]
		
    return game_description, game_image, game_rating, platform_name, platform_rating, website_link
   
'''
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
	games_availablePS5 = [(data['results'][i]['name']) for i in range(len(data['results']))]'''


#GETTING GAMES BASED ON THE CONSOLE
def platform_games(p_name):
    page = 1
    platform_ids = {"PC": "4", "Playstation 5":"187", "Xbox Series S/X":"186", "Playstation 4":"18","Xbox One":"1", 
										"Nintendo": "7"}
    #p_name = input("Choose your platform, (PC, Playstation 5, Xbox Series S/X): ") #to be replaced by the data from html
    id_no = platform_ids[p_name]
    while(page <= 5):
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

        return games_available
