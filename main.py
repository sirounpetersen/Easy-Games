from flask import Flask, request, render_template, flash
from api import anticipated_games, the_most_popular, search, platform_games,pricelookup
import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


app = Flask(__name__)
app.config['SECRET_KEY'] = '2d6ca153ea201fe4daf5a90f380026b5'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/home") 
def home_2():
    return render_template("home.html")


@app.route("/search", methods=['POST'])
def home_post():
    name = request.form.get('name')
    name2 = name.replace(" ", "+")
    try:
        detail, image, rate, platform, platformRate, website = search(name)
        if website == "":
            website = "/notfound"
        return render_template("search.html", name=name.upper(),
                               detail=cleanhtml(detail),
                               image=image, rate=rate,
                               website=website,
                               both=zip(platform, platformRate), name2=name2)
    except Exception:
        flash('Your search keyword was not found. Try again!')
        return render_template("home.html")


a, b, plus = the_most_popular()


@app.route("/trending")  
def trending():
    global a
    global b
    global plus
    return render_template("trending.html", both=zip(a, b, plus))


@app.route("/platform")
def platform():
    return render_template("platform.html")


@app.route("/platformGames", methods=['POST'])
def platform_post():
    platformName = request.form.get("console")
    game2, gameplus = platform_games(platformName)
    return render_template('platformGames.html',
                           console=platformName, games=zip(game2,gameplus))


c, d, gamep = anticipated_games()


@app.route("/anticipated")
def anticipated():
    global c
    global d
    global gamep
    return render_template("anticipated.html", both=zip(c, d,gamep))


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/notfound")
def notfound():
	return render_template("notfound.html")

@app.route("/search/<keyword>") # for turning names into links
def search_name(keyword):
	name = keyword.replace("+"," ")
	try:
		detail, image, rate, platform, platformRate,website = search(name)
		return render_template("search.html", name=name.upper(), detail=cleanhtml(detail), 
													 image=image, rate=rate, website=website, both=zip(platform,platformRate))
	except:
            flash(f'{name} was not found. Try again!')
            return render_template("home.html")


@app.route("/priced/<name2>")
def price_post(name2):
  game = name2.replace("+"," ")
  print(game)
  game_name, game_price, game_condition, game_link = pricelookup(game)
	
  return render_template("priced.html", 
												 info = zip(game_name,game_price, game_condition,game_link))

	 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
