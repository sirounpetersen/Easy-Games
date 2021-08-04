import json
import requests
params = {
						'api_key': '165DFEB03D1E4603869943DA6574781D',
						'type': 'search',
						'ebay_domain': 'ebay.com',
						'search_term': "valheim"
					}
response = requests.get('https://api.countdownapi.com/request', params)

data = response.json()

game_name = [data["search_results"][i]["title"] for i in range(len(data["search_results"]))]
game_price = [data["search_results"][i]["prices"][0]["raw"] for i in range(len(data["search_results"]))]
game_condition = [data["search_results"][i]["condition"] for i in range(len(data["search_results"]))]
buying_site = [data["search_results"][i]["link"] for i in range(len(data["search_results"]))]

a = zip(game_name,game_condition,game_price,buying_site)
for game_name,game_condition,game_price,buying_site in a:
	print(game_name,game_condition,game_price,buying_site)