'''import requests

url = "https://rawg-video-games-database.p.rapidapi.com/games/fifa"

headers = {
    'x-rapidapi-key': "abb52e9723084913a5e0668b3c92523f",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)'''

import rawgpy

rawg = rawgpy.RAWG("User-Agent, I would like to use RAWG's API to do a personal project for searching different video games and their prices")
results = rawg.search("Warframe")  # defaults to returning the top 5 results
print(results)
#game = results[0]
#game.populate()  # get additional info for the game

#print(game.name)

#print(game.description)

#for store in game.stores:
   # print(store.url)

#rawg.login("godwinsilayo100@gmail.com", "Godweezy1557")

#me = rawg.current_user()

#print(me.name) # print my name, equivalent to print(self.username)

#me.populate() # gets additional info for the user

#for game in me.playing:
    #print(game.name) # prints all the games i'm currently playing