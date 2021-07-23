import requests
import json
'''
headers = {
    'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }
key = {"key":"abb52e9723084913a5e0668b3c92523f"}

gameName = input("Enter input: ")
name = gameName.replace(" ", "-")

url = "https://api.rawg.io/api/games/"+name
response = requests.get(url, headers=headers, params=key)

data = response.json()

game_description = data['description']
game_rating = data['metacritic']
game_image = data['background_image']
platform_name = [data['metacritic_platforms'][i]['platform']['name'] for i in range(len(data['metacritic_platforms']))]
platform_rating = [data['metacritic_platforms'][i]['metascore'] for i in range(len(data['metacritic_platforms']))]

print( game_description, game_image, game_rating, platform_name, platform_rating )'''

'''
page = 1
platform_ids = {"PC": "4", "PlayStation 5":"187", "Xbox Series S/X":"186"}
p_name = input("Choose your platform, (PC, Playstation 5, Xbox Series S/X): ") #to be replaced by the data from html

while(True): #checking the input if is valid
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

		return p_name, games_available
'''
'''
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
				
print(GameName)
print(ImageLink)'''

headers = {
'x-rapidapi-key': "e75704e1c2mshd99b5c5f595246bp19e6dajsn4f38aacd6f57",
'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
}
key = {"key":"abb52e9723084913a5e0668b3c92523f"}

#name = gameName.replace(" ", "-")

url = "https://api.rawg.io/api/games/fifa-21"
response = requests.get(url, headers=headers, params=key)

data = response.json()

game_description = data['description']
game_rating = data['metacritic']
game_image = data['background_image']
website_link = data["website"]
platform_name = [data['metacritic_platforms'][i]['platform']['name'] for i in range(len(data['metacritic_platforms']))]
platform_rating = [data['metacritic_platforms'][i]['metascore'] for i in range(len(data['metacritic_platforms']))]

print(website_link)