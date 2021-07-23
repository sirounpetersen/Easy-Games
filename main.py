from flask import Flask, request, render_template
from api import anticipated_games,the_most_popular,search,platform_games


app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/home") #Why do we have this route too
def home_2():
	return render_template("home.html")

@app.route("/search", methods=['POST'])
def home_post():
	name = request.form.get('name')
	#print(name)
	try:
		detail, image, rate, platform, platformRate,website = search(name)
		return render_template("search.html", name=name.upper(), detail=detail, 
													 image=image, rate=rate, website=website, both=zip(platform,platformRate))#website=website,
	except:
		return '<script>window.alert("Your search keyword was not found. Try again!"); window.open("/home")</script>'


a,b = the_most_popular()
@app.route("/trending") #Changing the navbar to trending
def trending():
	global a
	global b
	return render_template("trending.html", both = zip(a,b))

@app.route("/platform")
def platform():
	return render_template("platform.html")

#@app.route("/platform")
#def platform_post():
  #pass
@app.route("/platformGames", methods=['POST'])
def platform_post():
	platformName =request.form.get("console")
	games = platform_games(platformName)
	print(games)
	return render_template('platformGames.html', console = platformName, games=games)
 
c,d = anticipated_games()
@app.route("/anticipated")
def anticipated():
	global c
	global d
	return render_template("anticipated.html", both = zip(c,d)) #create a template similar to trending
	
@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")

