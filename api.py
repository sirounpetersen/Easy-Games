import requests
import json


# GETTING THE MOST ANTICIPATED GAMES OF THE 2022 AND THEIR BACKGROUND IMAGES
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

    game_plus = [game.replace(" ", "+") for game in GameName]
    return GameName, ImageLink,game_plus

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
    game_plus = [game.replace(" ", "+") for game in game_name]
    image_link = [data['results'][i]['background_image'] for i in range(len(data['results']))]
    
    return game_name, image_link,game_plus

#MAKING A GAME SEARCH TO GET GAME DETAILS, GAME RATING, AND RATING BASED ON CONSOLE 
def search(gameName):
    headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }
    key = {"key":"abb52e9723084913a5e0668b3c92523f"}
    
    name = ((gameName.replace("- ","")).replace(" ", "-")).replace(":","")

    url = "https://api.rawg.io/api/games/"+name
  
    response = requests.get(url, headers=headers, params=key)

    data = response.json()

    game_description = data['description']
    game_rating = data['metacritic'] 
    game_image = data['background_image']
    website_link = data["website"]
    platform_name = [data['metacritic_platforms'][i]['platform']['name'] for i in range(len(data['metacritic_platforms']))]
    platform_rating = []
    if game_rating == None: #game_rating = None
        platform_rating.append("No ratings available")
    else:
        platform_rating = [data['metacritic_platforms'][i]['metascore'] for i in range(len(data['metacritic_platforms']))]
		
    return game_description, game_image, game_rating, platform_name, platform_rating, website_link


#GETTING GAMES BASED ON THE CONSOLE
def platform_games(p_name):
    page = 1
    platform_ids = {"PC": "4", "Playstation 5":"187", "Xbox Series S/X":"186", "Playstation 4":"18","Xbox One":"1", 
										"Nintendo": "7"}
    #p_name = input("Choose your platform, (PC, Playstation 5, Xbox Series S/X): ") #to be replaced by the data from html
    id_no = platform_ids[p_name]
    url = "https://api.rawg.io/api/games?platforms="+id_no
    
    while(page <= 2):
        key = {"key":"abb52e9723084913a5e0668b3c92523f", "page":str(page), "page_size":"39"}
        page += 1
        headers = {
            'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
            'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
                }

        response = requests.get(url, headers=headers, params=key)

        data = response.json()
        games_available = [(data['results'][i]['name']) for i in range(len(data['results']))]

    game_nospace = [game.replace(" ", "+") for game in games_available]

    return games_available, game_nospace
			
# GETTING PRICES FOR GAMES
def pricelookup(name):
    params = {
                'api_key': 'BA7332E6CF724523A1310BB86893D054',
                'type': 'search',
                'ebay_domain': 'ebay.com',
                'search_term': name
              }
    response = requests.get('https://api.countdownapi.com/request', params)
    
    data = response.json()
    
    game_name = [data["search_results"][i]["title"] for i in range(len(data["search_results"]))]
    game_price = [data["search_results"][i]["prices"][0]["raw"] for i in range(len(data["search_results"]))]
    game_condition = [data["search_results"][i]["condition"] for i in range(len(data["search_results"]))]
    buying_site = [data["search_results"][i]["link"] for i in range(len(data["search_results"]))]
    
    return game_name, game_price, game_condition, buying_site

