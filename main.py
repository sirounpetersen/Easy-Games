from flask import Flask, request, render_template, flash
<<<<<<< HEAD
from api import anticipated_games,the_most_popular,search,platform_games
=======
from api import anticipated_games, the_most_popular, search, platform_games
>>>>>>> 1d869aa421331924e7217ed96fab128135be4ab3
import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


app = Flask(__name__)
app.config['SECRET_KEY'] = '2d6ca153ea201fe4daf5a90f380026b5'
<<<<<<< HEAD
=======

>>>>>>> 1d869aa421331924e7217ed96fab128135be4ab3

@app.route("/")
def home():
    return render_template("home.html")


<<<<<<< HEAD
@app.route("/home") 
=======
@app.route("/home")  # Why do we have this route too
>>>>>>> 1d869aa421331924e7217ed96fab128135be4ab3
def home_2():
    return render_template("home.html")


@app.route("/search", methods=['POST'])
def home_post():
<<<<<<< HEAD
	name = request.form.get('name')
	try:
		detail, image, rate, platform, platformRate,website = search(name)
		if website == "":
			website = "/notfound"
		#print(platformRate)	
		#print(platform)
		return render_template("search.html", name=name.upper(), detail=cleanhtml(detail), 
                               image=image, rate=rate, website=website, both=zip(platform,platformRate))
	except:
            flash(f'Your search keyword was not found. Try again!')
            return render_template("home.html")

a,b = the_most_popular()
@app.route("/trending") #Changing the navbar to trending
=======
    name = request.form.get('name')
    try:
        detail, image, rate, platform, platformRate, website = search(name)
        return render_template("search.html", name=name.upper(),
                               detail=cleanhtml(detail),
                               image=image, rate=rate,
                               website=website,
                               both=zip(platform, platformRate))
    except Exception:
        flash('Your search keyword was not found. Try again!')
        return render_template("home.html")


a, b = the_most_popular()


@app.route("/trending")  # Changing the navbar to trending
>>>>>>> 1d869aa421331924e7217ed96fab128135be4ab3
def trending():
    global a
    global b
    return render_template("trending.html", both=zip(a, b))


@app.route("/platform")
def platform():
    return render_template("platform.html")


@app.route("/platformGames", methods=['POST'])
def platform_post():
    platformName = request.form.get("console")
    games = platform_games(platformName)
    return render_template('platformGames.html',
                           console=platformName, games=games)


c, d = anticipated_games()


@app.route("/anticipated")
def anticipated():
    global c
    global d
    return render_template("anticipated.html", both=zip(c, d))


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/notfound")
def notfound():
	return render_template("notfound.html")


if __name__ == '__main__':
<<<<<<< HEAD
  app.run(debug=True, host="0.0.0.0")

'''
@app.route("/search/<keyword>", methods=['POST'])
def search_name(keyword):
	name = keyword
	#print(name)
	try:
		detail, image, rate, platform, platformRate,website = search(name)
		return render_template("search.html", name=name.upper(), detail=cleanhtml(detail), 
													 image=image, rate=rate, website=website, both=zip(platform,platformRate))
	except:
		return '<script>window.alert("Your search keyword was not found. Try again!"); window.open("/home")</script>'
'''


=======
    app.run(debug=True, host="0.0.0.0")
>>>>>>> 1d869aa421331924e7217ed96fab128135be4ab3
